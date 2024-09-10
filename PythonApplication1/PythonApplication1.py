def find_vowels(text: str) -> list:
 
    vowels = "аоуыэеёиюя"
    

    vowel_list = [char for char in text.lower() if char in vowels]
    
    return vowel_list

text = input("Введите текст: ")


vowel_list = find_vowels(text)


print("Список гласных букв:", vowel_list)
print("Длина списка:", len(vowel_list))

