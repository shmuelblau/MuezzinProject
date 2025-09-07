docker build -t shmuelblau/preprocessor:1 ../services/preprocessor
docker push shmuelblau/preprocessor:1

docker build -t shmuelblau/dataloader:1 ../services/DataLoader
docker push shmuelblau/dataloader:1
