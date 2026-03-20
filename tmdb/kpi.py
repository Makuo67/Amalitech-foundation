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


def profit(revenue, budget):
    if revenue is None or budget is None:
        return None

    return revenue - budget


def roi(revenue, budget):
    if revenue is None or budget is None or budget == 0:
        return None

    return revenue / budget


def rank_movies(df, column, ascending=False, limit=5, filter_condition=None):
    temp = df.copy()

    if filter_condition is not None:
        temp = temp[filter_condition(temp)]
    return temp.sort_values(by=column, ascending=ascending).head(limit)


# ===========================================================
df = load_csv(filepath)


def highest_revenue(df, top=10):
    return rank_movies(df, column="revenue", ascending=False, limit=top)


def highest_budget(df, top=5):
    return rank_movies(df, column="budget", ascending=False, limit=top)


def highest_profit(df, top=5):
    df["profit"] = df["revenue"] - df["budget"]
    return rank_movies(df, "profit", ascending=False, limit=top)


def lowest_profit(df, top=5):
    df["profit"] = df["revenue"] - df["budget"]
    return rank_movies(df, "profit", ascending=True, limit=top)


def highest_roi(df, top=10):
    df["roi"] = df["revenue"] / df["budget"]
    return rank_movies(
        df,
        column="roi",
        ascending=False,
        limit=top,
        filter_condition=lambda d: d["budget"] >= 10
    )


def lowest_roi(df, top=10):
    df["roi"] = df["revenue"] / df["budget"]
    return rank_movies(
        df,
        column="roi",
        ascending=True,
        limit=top,
        filter_condition=lambda d: d["budget"] >= 10
    )


def most_voted(df, top=5):
    return rank_movies(df, column="vote_count", ascending=False, limit=top)


def highest_rated(df, top=5):
    return rank_movies(
        df,
        column="vote_average",
        ascending=False,
        limit=top,
        filter_condition=lambda d: d["vote_count"] >= 10
    )


def lowest_rated(df, top=5):
    return rank_movies(
        df,
        column="vote_average",
        ascending=True,
        limit=top,
        filter_condition=lambda d: d["vote_count"] >= 10
    )


def most_popular(df, top=5):
    return rank_movies(df, column="popularity", ascending=False, limit=top)


if __name__ == "__main__":
    print("================ Highest by Budget ==================================")
    print(highest_budget(df))
    print("================ Highest by Revenue ================================")
    print(highest_revenue(df))
    print("================ Highest by Profit =================================")
    print(highest_profit(df))
    print("================ Lowest by Profit =================================")
    print(lowest_profit(df))
    print("================ Highest by ROI =================================")
    print(highest_roi(df))
    print("================ Lowest by ROI =================================")
    print(lowest_roi(df))
    print("================ Most Voted =================================")
    print(most_voted(df))
    print("================ Highest Rated =================================")
    print(highest_rated(df))
    print("================ Lowest Rated =================================")
    print(lowest_rated(df))
    print("================ Most popular =================================")
    print(most_popular(df))
