import os
import redis


# Redis list key
PATIENT_QUEUE = 'patients:covid-vaccine'

# Create a Redis connection pool
pool = redis.ConnectionPool(
    host = os.environ['REDIS_HOST'],
    port = os.environ['REDIS_PORT'],
    password = os.environ['REDIS_PASSWORD']
)

# Fetch a redis connection from the pool
def get_redis():
    return redis.Redis(connection_pool=pool)
