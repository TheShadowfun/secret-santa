import random
import string
import uuid

MAX_NAME_LENGTH = 16
SHIFT = 4
VALID_CHARS = string.ascii_letters + string.digits

def simple_encrypt(text):
    text_len = chr(len(text) + SHIFT)
    padding_length = MAX_NAME_LENGTH - len(text)
    random_padding = ''.join(random.choice(VALID_CHARS) for _ in range(padding_length))
    padded = text + random_padding
    return text_len + ''.join(chr((ord(char) + SHIFT) % 128) for char in padded)

def simple_decrypt(text):
    original_len = ord(text[0]) - SHIFT
    decrypted = ''.join(chr((ord(char) - SHIFT) % 128) for char in text[1:])
    return decrypted[:original_len]

def gen_short_uuid():
    return str(uuid.uuid4())[:13]