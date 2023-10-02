import hashlib

# Simulated dictionary of known text and their corresponding hashes
known_hashes = {
    'password1': '5f4dcc3b5aa765d61d8327deb882cf99',  # MD5 hash of 'password1'
    'password2': '2cb42f51d7f7cdd30c61126b8edcdd81',  # MD5 hash of 'password2'
    '22452245Rf': '65e3f9f3dabe42528529a10224434050', # MD5 hash of '2242245Rf'
    # Add more known text-hash pairs as needed
}

def reverse_hash(hash_to_reverse):
    for text, known_hash in known_hashes.items():
        if hash_to_reverse == known_hash:
            return text
    return "Hash not found in dictionary"

def text_to_hash(text):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the text encoded as bytes
    sha256_hash.update(text.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hashed_text = sha256_hash.hexdigest()
    
    return hashed_text

def hash_to_text(hashed_text):
    # This is a one-way hash, so you can't directly convert it back to the original text.
    return "Hash functions are one-way!"

if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Reverse hash code to text")
        print("2. Convert text to hash code (MD5)")
        print("3. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            hash_to_reverse = input("Enter the hash code to reverse: ")
            original_text = reverse_hash(hash_to_reverse)
            print("Original text:", original_text)
        elif choice == "2":
          text = input("Enter the text to hash: ")
          hashed_text = text_to_hash(text)
          print("Hashed text:", hashed_text)
          known_hashes = known_hashes + text:hashed_text
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
