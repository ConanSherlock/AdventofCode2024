# Use the official Nginx image as the base
FROM nginx:1.27.3

# Install basic utilities: Python 3.x, CMake, GCC, and additional useful tools
RUN apk update && \
    apk add --no-cache \
    python3 \
    python3-dev \
    python3-venv \
    cmake \
    gcc \
    g++ \
    make \
    curl \
    git \
    vim \
    bash \
    build-base \
    unzip \
    wget \
    zip \
    bash-completion \
    iputils \
    && rm -rf /var/cache/apk/*

# Set the working directory inside the container
WORKDIR /usr/src/app
