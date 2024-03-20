import base64

FIRST_INVISIBLE_CHAR = 917760

def encode(s):
    """Encodes an input string to a hidden one"""
    encoded = []
    for char in s:
        if ord(char) > 127:
            raise Exception(f"Non ascii character {char}. Maybe base64 encode your string first")
        encoded.append(chr(ord(char) + FIRST_INVISIBLE_CHAR))
    return ''.join(encoded)

def decode(s):
    """Decodes any of our 'special' characters to ascii"""
    plain = []
    for char in s:
        try:
            plain.append(chr(ord(char) - FIRST_INVISIBLE_CHAR))
        except:
            pass
    return ''.join(plain)

def add(m, s):
    """Adds a message to a string"""
    b64 = base64.b64encode(m.encode("utf8")).decode("utf8")
    hidden = encode(b64)
    return s + hidden

def get(s):
    """Gets a message from a string"""
    hidden = decode(s)
    decoded = base64.b64decode(hidden).decode("utf8")
    return decoded






