# Covid Vax Dequeue

This app assumes you have a legit redis server running with a populated list of "patients" on the key: `patients:covid-vaccine`.

## Build App
I use docker for containerization/packaging applications so they are runnable form any host machine, typically. Instead of building from scratch, which you could do, just pull the image I created and now host from my DockerHub repository:

```bash
docker pull tchutch94/covid-vax-dequeue:1.0.0
```

## Run App
Assuming that works.. you can now run the app with Docker, and provide connection params to the Redis server.
```bash
docker run tchutch94/covid-vax-dequeue:1.0.0 \
-e REDIS_HOST='' \
-e REDIS_PORT='' \
-e REDIS_PASSWORD='' 
```

## Results
At the end, it will spit out a tracker containing the counts of patients recieved by each serving line like below:

```
{

}
```

Enjoy!