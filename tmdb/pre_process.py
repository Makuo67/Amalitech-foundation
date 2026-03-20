from tmdb_api import load_data, DEFAULT_MOVIE_IDS
from typing import Optional
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
load_dotenv()


def load_and_clean(api_key: Optional[str] = None, movie_ids: Optional[list[int]] = None) -> pd.DataFrame:
    """Load data from API and perform initial cleaning."""
    df = load_data(api_key=api_key, movie_ids=movie_ids)

    df = df[df['id'].notna() & (df['id'] != 0)].reset_index(drop=True)
    cols_to_drop = ['adult', 'imdb_id', 'original_title', 'video', 'homepage']
    df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

    df_credits = pd.json_normalize(df["credits"])

    df = df.join(df_credits)
    df = df.drop(columns=["credits"])

    return df


def extract_nested_list(series: pd.Series, key: str = 'name') -> pd.Series:
    """Vectorized extraction of list/dict to pipe-separated strings."""
    def _extract(val):
        if isinstance(val, list):
            return '|'.join(
                item.get(key, '') for item in val if isinstance(item, dict)
            )
        elif isinstance(val, dict):
            return val.get(key, pd.NA)
        return pd.NA

    return series.apply(_extract)


def full_pipeline(api_key: Optional[str] = None, movie_ids: Optional[list[int]] = None, save_path: str = '~/Amalitech-foundation/tmdb/processed_movies.csv') -> pd.DataFrame:
    """Complete processing pipeline: load, clean, extract nested fields."""
    df = load_and_clean(api_key, movie_ids)

    # Extract nested fields
    df['collection_name'] = extract_nested_list(
        df['belongs_to_collection'], 'name')
    df['genres_clean'] = extract_nested_list(df['genres'])
    df['spoken_languages_clean'] = extract_nested_list(
        df['spoken_languages'], 'english_name')
    df['production_countries_clean'] = extract_nested_list(
        df['production_countries'], 'name')
    df['production_companies_clean'] = extract_nested_list(
        df['production_companies'], 'name')

    df['cast_size'] = df['cast'].apply(
        lambda x: len(x) if isinstance(x, list) else 0
    )

    print(df['cast'].apply(type).value_counts())

    df['cast'] = df['cast'].apply(
        lambda x: "|".join([c.get("name", "")
                            for c in x]) if isinstance(x, list) else np.nan
    )

    def get_director(crew_list):
        if isinstance(crew_list, list):
            for member in crew_list:
                if member.get("job") == "Director":
                    return member.get("name")
        return np.nan

    df['director'] = df['crew'].apply(get_director)

    df['crew_size'] = df['crew'].apply(
        lambda x: len(x) if isinstance(x, list) else 0
    )

    json_cols = [
        'belongs_to_collection', 'genres', 'production_countries',
        'production_companies', 'spoken_languages'
    ]

    df = df.drop(columns=json_cols, errors='ignore')

    df = df.fillna({
        "collection_name": "None",
        "genres_clean": "Unknown",
        "spoken_languages_clean": "Unknown",
        "production_countries_clean": "Unknown",
        "production_companies_clean": "Unknown"
    })

    df['budget'] = df['budget'].replace(0, np.nan)
    df['revenue'] = df['revenue'].replace(0, np.nan)

    numeric_cols = ['budget', 'id', 'popularity',
                    'revenue', 'runtime', 'vote_count', 'vote_average', 'cast_size', 'crew_size']

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    df['budget'] = df['budget'].replace(0, np.nan)
    df['revenue'] = df['revenue'].replace(0, np.nan)
    df['runtime'] = df['runtime'].replace(0, np.nan)

    df['budget'] = df['budget'] / 1_000_000
    df['revenue'] = df['revenue'] / 1_000_000

    df.loc[df['vote_count'] == 0, 'vote_average'] = np.nan

    placeholders = ['No Data', 'none', 'None', '',
                    'null', 'Null', 'Undefined', 'undefined']

    df['overview'] = df['overview'].replace(placeholders, np.nan)
    df['tagline'] = df['tagline'].replace(placeholders, np.nan)

    df = df.dropna(subset=['id', 'title'])
    df = df[df.count(axis=1) >= 10]

    df = df[df['status'] == 'Released']
    df = df.drop(columns=['status'], errors='ignore')

    # Map cleaned columns
    df_final = df.rename(columns={
        'genres_clean': 'genres',
        'collection_name': 'belongs_to_collection',
        'production_companies_clean': 'production_companies',
        'production_countries_clean': 'production_countries',
        'spoken_languages_clean': 'spoken_languages'
    })

    final_columns = [
        'id', 'title', 'tagline', 'release_date',
        'genres', 'belongs_to_collection', 'original_language',
        'budget', 'revenue',
        'production_companies', 'production_countries',
        'vote_count', 'vote_average', 'popularity', 'runtime',
        'overview', 'spoken_languages', 'poster_path',
        'cast', 'cast_size', 'director', 'crew_size'
    ]

    df_final = df_final[[
        col for col in final_columns if col in df_final.columns]]
    df_final = df_final.reset_index(drop=True)

    # Saving file to csv
    df_final.to_csv(save_path, index=False)
    print(f"Processed data saved to {save_path}")
    print("Columns:", df_final.columns.tolist())


if __name__ == "__main__":
    print(full_pipeline())
