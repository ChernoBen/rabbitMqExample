import pika

# Configurar a conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # Substitua 'localhost' pelo endereço do servidor RabbitMQ
channel = connection.channel()

# Criar ou garantir que a fila exista
queue_name = 'minha_fila'
channel.queue_declare(queue=queue_name)

# Publicar uma mensagem na fila
message_body = 'Olá, RabbitMQ! Aqui é o Benja!!!'
channel.basic_publish(exchange='', routing_key=queue_name, body=message_body)

print(f'Mensagem publicada: {message_body}')

# Fechar a conexão
connection.close()