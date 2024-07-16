import hashlib

def hash_text(text, algorithm='sha256'):
    """Generate hash of input text using specified algorithm."""
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f'Algorithm "{algorithm}" is not available.')

    hash_func = hashlib.new(algorithm)
    hash_func.update(text.encode('utf-8'))
    return hash_func.hexdigest()

def main():
    while True:
        input_text = input("\nEnter text to hash (or type 'exit' to quit): ")
        
        print("Available algorithms:", hashlib.algorithms_available)
        selected_algorithm = input("Choose an algorithm (e.g., md5, sha1, sha256): ").lower()

        try:
            hashed_text = hash_text(input_text, selected_algorithm)
            print(f"Hash ({selected_algorithm}): {hashed_text}")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()
