import hashlib

import base62


def generate_code(url: str, *, size: int) -> str:
    md5 = hashlib.md5(url.encode()).digest()
    base62_encoded = base62.encodebytes(md5)
    return base62_encoded[:size]
