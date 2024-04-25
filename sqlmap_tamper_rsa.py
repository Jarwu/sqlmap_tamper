#!/usr/bin/env python
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64
from lib.core.enums import PRIORITY

'''
RSA -> base64
'''

__priority__ = PRIORITY.LOW

# input PUBLIC KEY
public_key_str = """-----BEGIN PUBLIC KEY-----
base64
-----END PUBLIC KEY-----"""


def rsa_encrypt_and_base64_encode(data, public_key_str, encoding='utf-8'):
    public_key = serialization.load_pem_public_key(public_key_str.encode(), backend=default_backend())

    ciphertext = public_key.encrypt(
        data.encode(encoding),
        padding.PKCS1v15()
    )

    encoded_data = base64.b64encode(ciphertext).decode(encoding)

    return encoded_data


def dependencies():
    pass


def tamper(payload, **kwargs):
    """
    Custom fields prefix
    """
    
    new_payload="customFields6 = 'xxxx'"+payload
    
    return rsa_encrypt_and_base64_encode(new_payload, public_key_str)
