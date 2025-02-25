# Data-hiding-in-Images-using-Steganography
Secure Data hiding in Images Using Steganography
This project implements image-based steganography to securely hide and retrieve sensitive information within digital images. It enhances security by encrypting the message before embedding it and using password protection to restrict access.

---
# Features
✅ Data Hiding: Uses Least Significant Bit (LSB) steganography for embedding messages into images.
✅ Encryption: Secures the hidden message using AES encryption / SHA-256 hashing.
✅ Password Protection: Prevents unauthorized extraction of hidden data.
✅ Image Integrity: Ensures minimal visual distortion after embedding.
✅ Error Handling: Prevents data loss and ensures reliable decryption.

---
# Technologies Used

Python – Main programming language.
OpenCV  – Image processing libraries.
Cryptography (AES/SHA-256) – For message encryption.

▶ Running the Project
⿡ Hiding a Message in an Image
python encrypt.py

Select an image and enter the secret message.
Provide a password for encryption.
The modified image with hidden data will be saved.

⿢ Extracting the Hidden Message
python decrypt.py

Enter the password to retrieve the hidden message
# Encrypted Image
![image](https://github.com/user-attachments/assets/4625d8e8-4b59-4070-adb7-96e32a276eac)

# Decryption Image
![image](https://github.com/user-attachments/assets/11ad4de1-9e67-459d-a046-4816813c2fba)

# Wrong Passcode
![image](https://github.com/user-attachments/assets/97f4c27c-9280-4394-aa89-2664372c6ee5)



