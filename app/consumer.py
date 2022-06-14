import random
import time
import threading

from utils import (
    get_redis,
    PATIENT_QUEUE
)
from collections import defaultdict
from pprint import pprint


LINES = 6
MAX_WAIT_TIME = 3
MIN_WAIT_TIME = 0
TRACKER = defaultdict(int)

class Consumer(threading.Thread):
    """
    Basic queue consumer class to read from a Redis List
    and process items simultaneously.
    """
    def __init__(self, i: int):
        super(Consumer, self).__init__()
        self.name = f'vax_line_{i}'
        self.redis_client = get_redis()
        print("Covid", self.name, "open for serving...", flush=True)

    def run(self):
        while True:
            # Grab the next available patient from the line
            patient = self.redis_client.rpop(PATIENT_QUEUE)
            if patient:
                # Process patient - inject some wait time randomness for fun
                time.sleep(random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME))
                # Update tracker
                TRACKER[self.name] += 1
            else:
                break


if __name__ == "__main__":
    print("Covid vax clinic open!", flush=True)

    # Start consumer threads
    for i in range(LINES):
        consumer = Consumer(i+1)
        consumer.start()

    # Check for completion
    r = get_redis()
    while r.exists(PATIENT_QUEUE):
        print("Processing patients...", r.llen(PATIENT_QUEUE), "remaining...", flush=True)
        time.sleep(1)

    print("Cavid vax patient line empty!\n", flush=True)
    pprint(dict(TRACKER), flush=True)
    