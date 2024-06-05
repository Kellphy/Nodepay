# [Contact Me](https://kellphy.com/socials) 
### But before, check the status of [Nodepay](https://app.nodepay.ai/dashboard)
#### Also, [check out other passive income tools](https://kellphy.com/proxynode) that run with Docker, such as Grass, HoneyGain, Mysterium, and many others!
# Setup:
1. [Download Docker Desktop](https://www.docker.com/products/docker-desktop).
2. Login to [Nodepay](https://app.nodepay.ai/dashboard).
3. Open `Developer Tools` and go to `Application(Chrome)` / `Storage(Firefox)`.
4. Go to `Local Storage` > `https://app.nodepay.ai` and copy the value of `np_webapp_token` OR `np_token` (The big array of random numbers and letters).
5. Replace `NP_COOKIE` with the value that you copied.
6. Open CMD and use the Docker Run command of the built image from Docker Hub.
7. Check and Manage the app from Docker Desktop > Containers.
# Usage Options
## A) Use built image from [Docker Hub](https://hub.docker.com/r/kellphy/nodepay)
#### Docker Compose
```
services:
  nodepay:
    container_name: Nodepay
    image: kellphy/nodepay
    restart: unless-stopped
    environment:
      - NP_COOKIE=YOURCOOKIE
```
#### Docker Run
```
docker run -d \
  --name Nodepay \
  --restart unless-stopped \
  -e NP_COOKIE="YOURCOOKIE" \
  kellphy/nodepay
```
## B) Build it yourself from [GitHub](https://github.com/Kellphy/Nodepay) 
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
      - NP_COOKIE=YOURCOOKIE
```
#### Docker Run
```
docker build -t nodepay . && \
docker run -d \
  --name Nodepay \
  --restart unless-stopped \
  -e NP_COOKIE="YOURCOOKIE" \
  nodepay
```
