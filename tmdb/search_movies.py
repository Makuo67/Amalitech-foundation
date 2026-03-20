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


def search_genre(genre, cast):
    return df[
        df["genres"].str.contains(genre) &
        df["genres"].str.contains("Action") &
        df["cast"].str.contains(cast)
    ].sort_values(by="vote_average", ascending=False)


def search_cast_and_director(cast, director):
    return df[
        df["cast"].str.contains(cast) &
        df["director"].str.contains(director)
    ].sort_values(by="runtime", ascending=True)


if __name__ == "__main__":
    print("Best-rated Science Fiction Action Movie: ",
          search_genre("Science Fiction", "Bruce Willis"))
    print()
    print("Movies starring Uma Thurman & directed by Quentin Tarantino: ",
          search_cast_and_director("Uma Thurman", "Quentin Tarantino"))
