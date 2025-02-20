import cv2
import os

img = cv2.imread(r"C:\New folder\white-offroader-jeep-parking.jpg")

if img is None:
    print("Error: Image not found")
    exit()

msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Check image dimensions
height, width, _ = img.shape
if len(msg) * 3 > height * width:
    print("Error: Image is too small to hide the message")
    exit()

# Encryption
d = {chr(i): i for i in range(255)}  # Encoding dictionary
c = {i: chr(i) for i in range(255)}  # Decoding dictionary

n = m = z = 0

# Embed the message into the image
for i in range(len(msg)):
    pixel_value = d[msg[i]]  # Get corresponding pixel value for the message
    img[n, m, z] = pixel_value  # Modify pixel value with the message's character value

    n += 1
    m += 1
    z = (z + 1) % 3

    # Ensure we don't go out of bounds of the image
    if m == width:
        m = 0
        n += 1
    if n == height:
        n = 0  # reset to top when we run out of rows

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open the image on Windows

# Decryption
message = ""
n = m = z = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    # Extract the message from the image
    for i in range(len(msg)):
        message += c[img[n, m, z]]  # Convert pixel back to the corresponding character

        n += 1
        m += 1
        z = (z + 1) % 3

        # Ensure we don't go out of bounds of the image
        if m == width:
            m = 0
            n += 1
        if n == height:
            n = 0  # reset to top when we run out of rows

    print("Decrypted message:", message)
else:
    print("Incorrect passcode. Unauthorized.")
