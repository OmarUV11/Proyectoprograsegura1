#!/usr/bin/env bash

[[ -f "$1" ]] || { echo "Se esperaba un archivo con variables de entorno"; exit 1; }


for linea in $(ccdecrypt -c "$1"); do
    echo "$linea"
    export "$linea"
done

docker-compose up -d 


