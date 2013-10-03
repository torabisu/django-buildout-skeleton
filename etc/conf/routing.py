import djcelery
djcelery.setup_loader()

BROKER_URL = 'amqp://guest:guest@localhost:5672/'