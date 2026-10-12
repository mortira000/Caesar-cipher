def caesar_cipher(text: str, shift: int) -> str:
    """
    Шифрует и расшифровывает текст с помощью шифра Цезаря.
    Сдвиг может быть положительным, отрицательным или больше 26.
    """
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            # Смещение для строчных латинских букв
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            # Смещение для заглавных латинских букв
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            # Все остальные символы (пробелы, знаки препинания, цифры) остаются без изменений
            result.append(char)

    return "".join(result)