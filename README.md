# Muezzin Project

Over the past few years, Israeli security forces have faced complex challenges in various arenas of operation. Recently, we have witnessed the development of a new threat, characterized by the use of digital platforms, primarily podcasts, to spread incitement against Israel and its institutions around the world.

For this purpose, we have developed a project that will help detect dangerous content and provide advance warning.


## There is a new version with a new folder arrangement in Brunch utils



## services & flow

- `Preprocessor` - Reads the information and passes it on to Kafka
- `DataLoader`  - Receives information from Kafka and publishes it to Elastic and the file to Mongo
- `Transcriber` - Receives information from Kafka who is ready for transcription pulls from Mongo and publishes the elastic text
- `Classified` - Receives from Kafka who is ready for classification, classifies and publishes back to Elastic
- `DataRetrieval` - Publishes an API service that allows you to find information about the data


### 🔹to start

open cmd in path MuezzinProject/scriptes and run bilud-posh.bat .
open cmd in path MuezzinProject/infra/Docker and run docker compose up .



### Prerequisites
- `Docker installed on the computer including connection to the master Docker`
- `CLI tool for mode shift called OC`




### Information regarding decision-making is in the attached file (for Hebrew speakers..) 


`
