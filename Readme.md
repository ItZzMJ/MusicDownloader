# Readme

## Installation

Zuerst Docker und Docker-Compose installieren
https://docs.docker.com/docker-for-windows/install/

## Ziel Ordner festlegen
In der docker-compose.yml '<<DEST_DIR>>' mit dem Pfad zum Ausgabeordner ersetzen

## Playlist zum Download festlegen
In /app in soundcloud.py oder spotify.py den Link zur Playlist einfügen

## Playlist downloaden
### Spotify:
docker-compose run --rm app python3 spotify.py

### Soundcloud:
docker-compose run --rm app python3 soundcloud.py
