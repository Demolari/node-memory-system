import uuid
from datetime import datetime
import os

LOG_PATH = "tools/uuid_log.txt"

def generate_uuid():
    """Generuje pełny UUIDv7."""
    return uuid.uuid7()

def get_short_uuid(uuid_obj, length=8):
    """Zwraca skróconą wersję UUID do np. wyświetlania w UI."""
    return str(uuid_obj).replace("-", "")[:length]

def log_uuid(uuid_obj, extra_note=""):
    """Zapisuje UUID do logu z datą i opcjonalną notatką."""
    timestamp = datetime.now().isoformat()
    entry = f"{timestamp} | {uuid_obj} | {extra_note}\n"

    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as log_file:
        log_file.write(entry)

def log_id_event(node_id, message):
    """Wrapper dla log_uuid do logowania eventów węzłów."""
    log_uuid(node_id, message)

# Przykład użycia:
if __name__ == "__main__":
    new_uuid = generate_uuid()
    short_uuid = get_short_uuid(new_uuid)
    log_uuid(new_uuid, extra_note="Generated for new node")
    print(f"Full UUID: {new_uuid}")
    print(f"Short UUID: {short_uuid}")
