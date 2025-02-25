import cv2
import os
import hashlib
def encrypt_message(image_path, message,password , output_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image not found or cannot be loaded.")
        height, width, _ = img.shape
        if len(message) > height * width:
            raise ValueError("Message is too long for this image.")
        password_hash = hashlib.sha256(password.encode()).hexdigest()[:16] 
        # Embed message length at the start (for better decoding)
        message = str(len(message)).zfill(5) + password_hash + message  
        index = 0
        for row in range(height):
            for col in range(width):
                if index < len(message):
                    img[row, col, 0] = ord(message[index])  # Store ASCII value in Blue channel
                    index += 1
        cv2.imwrite(output_path, img)
        print(f"Message encrypted successfully. Saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    image_path = ("input.png")
    message = input("Enter secret message: ")
    password = input("Enter a passcode:")
    output_path = "encrypted_image.png"
    encrypt_message(image_path, message,password,output_path)