def caesar_encoder(text, shift):
    """
    Encodes the given text using the Caesar cipher with the specified shift.

    :param text: str, the text to encode
    :param shift: int, the shift value for the Caesar cipher
    :return: str, the encoded text
    """
    encoded_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                encoded_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encoded_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encoded_text += char
    return encoded_text

# Example usage:
text = "Hello, World!"
shift = 3
encoded_text = caesar_encoder(text, shift)
print("Encoded text:", encoded_text)