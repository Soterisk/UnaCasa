import uuid


def generate_unique_username(self):
    return str(uuid.uuid4())[:30]