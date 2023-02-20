# get OS linux-alpine, install python3.9 and install pip
# FROM python:3.9-alpine
FROM python:3.9-buster

# create folder app, and move it
WORKDIR /app

# copy from to-> execute command in terminal for install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy all files from my repository to folder app in docker-container
COPY . .

# execute command for run uvicorn
CMD uvicorn main:app --host 0.0.0.0 --port 80
#CMD python -m uvicorn main:app --host 0.0.0.0 --port 80
