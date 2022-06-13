# Covid Vax Dequeue

This app assumes you have a legit redis server running with a populated list of "patients" on the key: `patients:covid-vaccine`.

## Build App
I use docker for containerization/packaging applications so they are runnable form any host machine, typically.

```bash
git clone 
cd covid-vax-dequeue/
docker build .... 
```

## Run App
```bash
docker run ....
```

# Results
At the end of the program, it will spit out a tracker containing the counts of patients recieved by each serving line like below:

```
{
    
}
```