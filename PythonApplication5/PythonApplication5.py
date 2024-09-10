
def caesar_cipher(message: str, shift: int) -> str:
   
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    n = len(alphabet)  
    
   
    shifted_alphabet = alphabet[shift % n:] + alphabet[:shift % n]
    

    encrypted_message = ''.join(
        shifted_alphabet[alphabet.index(char)] if char in alphabet else char
        for char in message.lower()
    )
    
    return encrypted_message


message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))


encrypted_message = caesar_cipher(message, shift)


print("Зашифрованное сообщение:", encrypted_message)
