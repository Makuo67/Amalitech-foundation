import os
import requests
import pandas as pd
from typing import List, Optional, Dict, Any


DEFAULT_MOVIE_IDS: List[int] = [299534, 19995, 140607, 299536, 597, 135397, 420818, 24428,
                                168259, 99861, 284054, 12445, 181808, 330457, 351286, 109445, 321612, 260513]
API_KEY: Optional[str] = os.getenv('TMDB_API_KEY')
BASE_URL = 'https://api.themoviedb.org/3/movie/'


def get_movie(movie_id: int, api_key: str) -> Optional[Dict[str, Any]]:
    """Fetch movie details from TMDB API."""
    if not api_key:
        raise ValueError("TMDB_API_KEY environment variable is required.")
    url = f"{BASE_URL}{movie_id}?api_key={api_key}&append_to_response=credits"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def load_data(movie_ids: Optional[List[int]] = None, api_key: Optional[str] = None) -> pd.DataFrame:
    """Load movie data from TMDB API into DataFrame."""
    if movie_ids is None:
        movie_ids = DEFAULT_MOVIE_IDS
    if api_key is None:
        api_key = os.getenv("TMDB_API_KEY")

    if not api_key:
        raise ValueError("TMDB_API_KEY environment variable must be set.")

    movies_data = []
    for movie_id in movie_ids:
        try:
            data = get_movie(movie_id, api_key)
            if data:  # Skip None
                movies_data.append(data)
        except requests.RequestException:
            print(f"Failed to fetch movie {movie_id}")
            continue

    return pd.DataFrame(movies_data)
