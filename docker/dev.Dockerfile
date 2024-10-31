# base image
FROM python:3.13.0

# Define the author
LABEL author="https://github.com/Maengdok" \
      maintainer="Maengdok" \
      version="0.0.0"

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Switch to app directory so that everything runs from here
WORKDIR /usr/src
RUN mkdir /usr/src/staticfiles

# Install system dependencies
RUN apt-get update
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev postgresql-client

# install dependencies
RUN pip install --upgrade pip

# Copy the required packages for the user
COPY ./requirements.txt .

# Let pip install required packages
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN sed -i 's/\r$//g' /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Copy the app code to image working directory for the user
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]