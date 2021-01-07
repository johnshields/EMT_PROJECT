# Python Version - 3.8 Tested and works with Tensorflow
FROM python:3.8

# project File Location within the container
WORKDIR /usr/src/app

# copy project requirments
COPY requirements.txt ./

# build env from requirments.txt
RUN pip install --no-cache-dir -r requirements.txt

# Port Blinding
EXPOSE 5000

# copy project src into container
COPY . /usr/src/app

# Set Flask Env vars
ENV FLASK_APP=web_service.py
ENV FLASK_ENV production
ENV FLASK_RUN_HOST 0.0.0.0

# Commands
CMD ["flask", "run"]
