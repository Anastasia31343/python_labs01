import re

def tokenize(text: str) -> list[str]:
    if not text:
        return []
    
    pattern = r'\b[\w]+(?:-[\w]+)*\b'
    tokens = re.findall(pattern, text)
    
    return tokens

result1 = tokenize("привет мир")
print(result1)
    
result2 = tokenize("hello,world!!!")
print(result2)
    
result3 = tokenize("по-настоящему круто")
print(result3)
    
result4 = tokenize("2025 год")
print(result4)
    
result5 = tokenize("emoji 😀 не слово")
print(result5)