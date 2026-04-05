import magic
import os
import sys


def detect_file_type(filepath: str) -> dict:
    """
    Определяет MIME-тип и описание файла по его содержимому.

    Возвращает словарь:
    {
        "mime": "image/jpeg",
        "description": "JPEG image data, JFIF standard 1.01"
    }
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"Файл не найден: {filepath}")

    try:
        # Создаём детектор с поддержкой MIME и описания
        mime_type = magic.from_file(filepath, mime=True)
        description = magic.from_file(filepath, mime=False)
        return {
            "mime": mime_type,
            "description": description
        }
    except Exception as e:
        raise RuntimeError(f"Ошибка при анализе файла: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python file_detector.py <путь_к_файлу>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        result = detect_file_type(filepath)
        print(f"Файл: {filepath}")
        print(f"MIME-тип: {result['mime']}")
        print(f"Описание: {result['description']}")
    except (FileNotFoundError, RuntimeError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)