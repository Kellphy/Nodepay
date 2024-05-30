Use built image:
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

Or, build it yourself:
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
