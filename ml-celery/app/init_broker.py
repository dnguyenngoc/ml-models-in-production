from kombu import Connection
from kombu.exceptions import OperationalError
from settings import config


def is_broker_running(retries: int = 3) -> bool:
    try:
        conn = Connection(config.BROKER)
        conn.ensure_connection(max_retries=retries)
    except OperationalError as e:
        print("Failed to connect to RabbitMQ instance at %s", config.BROKER)
        print(str(e))
        return False
    conn.close()
    return True