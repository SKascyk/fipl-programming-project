def get_bytes(text: str, key: str) -> tuple[list[int], list[int]]:
    text_bytes = list(text.encode('utf-8'))
    key_bytes = list(key.encode('utf-8'))
    return text_bytes, key_bytes

def extend_key(key_bytes: list[int], length: int) -> list[int]:
    key_len = len(key_bytes)
    if length <= key_len:
        return key_bytes[:length]
    extended = key_bytes * (length // key_len)
    extended.extend(key_bytes[:length % key_len])
    return extended

def get_permutation_order(extended_key: list[int], length: int) -> list[int]:
    pairs = [(extended_key[i], i) for i in range(length)]
    pairs.sort()
    return [idx for _, idx in pairs]

def permute_bytes(text_bytes: list[int], extended_key: list[int], length: int) -> list[int]:
    order = get_permutation_order(extended_key, length)
    return [text_bytes[order[i]] for i in range(length)]

def ksa(key: list[int]) -> list[int]:
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s

def prga(s:list[int] , length: int) -> list[int]:
    i = j = 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        t = (s[i] + s[j]) % 256
        keystream.append(s[t])
    return keystream

# Main Functions

def encrypt(plain_text: str, key: str) -> str:
    text_bytes, key_bytes = get_bytes(plain_text, key)
    length = len(text_bytes)

    extended_key = extend_key(key_bytes, length)
    permuted_bytes = permute_bytes(text_bytes, extended_key, length)
    s = ksa(key_bytes)
    gamma = prga(s, length)

    encrypted_bytes = [p ^ g for p, g in zip(permuted_bytes, gamma)]
    return bytes(encrypted_bytes).hex()

def decrypt(encrypted_hex_bytes: str, key: str) -> str:
    encrypted_bytes = list(bytes.fromhex(encrypted_hex_bytes))
    key_bytes = list(key.encode('utf-8'))
    length = len(encrypted_bytes)
    
    extended_key = extend_key(key_bytes, length)
    s = ksa(key_bytes)
    gamma = prga(s, length)
    permuted_bytes = [eb ^ g for eb, g in zip(encrypted_bytes, gamma)]

    order = get_permutation_order(extended_key, length)
    result = [0] * length
    for i in range(length):
        result[order[i]] = permuted_bytes[i]
    return bytes(result).decode('utf-8')
