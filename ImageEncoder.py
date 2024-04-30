from PIL import Image
from cryptography.fernet import Fernet
import os

def create_key():
    return Fernet.generate_key()

def save_key_to_file(key):
    with open("encryptKey.key", "wb") as key_file:
        key_file.write(key)

def encrypt_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    encrypted_image = Image.new(image.mode, (width, height))

    key = create_key()
    save_key_to_file(key)

    f = Fernet(key)

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            encrypted_pixel = tuple((p + k) % 256 for p, k in zip(pixel, f.encrypt(b' ')))
            encrypted_image.putpixel((x, y), encrypted_pixel)

    encrypted_image.save(image_path)
    print("Image encrypted successfully!")

def decrypt_image(image_path):
    try:
        image = Image.open(image_path)
        width, height = image.size
        decrypted_image = Image.new(image.mode, (width, height))

        with open("encryptKey.key", "rb") as key_file:
            key = key_file.read()

        f = Fernet(key)

        for y in range(height):
            for x in range(width):
                pixel = image.getpixel((x, y))
                decrypted_pixel = tuple((p - k) % 256 for p, k in zip(pixel, f.encrypt(b' ')))
                decrypted_image.putpixel((x, y), decrypted_pixel)

        decrypted_image.save(image_path)
        print("Image decrypted successfully!")
    except FileNotFoundError:
        print("Image/key not found!")


def main():
    user_choice = input("What action would you like to perform? (encrypt/decrypt): ").lower()

    if user_choice == 'encrypt':
        image_path = input("Enter the path to the image file: ")
        encrypt_image(image_path)
    elif user_choice == 'decrypt':
        image_path = input("Enter the path to the encrypted image file: ")
        decrypt_image(image_path)
    else:
        print("Invalid option. Terminating the program...")

if __name__ == "__main__":
    main()
