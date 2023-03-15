# get OS linux-alpine, install python3.9 and install pip
FROM python:3.9-alpine
#FROM python:3.9-buster

# add environment in container
ENV DB_URL="sqlite:///basic_db.sqlite3"

# create folder app, and move it
WORKDIR /app

# copy from to-> execute command in terminal for install requirements
COPY requirements.txt requirements.txt

# execute command in terminal
RUN pip install -r requirements.txt

# copy all files from my repository to folder app in docker-container
# except for the files and fodlers listed in .dockerignore
COPY . .

# execute command for run uvicorn
CMD uvicorn main:app --host 0.0.0.0 --port 8000


# docker build . -t python-6-fastapi-basic
# docker run -p 80:8000 --v /basic_db: /basic_db  -d python-6-fastapi-basic
#
#docker run -d --mount type=bind,source="$(pwd)"/datavolume, target=/app python-6-fastapi-basic
#
#docker run --mount src=/,target=/datavolume,type=bind -p 80:8000 -d python-6-fastapi-basic
#docker run -p 80:8000 -v /app: "$(pwd)"/datavolume -d python-6-fastapi-basic
