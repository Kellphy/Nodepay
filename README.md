## [Contact Me](https://kellphy.com/socials) 
### But before, check the status of [Nodepay](https://app.nodepay.ai/dashboard)
## Usage
### Use built image from [Docker Hub](https://hub.docker.com/r/kellphy/nodepay)
#### Docker Compose
```
services:
  nodepay:
    container_name: Nodepay
    image: kellphy/nodepay
    restart: unless-stopped
    environment:
      - NP_USER=YOUR@EMAIL.COM
      - NP_PASS=YOURPASSWORD
```
#### Docker Run
```
docker run -d \
  --name Nodepay \
  --restart unless-stopped \
  -e NP_USER="YOUR@EMAIL.COM" \
  -e NP_PASS="YOURPASSWORD" \
  kellphy/nodepay
```
### Build it yourself from [GitHub](https://github.com/Kellphy/Nodepay) 
#### Docker Compose
```
services:
  nodepay:
    container_name: Nodepay
    image: nodepay
    restart: unless-stopped
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - NP_USER=YOUR@EMAIL.COM
      - NP_PASS=YOURPASSWORD
```
#### Docker Run
```
docker build -t nodepay . && \
docker run -d \
  --name Nodepay \
  --restart unless-stopped \
  -e NP_USER="YOUR@EMAIL.COM" \
  -e NP_PASS="YOURPASSWORD" \
  nodepay
```
## I have never did this before steps:
1. [Download Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Open CMD and use the Docker Run command of the built image from Docker Hub
3. Check and Manage at Docker Desktop > Containers
