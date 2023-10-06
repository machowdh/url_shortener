import hashlib
import base58
import uuid



async def generate_unique_short_url() -> str:
    uuid_value = uuid.uuid4()

    uuid_bytes = uuid_value.bytes

    uuid_int = int.from_bytes(uuid_bytes, byteorder='big')

    uuid_int = uuid_int | (1 << 35)

    return base58.b58encode_int(uuid_int)

