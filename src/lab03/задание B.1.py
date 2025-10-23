#!/usr/bin/env python3
# src/text_stats.py - скрипт для статистики текста

import sys
import re
from collections import Counter

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализация текста"""
    if not text:
        return ""
    
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    
    if casefold:
        text = text.casefold()
    
    control_chars = '\t\n\r\v\f'
    for char in control_chars:
        text = text.replace(char, ' ')
    
    return ' '.join(text.split())

def tokenize(text: str) -> list[str]:
    """Токенизация текста"""
    if not text:
        return []
    
    pattern = r'\b[\w]+(?:-[\w]+)*\b'
    return re.findall(pattern, text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчет частот токенов"""
    return dict(Counter(tokens))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Топ-N самых частых слов"""
    if not freq:
        return []
    
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

def main():
    """Основная функция скрипта"""
    # Чтение ввода из stdin
    text = sys.stdin.read().strip()
    
    if not text:
        return
    
    # Обработка текста
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    
    total_words = len(tokens)
    unique_words = len(set(tokens))
    
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)
    
    # Вывод результатов в требуемом формате
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()