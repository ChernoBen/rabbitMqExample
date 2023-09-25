import pika

# Configurar a conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',
    #credentials=pika.PlainCredentials(username='user',password='password')
    ))  # Substitua 'localhost' pelo endereço do servidor RabbitMQ
channel = connection.channel()

# Declarar a fila da qual você receberá mensagens
queue_name = 'minha_fila'
channel.queue_declare(queue=queue_name)

def callback(ch, method, properties, body):
    # Esta função será chamada quando uma mensagem for recebida
    print(f"Recebi uma mensagem: {body}")

# Configurar a função de retorno de chamada para receber mensagens
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Aguardando mensagens. Pressione Ctrl+C para sair.')

# Iniciar a espera por mensagens
channel.start_consuming()
