eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
rus_upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def is_valid_dig(n):
    if n.isdigit() and int(n) in (1, 2):
        return True
    else:
        print('Выберите модуль работы:', '1 - шифратор', '2 - дешифратор', sep = '\n')
        return False

def is_valid_dig_1(n):
    if n.isdigit():
        return True
    else:
        print('Введите число, чтобы определить шаг сдвига')
        return False

def encrypt(step, lang):
    step = int(step)
    lang = int(lang)
    print('Введите сообщение, которое хотите зашифровать')
    message = input()
    encrypted_message = []
    
    for word in message.split():
        encrypted_word = ''
        
        for letter in word:
            if lang == 1:  # Русский
                if letter in rus_lower_alphabet:
                    index = rus_lower_alphabet.index(letter)
                    new_index = (index + step) % 32
                    encrypted_word += rus_lower_alphabet[new_index]
                elif letter in rus_upper_alphabet:
                    index = rus_upper_alphabet.index(letter)
                    new_index = (index + step) % 32
                    encrypted_word += rus_upper_alphabet[new_index]
                else:
                    encrypted_word += letter  # Оставляем символы, не входящие в алфавит
                    
            elif lang == 2:  # Английский
                if letter in eng_lower_alphabet:
                    index = eng_lower_alphabet.index(letter)
                    new_index = (index + step) % 26
                    encrypted_word += eng_lower_alphabet[new_index]
                elif letter in eng_upper_alphabet:
                    index = eng_upper_alphabet.index(letter)
                    new_index = (index + step) % 26
                    encrypted_word += eng_upper_alphabet[new_index]
                else:
                    encrypted_word += letter
        
        encrypted_message.append(encrypted_word)
    
    return encrypted_message

def decrypt(step, lang):
    step = int(step)
    lang = int(lang)
    print('Введите сообщение, которое хотите расшифровать')
    message = input()
    decrypted_message = []
    
    for word in message.split():
        decrypted_word = ''
        
        for letter in word:
            if lang == 1:  # Русский
                if letter in rus_lower_alphabet:
                    index = rus_lower_alphabet.index(letter)
                    new_index = (index - step) % 32
                    decrypted_word += rus_lower_alphabet[new_index]
                elif letter in rus_upper_alphabet:
                    index = rus_upper_alphabet.index(letter)
                    new_index = (index - step) % 32
                    decrypted_word += rus_upper_alphabet[new_index]
                else:
                    decrypted_word += letter
                    
            elif lang == 2:  # Английский
                if letter in eng_lower_alphabet:
                    index = eng_lower_alphabet.index(letter)
                    new_index = (index - step) % 26
                    decrypted_word += eng_lower_alphabet[new_index]
                elif letter in eng_upper_alphabet:
                    index = eng_upper_alphabet.index(letter)
                    new_index = (index - step) % 26
                    decrypted_word += eng_upper_alphabet[new_index]
                else:
                    decrypted_word += letter
        
        decrypted_message.append(decrypted_word)
    
    return decrypted_message


# НАЧАЛО
print('Эта программа шифровки и дешифровки.')
print()

print('Выберите модуль работы:', '1 - шифратор', '2 - дешифратор', sep = '\n')
ans_1 = input()
while not is_valid_dig(ans_1):
    ans_1 = input()
print()

print('Выберите язык:', '1 - русский', '2 - английский', sep = '\n')
ans_2 = input()
while not is_valid_dig(ans_2):
    ans_2 = input()
print()

print('Выберите шаг сдвига (число)')
ans_3 = input()
while not is_valid_dig_1(ans_3):
    ans_3 = input()
print()

if ans_1 == '1':
    new_message = encrypt(ans_3, ans_2)
elif ans_1 == '2':
    new_message = decrypt(ans_3, ans_2)

print('Результат:', ' '.join(new_message))