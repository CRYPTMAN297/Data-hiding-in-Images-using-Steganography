import cv2
import hashlib
def decrypt_message(image_path= "encrypted_image.png" ):
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image not found or cannot be loaded.")
        height, width, _ = img.shape
        message = ""
        index = 0
        extracted_password_hash = ""
        for row in range(height):
            for col in range(width):
                char = chr(img[row, col, 0]) 
                message += char
                index += 1
                if index == 5: 
                    message_length = int(message[:5]) 
                elif  index == 5+16:  
                    extracted_password_hash = message[5:21] 

                elif index > 5 + 16 and len(message[5 + 16:]) >= message_length:
                  break 
                if index > 5 + 16 and index == 5 + 16 + message_length:
                 break 

            password = input("Enter the passcode: ")
            password_hash = hashlib.sha256(password.encode()).hexdigest()[:16] 
            if password_hash != extracted_password_hash:
             print("❌ Incorrect password! Decryption failed.")  
             return  
 
            secret_message = message[5+16:5+16+message_length].rstrip("\0")
            print(f"Decrypted message:{secret_message.strip()}") 

    except Exception as e:
        print(f"Error:{e}")
if __name__=="__main__":
    image_path = "encrypted_image.png"
    decrypt_message(image_path)