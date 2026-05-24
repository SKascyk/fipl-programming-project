def get_bytes(text, key):
    text_bytes = list(text.encode('utf-8'))
    key_bytes = list(key.encode('utf-8'))
    return text_bytes, key_bytes

def extend_key(key_bytes, length):
    key_len = len(key_bytes)
    if length <= key_len:
        return key_bytes[:length]
    extended = key_bytes * (length // key_len)
    extended.extend(key_bytes[:length % key_len])
    return extended

def get_permutation_order(extended_key, length):
    pairs = [(extended_key[i], i) for i in range(length)]
    pairs.sort()
    return [idx for _, idx in pairs]

def permute_bytes(text_bytes, extended_key, length):
    order = get_permutation_order(extended_key, length)
    return [text_bytes[order[i]] for i in range(length)]

def ksa(key):
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s

def prga(s, length):
    i = j = 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        t = (s[i] + s[j]) % 256
        keystream.append(s[t])
    return keystream

# Main Function

def encrypt(plain_text, key):
    text_bytes, key_bytes = get_bytes(plain_text, key)
    length = len(text_bytes)

    extended_key = extend_key(key_bytes, length)
    permuted_bytes = permute_bytes(text_bytes, extended_key, length)
    s = ksa(key_bytes)
    gamma = prga(s, length)

    encrypted_bytes = [p ^ g for p, g in zip(permuted_bytes, gamma)]
    return bytes(encrypted_bytes).hex()
