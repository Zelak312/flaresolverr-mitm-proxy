#!/bin/sh

if [ "$1" = "up" ]; then
    docker compose -f docker-compose.dev.yml up -d
elif [ "$1" = "down" ]; then
    docker compose -f docker-compose.dev.yml down
elif [ "$1" = "build" ]; then
    docker compose -f docker-compose.dev.yml build
elif [ "$1" = "restart" ]; then
    docker compose -f docker-compose.dev.yml down --remove-orphans
    docker compose -f docker-compose.dev.yml up -d
elif [ "$1" = "log" ]; then
    docker compose -f docker-compose.dev.yml logs -f
else
    echo "Argument is neither up nor down"
fi