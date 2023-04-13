
import logging

from research.vertica.db_utils.db_factory import insert_butches as run_single


logging.basicConfig(level=logging.INFO)
logging.root.name = 'RESEARCH'


if __name__ == "__main__":
    run_single()
