import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Global style
plt.style.use("seaborn-v0_8")
sns.set_palette("viridis")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 13


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


# Convert date column to datetime
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

# Calculate ROI, avoid zeros
df["roi"] = df.apply(
    lambda r: (r["revenue"] / r["budget"]
               ) if r["budget"] and r["budget"] != 0 else pd.NA,
    axis=1
)

# Identify franchise vs standalone
df["movie_type"] = df["belongs_to_collection"].apply(
    lambda x: "Franchise" if pd.notna(x) else "Standalone"
)


# Helper Function for Plotting
def finalize_plot(title, xlabel="", ylabel="", save_path=None):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.savefig("my_plot.png")


# Revenue vs Budget
def plot_revenue_vs_budget():
    plt.scatter(df["budget"], df["revenue"], alpha=0.7)
    finalize_plot(
        "Revenue vs Budget Trend",
        xlabel="Budget ($)",
        ylabel="Revenue ($)"
    )


# ROI Distribution by Genre

# First, we explode genre
def explode_genres():
    df_copy = df.copy()
    df_copy["genres"] = df_copy["genres"].str.split("|")
    return df_copy.explode("genres")


def plot_roi_by_genre():
    genre_df = explode_genres()

    sns.boxplot(data=genre_df, x="genres", y="roi")
    plt.xticks(rotation=45, ha="right")

    finalize_plot(
        "ROI Distribution by Genre",
        xlabel="Genre",
        ylabel="ROI"
    )


# Popularity vs Rating

def plot_popularity_vs_rating():
    sns.regplot(
        data=df,
        x="vote_average",
        y="popularity",
        scatter_kws={"alpha": 0.6}
    )
    finalize_plot(
        "Popularity vs Rating",
        xlabel="Rating",
        ylabel="Popularity"
    )


# Yearly Box Office Trends
def plot_yearly_box_office():
    df["year"] = df["release_date"].dt.year

    yearly = df.groupby("year")["revenue"].mean()

    yearly.plot(kind="line", marker="o")

    finalize_plot(
        "Yearly Average Box Office Revenue",
        xlabel="Year",
        ylabel="Mean Revenue ($)"
    )


# Frnachise Vs Standalone
def plot_franchise_vs_standalone():
    compare = df.groupby("movie_type").agg({
        "revenue": "mean",
        "roi": "mean",
        "popularity": "mean",
        "vote_average": "mean"
    })

    compare.plot(kind="bar")

    finalize_plot(
        "Franchise vs Standalone Performance",
        xlabel="Movie Type",
        ylabel="Mean Metric Value"
    )
