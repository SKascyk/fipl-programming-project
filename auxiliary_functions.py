def get_bytes(text, key):
    text_bytes = list(text.encode('utf-8'))
    key_bytes = list(key.encode('utf-8'))
    return text_bytes, key_bytes

text = input('Enter any text: ')
key = input('Enter any key: ')

text_b, key_b = get_bytes(text, key)
print(f'''\nAfter get_bytes():
{text_b} (text_bytes)
{key_b} (key_bytes)''')
