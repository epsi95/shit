from hashlib import sha256


def create_hash(binary_data):
    return sha256(binary_data).hexdigest()
