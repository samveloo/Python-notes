import random
import string
import itertools

# Все возможные символы
chars = string.ascii_letters + string.digits # + string.punctuation

password = input("Set Password: ")
print("\nAccessing Database...\n")

found = False

# Перебираем длину пароля от 1 до бесконечности
for length in range(1, len(password) + 1):
    if found:
        break
        
    # itertools.product генерирует строгие последовательные комбинации без повторов
    for combination in itertools.product(chars, repeat=length):
        guess = "".join(combination)
        
        # Печатаем не каждую попытку, а только сотую часть, чтобы не тормозить консоль
        if random.randint(1, 100) == 1:
            print(f"Trying: {guess}", end="\r")
            
        if guess == password:
            print(f"\n🔑 PASSWORD CRACKED: {password}")
            found = True
            break