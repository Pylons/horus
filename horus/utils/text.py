import hashlib
import random
import string
from pyramid.compat import text_type


def generate_random_string(length=12):
    """Generate a generic hash key for the user to use."""
    m = hashlib.sha256()
    word = ''
    for i in range(length):
        word += random.choice(string.ascii_letters)
    m.update(word.encode('ascii'))
    return text_type(m.hexdigest()[:length])
