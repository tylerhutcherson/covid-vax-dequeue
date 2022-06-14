# Covid Vax Dequeue

This app assumes you have a redis server running with a populated list of "patients" on the key: `patients:covid-vaccine`. If you don't, I have included a `producer.py` script that you can run (set environment variables for your redis connection details).

## Build App
I use docker for containerization/packaging applications. Instead of building from scratch, which you could do, just pull the image I have hosted from my DockerHub repository:

```bash
docker pull tchutch94/covid-vax-dequeue:1.0.0
```

## Run App
Run the container and provide connection params to the Redis server.
```bash
docker run tchutch94/covid-vax-dequeue:1.0.0 \
-e REDIS_HOST='localhost' \
-e REDIS_PORT='12000' \
-e REDIS_PASSWORD='12345678' 
```

## Results
At the end, it will spit out a tracker containing the counts of patients recieved by each serving line like below:

```
{

}
```

Enjoy!