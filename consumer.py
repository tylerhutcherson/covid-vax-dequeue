import os
import random
import redis
import time
import threading

from collections import defaultdict


LINES = 6
MAX_WAIT_TIME = 3
MIN_WAIT_TIME = 0
PATIENT_QUEUE = 'patients:covid-vaccine'
TRACKER = defaultdict(int)

# Create a Redis connection pool
pool = redis.ConnectionPool(
    host = os.environ['REDIS_HOST'],
    port = os.environ['REDIS_PORT'],
    password = os.environ['REDIS_PASSWORD']
)

class Consumer(threading.Thread):
    """
    Basic queue consumer class to read from a Redis List
    and process items simultaneously.
    """
    def __init__(self, i: int, pool: redis.ConnectionPool):
        self.name = f'vax_line_{i}'
        self.redis_client = pool.get_connection()

    def run(self):
        while True:
            patient = self.redis_client.rpop(PATIENT_QUEUE)
            if patient:
                # process patient - inject some randomness for fun
                time.sleep(random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME))
                # update tracker
                TRACKER[self.name] += 1
            else:
                break


if __name__ == "__main__":
    # Start threads
    for i in range(LINES):
        consumer = Consumer(i+1, pool)
        consumer.start()

    # Check for completion
    r = pool.get_connection()
    while r.exists(PATIENT_QUEUE):
        print('Processing patients', flush=True)
        time.sleep(1)

    print('Cavid Vax Patient line empty!', flush=True)
    print(TRACKER, flush=True)
    