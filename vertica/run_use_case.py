from research.vertica.run_tests.check_score import run as run_score
from research.vertica.run_tests.check_bookmarks import run as run_bookmarks
from research.vertica.run_tests.check_film_likes_by_user import run as run_likes_by_user
from research.vertica.run_tests.check_user_likes_by_film import run as run_likes_by_film


if __name__ == "__main__":
    run_score()
    run_bookmarks()
    run_likes_by_user()
    run_likes_by_film()
