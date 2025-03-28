# Misc 5 - Extraction Mission Heart of the vault

The dwarves of Deep Rock Galactic have uncovered a series of hidden vaults, each sealed tighter than the last.  
Your mission: crack through the zips, one vault at a time, and uncover what lies beneath.  
Flag format: ectf{the_code}

### File provided:
Misc_5_-_dwarf_vault_200.zip  

\Author - Antoine

#### Points :
`450`
### Other files
drop_pod.py: Python file that serves as a hint for the flag and is located in the last zip.

mining_report.txt: Text file output from the drop_pod.py file, which contains the position hints for the flag based on the zip passwords.

rock.sh: Script that constructs the zips and finally the mining_report.txt file.

output.py: Python file that constructs the mining_report.txt file.

sol.py: Python file that is the solution to the challenge.

password.txt: Text file that is the output of sol.py and contains the flag.

dwarf_vault_200.zip: Zip file of the challenge.

## Overview
The task involves cracking the password of multiple ZIP files using a wordlist-based approach and extracting the flag from these files. Each ZIP file contained another ZIP file (named dwarf_vault_X.zip, where X is a number from 1 to 200), and this process needed to be repeated recursively until we extracted the final flag. Once the passwords for the ZIP files were cracked and the files were extracted, the flag was hidden and reconstructed using specific coordinates derived from the cracked passwords.

The ultimate goal was to reconstruct the flag using certain characters from the cracked passwords, based on predefined positions.

### Tools and Techniques Used
John the Ripper: This tool was used to crack the password of each ZIP file. You utilize the zip2john tool to generate a hash of the ZIP file and john to attempt cracking the password using a wordlist (rockyou.txt).

Pyzipper: This library was used for handling the extraction of the contents of the ZIP files. We specifically used the AESZipFile class to extract password-protected ZIP files.

Python Scripting: The extraction and cracking process was automated with Python, which recursively handled ZIP files and tracked passwords used for cracking.

## Solution
### Step 1: Cracking the ZIP Passwords
Each ZIP file was password-protected, and you needed to crack the password for each one. This was achieved by using zip2john and john:

1. zip2john: This tool generates a hash from the ZIP file, which John the Ripper can then attempt to crack.
2. john: John the Ripper attempts to find the password using a wordlist (in this case, the popular rockyou.txt wordlist).
```
def crack_zip(zip_file):
    hash_file = f"{zip_file}.hash"
    subprocess.run(["zip2john", zip_file], stdout=open(hash_file, "w"))
    subprocess.run(["john", "--wordlist=/usr/share/wordlists/rockyou.txt", hash_file])
    result = subprocess.run(["john", "--show", hash_file], capture_output=True, text=True)
    os.remove(hash_file)
    return result.stdout.split(":")[1].strip() if ":" in result.stdout else None
```
### Step 2: Extracting ZIP Contents
Once you had cracked the password of a ZIP file, you use pyzipper to extract the contents:
```
def extract_zip(zip_file, password):
    try:
        with pyzipper.AESZipFile(zip_file) as zip_ref:
            zip_ref.setpassword(password.encode())
            zip_ref.extractall(os.path.dirname(zip_file))
            os.remove(zip_file)  # Delete ZIP after extraction
    except Exception as e:
        print(f"Error with {zip_file}: {e}")
```
### Step 3: Handling Nested ZIP Files
The ZIP files contained other ZIP files. These nested files were processed recursively. The script handled nested ZIPs by extracting and cracking each new ZIP file as it was found:
```
def process_zip(zip_file, passwords_list):
    password = crack_zip(zip_file)
    if password:
        extract_zip(zip_file, password)
        passwords_list.append(password)
        for next_zip in glob.glob(os.path.join(os.path.dirname(zip_file), "*.zip")):
            process_zip(next_zip, passwords_list)

```
### Step 4: Extracting the Flag
Once all ZIP files were processed and cracked, we used predefined indices to extract specific characters from the cracked passwords. These indices were provided in the challenge and referenced positions in the passwords that had been cracked:

```
def extract_flag(passwords_list):
    flag_indexes = [[0, 6], [6, 8], [4, 7], [4, 7], [15, 5], '_', [0, 6], [6, 8], [4, 7], [4, 7], [15, 5], '_', [0, 3], [0, 9], [1, 7], [28, 7]]
    passwords_list = passwords_list[::-1]  # Reverse the order of passwords
    flag = "ectf{"
    for item in flag_indexes:
        flag += "_" if item == "_" else passwords_list[item[0]][item[1]] if len(passwords_list) > item[0] else "?"
    return flag + "}"
```

### Step 5: Saving the Results
To save the results and get the flag you initialize the program with the empty list `passwords_list` then you process each ZIP file in reverse order (from dwarf_vault_200.zip to dwarf_vault_1.zip). Since the ZIP files were created in ascending order (from 1 to 200), the cracking starts with the last file (dwarf_vault_200.zip) and proceeds backward to the first file (dwarf_vault_1.zip). 
```
# Save passwords and extracted flag
if __name__ == "__main__":
    directory = os.path.expanduser("~/Desktop/deeprock")
    passwords_list = []

    # Process all ZIP files in reverse order
    for i in range(200, 0, -1):
        zip_file = os.path.join(directory, f"dwarf_vault_{i}.zip")
        if os.path.isfile(zip_file):
            process_zip(zip_file, passwords_list)
```
As a result, the cracked passwords are added to the passwords_list in reverse order, from 200 to 1.  
The flag is extracted using the list of passwords, and the flag is then appended to the same passwords.txt file.  
```
    # Save passwords and extracted flag
    password_file = os.path.join(directory, "passwords.txt")
    with open(password_file, 'w') as f:
        f.write(str(passwords_list))
    flag = extract_flag(passwords_list)
    with open(password_file, 'a') as f:
        f.write(f"\nFlag: {flag}")
```

### Flag 
After processing all ZIP files and extracting the necessary passwords, the final flag was extracted and appended to the passwords.txt file. The flag in this case was:
`ectf{d1ggy_d1ggy_h0l3}`  
