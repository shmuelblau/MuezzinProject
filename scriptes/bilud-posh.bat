docker build -t shmuelblau/preprocessor:1 ../services/Preprocessor
docker push shmuelblau/preprocessor:1

docker build -t shmuelblau/dataloader:1 ../services/DataLoader
docker push shmuelblau/dataloader:1

docker build -t shmuelblau/transcriber:1 ../services/Transcriber
docker push shmuelblau/transcriber:1

docker build -t shmuelblau/classified:1 ../services/Classified
docker push shmuelblau/classified:1