# Crypto 3 - Cracking the Vault

The vault is locked with a key, but we've managed to access a security computer. Unfortunately, the key is encrypted, and the owner forgot to remove the file that encrypts it. It appears to be some sort of homemade encryption, but don’t worry this should be a piece of cake for you, right?  
Flag format: ectf{the_code}  

### Files
Encryption.py : The encryption code.  
VaultKey_encrypted.txt : The file with the flag that is encrypted by Encryption.py  

\Author - Antoine

#### Points :
`250`

### Files Provided
Encryption.py : The encryption code.  
VaultKey_encrypted.txt : The file with the flag that is encrypted by Encryption.py  
VaultKey_decrypted_1.txt : The file decrypted by the programm  
Decryption_solution.py: The solution of the challenge.  

## Solution

### Understanding the Encryption

The Encryption.py script applies a custom encryption method to obscure the contents of `VaultKey_encrypted.txt`. Let's break it down and identify which parts are not used in the final encryption process, focusing on the core logic.  


#### Padding Addition (bait):  
The script adds random padding to make the text length a multiple of 256. This padding is scrambled and manipulated before being appended to the original text. However, this padding and scrambling are just a distraction and don't affect the encryption of the actual flag.

The relevant code for padding:  
```
padding_length = 256 - len(text) % 256
    raw_padding = [chr(random.randint(32, 126)) for _ in range(padding_length)]

    scrambled_padding = [chr((ord(c) * 3 + 7) % 94 + 32) for c in raw_padding]
    shifted_padding = scrambled_padding[::-1]

    padded_text = ''.join(shifted_padding) + text
```

#### Bitwise XOR and Character Shifting (bait):  
The text undergoes a transformation where every second character is XORed with 42. Every second character remains unchanged, adding complexity. This part of the encryption also does not affect the final output, as we will see in the next section.

The XOR operation is done here:  
```
final_padded_text = ''.join(
    chr((ord(c) ^ 42) % 94 + 32) if i % 2 == 0 else c
    for i, c in enumerate(padded_text)
)
```

#### Key Generation (bait):  
A numeric key is derived from the sum of the ASCII values of the original text. This key is reversed and hashed using SHA-256. A 16-byte seed is extracted from the hash for pseudo-randomization. While this key generation is used to create a random seed for pseudo-randomization, it doesn’t affect the actual shifting logic used in the final encryption.  

The key generation logic is:  
```
secret_key = str(sum(ord(c) for c in text))
secret_key = secret_key[::-1]

hashed_key = hashlib.sha256(secret_key.encode()).hexdigest()
seed = int(hashed_key[:16], 16)
random = secrets.SystemRandom(seed)
```

#### Final Encryption Loop (real encryption):
The final loop performs the actual encryption, where each character is shifted based on its position and an offset of 67. This is the core logic that you need to focus on to decrypt the flag.  

Here’s the relevant code for encryption:
```
for i, char in enumerate(text):
    char_code = ord(char)
    shift = (i + 1) * 3
    transformed = (char_code + shift + 67) % 256
    encrypted.append(chr(transformed))
```
This part of the code is the heart of the encryption, where the characters are shifted, and you need to reverse this transformation for decryption.

### Decryption Exploit
Since the encryption only involved shifting characters and adding an offset, you can reverse this process to decrypt the message. Here's the decryption code:
```
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
```
### Flag
The output from this exploit is the following message:  
`Well done! I bet you're great at math. Here's your flag, buddy: ectf{1t_W45_ju5T_4_m1nu5}`


