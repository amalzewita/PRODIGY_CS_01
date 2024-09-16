class CaesarCipher:
    def __init__(self, message, shift):
        """
        Constructor to initialize the CaesarCipher class.
        It takes the message to be encrypted/decrypted and the shift value.
        """
        self.message = message  # Store the message
        self.shift = shift      # Store the shift value (how much to shift each letter)

    def encrypt(self):
        """
        Encrypts the message by shifting each letter by the specified shift value.
        Non-alphabetic characters are not changed.
        """
        encrypted_message = ""  # Initialize an empty string to store the encrypted message
        for char in self.message:
            if char.isalpha():  # Check if the character is a letter (alphabetic)
                # Determine if the letter is uppercase or lowercase
                # 'A' has ASCII code 65, and 'a' has ASCII code 97
                offset = 65 if char.isupper() else 97
                
                # Shift the letter and wrap around the alphabet using modulo 26
                encrypted_message += chr((ord(char) - offset + self.shift) % 26 + offset)
            else:
                # If it's not an alphabetic character (e.g., space, punctuation), leave it unchanged
                encrypted_message += char
        return encrypted_message  # Return the encrypted message
                
    def decrypt(self):
        """
        Decrypts the encrypted message by reversing the shift value.
        Non-alphabetic characters are not changed.
        """
        decrypted_message = ""  # Initialize an empty string to store the decrypted message
        for char in encrypted_message:
            if char.isalpha():  # Check if the character is a letter
                # Determine if the letter is uppercase or lowercase
                offset = 65 if char.isupper() else 97
                
                # Reverse the shift applied during encryption
                decrypted_message += chr((ord(char) - offset - self.shift) % 26 + offset)
            else:
                # Leave non-alphabetic characters unchanged
                decrypted_message += char
        return decrypted_message  # Return the decrypted message

# Main program execution starts here
if __name__ == "__main__":
    # Get the message and shift value from the user
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))  # Convert the shift value to an integer
    
    # Create an instance of CaesarCipher with the user-provided message and shift
    cipher = CaesarCipher(message, shift)
    
    # Encrypt the message and display the result
    encrypted_message = cipher.encrypt()
    print(f"Encrypted Message: {encrypted_message}")
    
    # Decrypt the encrypted message and display the result
    decrypted_message = cipher.decrypt()
    print(f"Decrypted Message: {decrypted_message}")
