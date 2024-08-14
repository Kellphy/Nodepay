FROM debian:11-slim

# Set environment variables
ENV EXTENSION_ID=lgmpfmgeabnnlemejacfljbmonaomfmm
ENV EXTENSION_URL='https://app.nodepay.ai/'
ENV GIT_USERNAME=warren-bank
ENV GIT_REPO=chrome-extension-downloader

# Install necessary packages then clean up to reduce image size
RUN apt update && \
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

# Download crx downloader from git
RUN git clone "https://github.com/${GIT_USERNAME}/${GIT_REPO}.git" && \
    chmod +x ./${GIT_REPO}/bin/*

# Download the extension selected
RUN ./${GIT_REPO}/bin/crxdl $EXTENSION_ID

# Install Python packages
RUN pip3 install distro

# Copy the Python script
COPY main.py .

# Run the Python script
ENTRYPOINT [ "python3", "main.py" ]