import json
from pathlib import Path
from typing import List
try:
    from models import Student
except ImportError:
    from .models import Student


def students_to_json(students: List[Student], path: str) -> None:
   
    if not students:
        raise ValueError("Список студентов пуст")
    
    data = [student.to_dict() for student in students]
    
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные успешно сохранены в {path}")
    except IOError as e:
        raise IOError(f"Не удалось записать файл {path}: {e}")


def students_from_json(path: str) -> List[Student]:
    
    if not Path(path).exists():
        raise FileNotFoundError(f"Файл {path} не найден")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Некорректный JSON в файле {path}: {e}")
    except IOError as e:
        raise IOError(f"Не удалось прочитать файл {path}: {e}")
    
    if not isinstance(data, list):
        raise ValueError(f"Ожидался список в файле {path}, получен {type(data)}")
    
    students = []
    errors = []
    
    for i, item in enumerate(data):
        try:
            student = Student.from_dict(item)
            students.append(student)
        except (ValueError, KeyError) as e:
            errors.append(f"Строка {i}: {e}")
    
    if errors:
        error_msg = "\n".join(errors)
        raise ValueError(f"Ошибки при загрузке данных:\n{error_msg}")
    
    return students


if __name__ == "__main__":
    try:
        students = [
            Student("Иванов Иван Иванович", "2000-05-15", "SE-01", 4.2),
            Student("Петрова Анна Сергеевна", "2001-08-22", "CS-02", 4.8),
            Student("Сидоров Алексей Петрович", "1999-11-30", "AI-03", 3.5),
        ]
        
        import os
        current_dir = os.path.dirname(__file__)
        output_path = os.path.join(current_dir, "..", "..", "data", "lab08", "students_output.json")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        students_to_json(students, output_path)
        print(f"\nСтуденты сохранены в {output_path}")
        
        print("\nЗагрузка студентов из файла...")
        loaded_students = students_from_json(output_path)
        
        print(f"\nЗагружено {len(loaded_students)} студентов:")
        for student in loaded_students:
            print("-" * 30)
            print(student)
            
    except Exception as e:
        print(f"Ошибка: {e}")