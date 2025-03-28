import secrets

def decryption(encrypted_text):
    original = []
    
    for i, char in enumerate(encrypted_text):
        char_code = ord(char)
        shift = (i + 1) * 3
        original_char_code = (char_code - shift - 67) % 256
        original.append(chr(original_char_code))
    
    original_text = ''.join(original)
    
    
    
    return original_text

with open('VaultKey_encrypted.txt', 'r') as f:
    encrypted_text = f.read()

original_text = decryption(encrypted_text)

with open('VaultKey_decrypted.txt', 'w') as f:
    f.write(original_text)

print("The file has been successfully decrypted!")
