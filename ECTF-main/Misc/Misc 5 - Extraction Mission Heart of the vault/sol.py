import subprocess
import os
import pyzipper
import glob

def crack_zip(zip_file):
    """Crack the password of a ZIP file using John the Ripper."""
    hash_file = f"{zip_file}.hash"
    subprocess.run(["zip2john", zip_file], stdout=open(hash_file, "w"))
    subprocess.run(["john", "--wordlist=/usr/share/wordlists/rockyou.txt", hash_file])
    result = subprocess.run(["john", "--show", hash_file], capture_output=True, text=True)
    os.remove(hash_file)
    return result.stdout.split(":")[1].strip() if ":" in result.stdout else None

def extract_zip(zip_file, password):
    """Extract a password-protected ZIP file."""
    try:
        with pyzipper.AESZipFile(zip_file) as zip_ref:
            zip_ref.setpassword(password.encode())
            zip_ref.extractall(os.path.dirname(zip_file))
            os.remove(zip_file)  # Delete ZIP after extraction
    except Exception as e:
        print(f"Error with {zip_file}: {e}")

def process_zip(zip_file, passwords_list):
    """Process a ZIP file, crack it, extract it, and handle nested ZIPs."""
    password = crack_zip(zip_file)
    if password:
        extract_zip(zip_file, password)
        passwords_list.append(password)
        for next_zip in glob.glob(os.path.join(os.path.dirname(zip_file), "*.zip")):
            process_zip(next_zip, passwords_list)

def extract_flag(passwords_list):
    """Extract the flag using predefined indices from the cracked passwords."""
    flag_indexes = [[0, 6], [6, 8], [4, 7], [4, 7], [15, 5], '_', [0, 6], [6, 8], [4, 7], [4, 7], [15, 5], '_', [0, 3], [0, 9], [1, 7], [28, 7]]
    passwords_list = passwords_list[::-1]
    flag = "ectf{"
    for item in flag_indexes:
        flag += "_" if item == "_" else passwords_list[item[0]][item[1]] if len(passwords_list) > item[0] else "?"
    return flag + "}"

if __name__ == "__main__":
    directory = os.path.expanduser("~/Desktop/deeprock")
    passwords_list = []

    # Process all ZIP files in reverse order
    for i in range(200, 0, -1):
        zip_file = os.path.join(directory, f"dwarf_vault_{i}.zip")
        if os.path.isfile(zip_file):
            process_zip(zip_file, passwords_list)

    # Save passwords and extracted flag
    password_file = os.path.join(directory, "passwords.txt")
    with open(password_file, 'w') as f:
        f.write(str(passwords_list))
    flag = extract_flag(passwords_list)
    with open(password_file, 'a') as f:
        f.write(f"\nFlag: {flag}")
    
    print(f"Flag extracted: {flag}")
