# PRODIGY_CS_02
A task in compliance with Prodigy InfoTech's Internship Program

This program works as an **Image Encryptor and Decryptor**.

**Steps:**
1. The user is prompted what action (encryption/decryption) they would like to perform.
2. The user is then prompted to input the filename of the image they would like to encrypt/decrypt, assuming that the file is under the same directory as the _imageEncoder.py_ file.
3. The image is then encrypted/decrypted, replacing the original image with the encrypted/decrypted file.
    - Upon encryption, a key is generated to encrypt the file. This key is saved under the _encryptKey.key_ file. The program then iterates through each pixel in the image and obtains its RGB channels, where the generated key is added to the pixel.
    - Upon decryption, the generated key is used to undo the encryption process by subtracting the pixel's RGB channels to the key found in the _encryptKey.key_ file.  
