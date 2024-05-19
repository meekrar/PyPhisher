# Dockerfile

# Author       : meekrar
# Github       : https://github.com/meekrar
# Messenger    : https://m.me/meekrar
# Email        : hackermeekrar@gmail.com
# Date         : 19-05-2024
# Main Language: Python

# Download and import main images

# Operating system
FROM debian:latest
# Main package
FROM python:3

# Author info
LABEL MAINTAINER="https://github.com/meekrar/PyPhisher"

# Working directory
WORKDIR PyPhisher/
# Add files 
ADD . /PyPhisher

# Installing other packages
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install php openssh-client -y
RUN pip3 install -r files/requirements.txt
RUN apt-get clean

# Main command
CMD ["python3", "pyphisher.py", "--noupdate"]

## Wanna run it own? Try following commnads:

## "sudo docker build . -t meekrar/pyphisher:latest", "sudo docker run --rm -it meekrar/pyphisher:latest"

## "sudo docker pull meekrar/pyphisher", "sudo docker run --rm -it meekrar/pyphisher"
