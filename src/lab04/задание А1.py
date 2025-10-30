import csv
from pathlib import Path
from typing import Iterable, Sequence, Union


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
   
    file_path = Path(path)
    return file_path.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: Union[str, Path], 
              header: tuple[str, ...] = None) -> None:
    
    file_path = Path(path)
    rows_list = list(rows)
    
    if rows_list:
        first_length = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != first_length:
                raise ValueError(f"Row {i} has length {len(row)}, expected {first_length}")
    
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with file_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows_list)


def ensure_parent_dir(path: Union[str, Path]) -> None:

    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

try:
    file_content = read_text("src/lab04/test_io.py.txt")
    print(f"   📄 Содержимое ({len(file_content)} символов):")
    print(f"   '{file_content[:50]}...'" if len(file_content) > 50 else f"   '{file_content}'")
    print()
        
    print("2. 📁 Создание директорий...")
    ensure_parent_dir("data/lab04/test_results.csv")
    print("   ✅ Директории созданы!")
    print()
        
    print("3. 💾 Запись CSV файла...")
        
    test_data = [
        ("файл", 1),
        ("прочитан", 1), 
        ("успешно", 1),
        ("test_io", 1),
        ("py", 1)
    ]
        
    write_csv(test_data, "data/lab04/test_output.csv", header=("слово", "количество"))
    print("   ✅ CSV файл создан: data/lab04/test_output.csv")
    print("   📊 Данные записаны:")
    for word, count in test_data:
        print(f"      {word}: {count}")
    print()
        
    print("4. 🔍 Проверка созданного CSV файла...")
    csv_content = read_text("data/lab04/test_output.csv")
    print("   📋 Содержимое CSV:")
    for line in csv_content.split('\n'):
        if line.strip():
            print(f"      {line}")
    print()
        
    print("🎉 Все функции работают корректно!")
    print("=====================================")
        
except FileNotFoundError as e:
    print(f"❌ Ошибка: Файл не найден - {e}")
    print("   Убедитесь, что файл test_io.py существует в папке lab04")
except Exception as e:
    print(f"❌ Ошибка: {e}")
