
import pandas as pd
import os

filepath = 'tmdb/processed_movies.csv'


def load_csv(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV file not found: {filepath}")

    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        print(f"Unexpected error while loading CSV: {e}")

    return df


df = load_csv(filepath)


def add_movie_type():
    df["movie_type"] = df["belongs_to_collection"].apply(
        lambda x: "Franchise" if pd.notna(x) else "Standalone"
    )
    return df


def compare_franchise_vs_standalone():
    df = add_movie_type()
    df["roi"] = df['revenue'] / df['budget']

    grouped = df.groupby("movie_type").agg({
        "revenue": "mean",
        "roi": "median",
        "budget": "mean",
        "popularity": "mean",
        "vote_average": "mean"
    })

    grouped = grouped.rename(columns={
        "revenue": "mean_revenue",
        "roi": "median_roi",
        "budget": "mean_budget",
        "popularity": "mean_popularity",
        "vote_average": "mean_rating"
    })

    return grouped


# print("=============== Franchise vs Standalone ==================")
# print(compare_franchise_vs_standalone())
# print()


def franchise_success():
    franchises = df[df["belongs_to_collection"].notna()]

    results = franchises.groupby("belongs_to_collection").agg({
        "id": "count",
        "budget": ["sum", "mean"],
        "revenue": ["sum", "mean"],
        "vote_average": "mean"
    })

    results.columns = [
        "movie_count",
        "total_budget",
        "mean_budget",
        "total_revenue",
        "mean_revenue",
        "mean_rating"
    ]

    return results.sort_values(by="total_revenue", ascending=False)


# print("=============== Most Successful Movie Franchises ==================")
# print(franchise_success())
# print()


def top_franchise_by_metric(metric):
    data = franchise_success()

    if isinstance(metric, str):
        metric = [metric]

    return data.sort_values(by=metric, ascending=False).head(5)


# print("Total number of movies in franchise")
# print(top_franchise_by_metric('movie_count'))
# print()
# print("Top Franchise by Budget: ")
# print(top_franchise_by_metric(["total_budget", "mean_budget"]))
# print()
# print("Top Franchise by revenue")
# print(top_franchise_by_metric(["total_revenue", "mean_revenue"]))
# print()
# print("Top Franchise by Mean Rating")
# print(top_franchise_by_metric('mean_rating'))
# print()


def explode_directors():
    temp = df.copy()
    temp["director"] = temp["director"].fillna("")
    temp["director"] = temp["director"].str.split("|")
    return temp.explode("director")


def director_success():
    df = explode_directors()
    df = df[df["director"] != ""]

    results = df.groupby("director").agg({
        "id": "count",
        "revenue": "sum",
        "vote_average": "mean"
    })

    results.columns = [
        "movie_count",
        "total_revenue",
        "mean_rating"
    ]

    return results.sort_values(by="total_revenue", ascending=False)


def top_directors_by_metric(metric, top=10):
    data = director_success()
    return data.sort_values(by=metric, ascending=False).head(top)


print('Top Directors by Number of Movies Directed: ',
      top_directors_by_metric('movie_count'))
print('Top Directors by Revenue: ', top_directors_by_metric('total_revenue'))
print('Top Directors by Rating: ', top_directors_by_metric('mean_rating'))
