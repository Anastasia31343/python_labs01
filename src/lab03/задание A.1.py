def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""
    
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    
    if casefold:
        text = text.casefold()
    
    control_chars = '\t\n\r\v\f'
    for char in control_chars:
        text = text.replace(char, ' ')
    
    text = ' '.join(text.split())
    
    return text


    
result1 = normalize("ПрИвЕт\nМИр\t")
print(result1)
    
result2 = normalize("ёжик, Ёлка", yo2e=True)
print(result2)
    
result3 = normalize("Hello\r\nWorld")
print(result3)

result4 = normalize("  двойные   пробелы  ")
print(result4)