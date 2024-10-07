from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    split_text = []
    text_index = []
    changed_text_index = []
    encoded_text_list = []
    for ch in text:
        split_text += ch.lower()
    for ch in split_text:
        if ch in alphabet:
            text_index.append(alphabet.index(ch))
        else:
            text_index.append(ch)
    for num in text_index:
        if isinstance(num, int):
            if num + shift > 25:
                changed_text_index.append(num + shift - 26)
            else:
                changed_text_index.append(num + shift)
        else:
            changed_text_index.append(num)
    for num in changed_text_index:
        if isinstance(num, int):
            encoded_text_list.append(alphabet[num])
        else:
            encoded_text_list.append(num)
    encoded_text = "".join(encoded_text_list)
    print(encoded_text)

def decrypt(text, shift):
    split_text = []
    text_index = []
    changed_text_index = []
    decoded_text_list = []
    for ch in text:
        split_text += ch.lower()
    for ch in split_text:
        if ch in alphabet:
            text_index.append(alphabet.index(ch))
        else:
            text_index.append(ch)
    for num in text_index:
        if isinstance(num, int):
            if num + shift < 0:
                changed_text_index.append(num - shift + 26)
            else:
                changed_text_index.append(num - shift)
        else:
            changed_text_index.append(num)
    for num in changed_text_index:
        if isinstance(num, int):
            decoded_text_list.append(alphabet[num])
        else:
            decoded_text_list.append(num)
    decoded_text = "".join(decoded_text_list)
    print(decoded_text)

def caesar(direction):
    if direction.lower() == "encode":
        encrypt(text, shift)
    elif direction.lower() == "decode":
        decrypt(text, shift)
    else:
        print("That was not an option.")

caesar(direction)


