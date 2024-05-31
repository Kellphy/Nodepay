Contact: https://kellphy.com/socials
---
## Docker Run
```
docker run -d \
  --name Nodepay \
  --restart unless-stopped \
  -e NP_USER=YOUR@EMAIL.COM \
  -e NP_PASS=YOURPASSWORD \
  kellphy/nodepay
```
## Docker Compose
Use built image from Docker Hub: https://hub.docker.com/r/kellphy/nodepay
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

Or, build it yourself from GitHub: https://github.com/Kellphy/Nodepay
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
