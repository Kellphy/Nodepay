FROM debian:11-slim

# Set environment variables
ENV EXTENSION_ID=lgmpfmgeabnnlemejacfljbmonaomfmm
ENV EXTENSION_URL='https://app.nodepay.ai/'
ENV GIT_USERNAME=sryze
ENV GIT_REPO=crx-dl

# Install necessary packages then clean up to reduce image size
RUN set -e; \
    apt update && \
    apt upgrade -y && \
    apt install -qqy \
    curl \
    wget \
    git \
    chromium \
    chromium-driver \
    python3 \
    python3-pip \
    python3-requests \
    python3-selenium \
    coreutils \
    bash && \
    apt autoremove --purge -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install distro

# Copy the Python script
COPY main.py .

# Run the Python script
ENTRYPOINT [ "python3", "main.py" ]