import os
import platform
from cryptography.fernet import Fernet

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def generate_key():
    return Fernet.generate_key()

def encrypt_text(key, text):
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())
    return encrypted_text

def decrypt_text(key, encrypted_text):
    f = Fernet(key)
    decrypted_text = f.decrypt(encrypted_text).decode()
    return decrypted_text

def splash_screen():
    clear_screen()
    print("***************************")
    print("      VOLATILE ver0.1")
    print("***************************")

def write_mode():
    clear_screen()
    content = input("Enter text and press [ENTER] to save >\n\n")
    filename = input("\nEnter a filename > ")
    clear_screen()
    
    key = generate_key()
    encrypted_text = encrypt_text(key, content)
    
    file_path = os.path.expanduser("~/Desktop/{}.volat".format(filename))
    
    with open(file_path, "wb") as file:
        file.write(encrypted_text)
    
    print("Text saved to", file_path)
    print("Encryption key > ", key.decode())
    print("")
    print("KEEP THIS KEY SAFE. If you lose it, you will lose access to your content.\n")
    input("Press Enter to continue...")

def read_mode():
    clear_screen()
    print("Paste your .volat file that you want to read in the desktop.")
    filename = input("Enter filename to read > ")
    file_path = os.path.expanduser("~/Desktop/{}.volat".format(filename))
    key = input("Enter encryption key > ").encode()
    
    try:
        with open(file_path, "rb") as file:
            encrypted_text = file.read()
            decrypted_text = decrypt_text(key, encrypted_text)
            print("\nDecrypted contents of the file:\n\n", decrypted_text)
    except FileNotFoundError:
        print("The file was not found.\n")
    except Exception as e:
        print("An error occurred > ", str(e))
    
    input("\n\nPress [ENTER] to continue...")

def main():
    while True:
        splash_screen()
        print("\nOptions:")
        print("1. Write Mode")
        print("2. Read Mode")
        print("3. Quit")
        
        choice = input("Select an option > ")
        
        if choice == "1":
            write_mode()
        elif choice == "2":
            read_mode()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
