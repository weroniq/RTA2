# From the source image
FROM python:3.9-slim
COPY --from=openjdk:8-jre-slim /usr/local/openjdk-8 /usr/local/openjdk-8

ENV JAVA_HOME="/usr/local/openjdk-8"

RUN update-alternatives --install /usr/bin/java java /usr/local/openjdk-8/bin/java 1

# Identify maintainer
LABEL maintainer = "wb72698@student.sgh.waw.pl"

# Set the default working directory
WORKDIR /app/

# Copy requirements.txt outside the container
# to /app/ inside the container
COPY requirements.txt /app/

# Install required packages
RUN pip install -r ./requirements.txt

# Copy app.py and__init__.py outside the container
# to /app/ inside the container
COPY socket_pyspark_receiver.py __init__.py  /app/

# When the container starts, run this
ENTRYPOINT python ./socket_pyspark_receiver.py