def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("Запись должна быть кортежем из 3 элементов")
    
    fio, group, gpa = rec
    
    if not isinstance(fio, str):
        raise TypeError("ФИО должно быть строкой")
    if not isinstance(group, str):
        raise TypeError("Группа должна быть строкой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должно быть числом")
    
    if not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group.strip():
        raise ValueError("Группа не может быть пустой")
    if gpa < 0:
        raise ValueError("GPA не может быть отрицательным")
    
    fio_parts = ' '.join(fio.split()).split()
    
    surname = fio_parts[0].capitalize()
    
    initials = []
    for name_part in fio_parts[1:]:
        if name_part:  
            initials.append(f"{name_part[0].upper()}.")
    
    formatted_fio = f"{surname} {' '.join(initials)}"
    
    formatted_gpa = f"{gpa:.2f}"
    
    return f"{formatted_fio}, гр. {group.strip()}, GPA {formatted_gpa}"


if __name__ == "__main__":
    test_cases = [
        ("Иванов Иван Иванович", "BIVT-25", 4.6),
        ("Петров Пётр", "IKBO-12", 5.0),
        ("Петров Пётр Петрович", "IKBO-12", 5.0),
        ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
    ]
    
    for test in test_cases:
        result = format_record(test)
        print(result)