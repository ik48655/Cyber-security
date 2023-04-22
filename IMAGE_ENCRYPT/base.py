from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    image_bytes = image.tobytes()
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_image_bytes = cipher.encrypt(pad(image_bytes, AES.block_size))
    encrypted_image = Image.frombytes(image.mode, image.size, encrypted_image_bytes)
    return encrypted_image, iv

def decrypt_image(encrypted_image_path, key, iv):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_image_bytes = encrypted_image.tobytes()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_image_bytes = unpad(cipher.decrypt(encrypted_image_bytes), AES.block_size)
    decrypted_image = Image.frombytes(encrypted_image.mode, encrypted_image.size, decrypted_image_bytes)
    return decrypted_image

image_path = 'image.png'
key = b'mysecretkey12345'
encrypted_image, iv = encrypt_image(image_path, key)
encrypted_image.save('encrypted_image.png')

encrypted_image_path = 'encrypted_image.png'
key = b'mysecretkey12345'
decrypted_image = decrypt_image(encrypted_image_path, key, iv)
decrypted_image.save('decrypted_image.png')
