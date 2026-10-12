import math


# ==================== 1. ШИФР ЦЕЗАРЯ ====================
def caesar_cipher(text: str, shift: int) -> str:
    """Шифрует и расшифровывает текст с помощью шифра Цезаря."""
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    return "".join(result)


# ==================== 2. АФФИННЫЙ ШИФР ====================
def mod_inverse(a: int, m: int) -> int:
    """Находит обратный элемент к 'a' по модулю 'm'."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Число {a} не имеет обратного элемента по модулю {m}")


def affine_encrypt(text: str, a: int, b: int) -> str:
    """Шифрование Аффинным шифром: E(x) = (a*x + b) mod 26"""
    if math.gcd(a, 26) != 1:
        raise ValueError(f"Недопустимый ключ a={a}: он должен быть взаимно простым с 26!")

    result = []
    for char in text:
        if 'a' <= char <= 'z':
            x = ord(char) - ord('a')
            new_char = chr((a * x + b) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            x = ord(char) - ord('A')
            new_char = chr((a * x + b) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    return "".join(result)


def affine_decrypt(text: str, a: int, b: int) -> str:
    """Расшифровка Аффинного шифра: D(y) = a_inv * (y - b) mod 26"""
    if math.gcd(a, 26) != 1:
        raise ValueError(f"Недопустимый ключ a={a}: он должен быть взаимно простым с 26!")

    a_inv = mod_inverse(a, 26)
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            y = ord(char) - ord('a')
            new_char = chr((a_inv * (y - b)) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            y = ord(char) - ord('A')
            new_char = chr((a_inv * (y - b)) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    return "".join(result)


# ==================== 3. ШИФР АТБАШ ====================
def atbash_cipher(text: str) -> str:
    """
    Шифр Атбаш заменяет букву на симметричную с другого конца алфавита (A<->Z, B<->Y).
    Для расшифровки применяется эта же функция.
    """
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr(ord('z') - (ord(char) - ord('a')))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            new_char = chr(ord('Z') - (ord(char) - ord('A')))
            result.append(new_char)
        else:
            result.append(char)
    return "".join(result)


# ==================== МЕНЮ И ВЗАИМОДЕЙСТВИЕ ====================
def main():
    print("=== Программа шифрования ===")
    print("1. Шифр Цезаря")
    print("2. Аффинный шифр")
    print("3. Шифр Атбаш")

    choice = input("Выберите шифр (1-3): ").strip()

    if choice == "1":
        user_text = input("Введите текст: ")
        try:
            shift = int(input("Введите ключ (сдвиг): "))
            enc = caesar_cipher(user_text, shift)
            dec = caesar_cipher(enc, -shift)
            print(f"Зашифрованный текст: {enc}")
            print(f"Расшифрованный текст: {dec}")
        except ValueError:
            print("Ошибка: ключ должен быть целым числом.")

    elif choice == "2":
        user_text = input("Введите текст: ")
        try:
            a = int(input("Введите ключ 'a' (взаимно простой с 26): "))
            b = int(input("Введите ключ 'b' (сдвиг): "))
            enc = affine_encrypt(user_text, a, b)
            dec = affine_decrypt(enc, a, b)
            print(f"Зашифрованный текст: {enc}")
            print(f"Расшифрованный текст: {dec}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    elif choice == "3":
        user_text = input("Введите текст: ")
        enc = atbash_cipher(user_text)
        dec = atbash_cipher(enc)  # Двойное применение возвращает исходный текст
        print(f"Зашифрованный текст: {enc}")
        print(f"Расшифрованный текст: {dec}")

    else:
        print("Некорректный выбор!")


if __name__ == "__main__":
    # --- ТЕСТЫ ЦЕЗАРЯ ---
    assert caesar_cipher("ABC XYZ", 3) == "DEF ABC"
    assert caesar_cipher("xyz", 3) == "abc"
    assert caesar_cipher("Python!", 0) == "Python!"
    assert caesar_cipher("abc", -1) == "zab"

    # --- ТЕСТЫ АФФИННОГО ШИФРА ---
    assert affine_decrypt(affine_encrypt("Hello, World!", 5, 8), 5, 8) == "Hello, World!"

    # --- ТЕСТЫ АТБАШ ---
    assert atbash_cipher("ABC XYZ") == "ZYX CBA"
    assert atbash_cipher("Hello, World!") == "Svool, Dliow!"
    assert atbash_cipher("") == ""
    assert atbash_cipher(atbash_cipher("Test")) == "Test"

    print("Все автотесты для всех трёх шифров успешно пройдены!\n")
    main()