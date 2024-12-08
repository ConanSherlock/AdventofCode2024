# Use the official Nginx image as the base
FROM nginx:1.27.3

COPY requirements.txt .

# Install basic utilities: Python 3.x, CMake, GCC, and additional useful tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
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
    build-essential \
    unzip \
    wget \
    zip \
    bash-completion \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /venv
RUN chmod 755 /venv/bin/activate
RUN /venv/bin/pip install --upgrade pip
RUN /venv/bin/pip install -r requirements.txt

RUN adduser --disabled-password --gecos '' base_user
USER base_user

WORKDIR /usr/src/app

CMD ["./start-venv.sh"]
