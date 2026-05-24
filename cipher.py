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
