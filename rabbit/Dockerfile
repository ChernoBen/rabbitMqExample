FROM rabbitmq:latest

# Exponha as portas padrão usadas pelo RabbitMQ
EXPOSE 5672 15672

# Defina as variáveis de ambiente para o RabbitMQ (se necessário)
# ENV RABBITMQ_USER=user
# ENV RABBITMQ_PASSWORD=password

# Você pode configurar o RabbitMQ adicionando configurações personalizadas aqui
# COPY rabbitmq.config /etc/rabbitmq/

# Execute o RabbitMQ Server quando o contêiner for iniciado
CMD ["rabbitmq-server"]