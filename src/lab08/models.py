from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import ClassVar
import re


@dataclass
class Student:
    
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    DATE_FORMAT: ClassVar[str] = "%Y-%m-%d"
    GPA_MIN: ClassVar[float] = 0.0
    GPA_MAX: ClassVar[float] = 5.0
    
    def __post_init__(self):
        self._validate_birthdate()
        self._validate_gpa()
        self._validate_fio()
    
    def _validate_birthdate(self) -> None:
        try:
            datetime.strptime(self.birthdate, self.DATE_FORMAT)
        except ValueError:
            raise ValueError(
                f"Неверный формат даты: {self.birthdate}. "
                f"Ожидается: {self.DATE_FORMAT}"
            )
    
    def _validate_gpa(self) -> None:
        if not (self.GPA_MIN <= self.gpa <= self.GPA_MAX):
            raise ValueError(
                f"Средний балл {self.gpa} вне допустимого диапазона "
                f"[{self.GPA_MIN}, {self.GPA_MAX}]"
            )
    
    def _validate_fio(self) -> None:
        if not self.fio or not self.fio.strip():
            raise ValueError("ФИО не может быть пустым")
    
    def age(self) -> int:

        birth_date = datetime.strptime(self.birthdate, self.DATE_FORMAT).date()
        today = date.today()
        
        age = today.year - birth_date.year
        
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age
    
    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
            "age": self.age()  
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        
        student_data = {
            "fio": data["fio"],
            "birthdate": data["birthdate"],
            "group": data["group"],
            "gpa": float(data["gpa"]) 
        }
        return cls(**student_data)
    
    def __str__(self) -> str:
        return (f"Студент: {self.fio}\n"
                f"Группа: {self.group}\n"
                f"Дата рождения: {self.birthdate} (возраст: {self.age()} лет)\n"
                f"Средний балл: {self.gpa:.2f}")
    
    def __repr__(self) -> str:
        return (f"Student(fio={self.fio!r}, "
                f"birthdate={self.birthdate!r}, "
                f"group={self.group!r}, "
                f"gpa={self.gpa})")


if __name__ == "__main__":
    try:
        student1 = Student(
            fio="Иванов Иван Иванович",
            birthdate="2000-05-15",
            group="SE-01",
            gpa=4.2
        )
        
        print("=== Пример работы класса Student ===")
        print(student1)
        print()
        
        print("Словарь из объекта:")
        print(student1.to_dict())
        print()
        
        print("Объект из словаря:")
        student_dict = {
            "fio": "Петров Петр Петрович",
            "birthdate": "1999-11-30",
            "group": "CS-02",
            "gpa": 3.8
        }
        student2 = Student.from_dict(student_dict)
        print(student2)
        
    except ValueError as e:
        print(f"Ошибка валидации: {e}")