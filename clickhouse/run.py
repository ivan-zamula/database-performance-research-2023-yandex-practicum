
import logging

from check_insert_n_select_time import run as run_single
from check_insert_n_select_time_batches import run as run_batches


logging.basicConfig(level=logging.INFO)
logging.root.name = 'RESEARCH'


if __name__ == "__main__":
    run_single()
    run_batches()
