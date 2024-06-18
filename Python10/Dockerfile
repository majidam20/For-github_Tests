FROM postgres:12

# Install Python and Daff (https://github.com/paulfitz/daff)
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip
RUN pip3 install daff==1.3.46

# Copy project files
COPY . /app
WORKDIR /app
ENV PATH=$PATH:/app/bin

