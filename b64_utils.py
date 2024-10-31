# b64_utils.py
# v0.1.0

import base64
def encode(string):
    return base64.b64encode(string.encode()).decode()
def decode(bytes):
    return base64.b64decode(bytes).decode()

if __name__ == '__main__':
    string = 'The quick brown fox jumps over the lazy dog'
    encoded = encode(string)
    print('Encoded: ' + encoded)
    print('Decoded: ' + decode(encoded))
