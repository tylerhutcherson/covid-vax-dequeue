VERSION_TAG=$(<VERSION)
docker build -t tchutch94/covid-vax-dequeue:$VERSION_TAG .