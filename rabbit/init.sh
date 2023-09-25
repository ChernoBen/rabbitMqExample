#!/bin/bash
docker build -t rabbitmq-custom:1.0 .
docker run -d --name meu-rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq-custom:1.0
