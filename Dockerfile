FROM python:3.8

RUN apt-get update && apt-get install -y ffmpeg

COPY app /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENV SPOTIPY_CLIENT_ID=f46a4e17d5b94064bfbf4e5ff0a365b1
ENV SPOTIPY_CLIENT_SECRET=b556367d59ab42a7bea5080d36f31ce7
ENV YOUTUBE_DEV_KEY=AIzaSyBZO2Pry7RIKxGEGOX0NMFbnUzcOsJGPXA


