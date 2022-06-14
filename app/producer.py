import json

from utils import (
    get_redis,
    PATIENT_QUEUE
)


NUM_PATIENTS = 200

if __name__ == "__main__":
    print('Adding patients to the vax line', flush=True)

    # Setup redis connection
    r = get_redis()
    
    # Add patients to the queue
    for i in range(NUM_PATIENTS):
        r.lpush(PATIENT_QUEUE, json.dumps({'patient_id': i}))
    
    print("Line is now full and contains", r.llen(PATIENT_QUEUE), "patients...", flush=True)
    