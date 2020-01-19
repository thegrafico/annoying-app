"""
This file encrypt and decrypt some data for security
"""
# dependencies
from cryptography.fernet import Fernet

# Const
FILE_PATH = "./../key.key"


# --
def generate_key() -> bytes:
    """
    Generate a new Key to encrypt and decrypt our data into the database. User should store the key in a file.

    :returns: bytes with the key generated
    """

    # Generate new key
    new_key = Fernet.generate_key()

    # Store the key in a file
    store_key_in_file(new_key)

    return new_key


# --
def store_key_in_file(key: bytes, file_path: str = FILE_PATH):
    """
    Store the key into a text file
    :param key: key to be store in the file
    :param file_path: where the key will be stored
    """

    with open(file_path, "r+") as f:
        text = f.read()
        if len(text) > 0:
            print("File is not empty, so is possible there is a key stored in it."
                  "\nAre you sure you want to create a new key?[y/n]", end=" ")
            user_response = input("")

            if not len(user_response) or user_response.lower().strip() == "n" or user_response[0].lower() == "n":
                print("Key was not created")
                return

    with open(file_path, "wb") as f:
        f.write(key)
        print("Key was created in the file:", file_path)


# --
def read_key_from_file(file_path: str = FILE_PATH) -> bytes:
    """
    get the key in the file
    :param file_path: where the file is located
    """
    file_key = None

    with open(file_path, "rb") as f:
        file_key = f.read()

    # print(file_key, type(file_key))

    return file_key


# --
def encrypt_data(key: bytes, data: str) -> str:
    """
    Encrypt the data
    :param key: key to encrypt the data
    :param data: data to be encrypted
    :returns: bytes encrypted
    """
    # instance class
    cipher_suite = Fernet(key)

    # convert our data into bytes mode
    data_to_bytes = bytes(data, "utf-8")

    encrypted = cipher_suite.encrypt(data_to_bytes)

    return encrypted.decode("utf-8")


# --
def decrypt_data(key: bytes, data: str) -> str:
    """
    decrypt the data into a string format
    :param key: key to decrypt the data
    :param data: data to be decrypted
    :returns: new string with the data decrypted
    """

    cipher_suite = Fernet(key)

    return cipher_suite.decrypt(bytes(data, "utf-8")).decode("utf-8")


if __name__ == "__main__":

    # generate the key
    # key = generate_key()

    key = read_key_from_file()

    encrypted_data = encrypt_data(key, "Lana Nicole Santiago")
    decrypted_data = decrypt_data(key, encrypted_data)
    print("Encrypted Data: ", encrypted_data, type(encrypted_data))
    print("Decrypted Data: ", decrypted_data, type(decrypted_data))
