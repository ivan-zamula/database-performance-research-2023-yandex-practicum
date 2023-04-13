
import logging

from check_score import run as run_score
from check_bookmarks_count import run as run_bookmarks
from check_film_likes_by_user import run as run_likes_by_user
from check_user_likes_by_film import run as run_likes_by_film


# logging.basicConfig(level=logging.INFO)
# logging.root.name = 'RESEARCH'


if __name__ == "__main__":
    run_score()
    run_bookmarks()
    run_likes_by_user()
    run_likes_by_film()
