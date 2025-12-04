#!/usr/bin/env python3
"""
CLI утилиты для работы с текстом: cat и stats
"""

import argparse
import sys
import os
from pathlib import Path

# Импорт функций из lab03 (предполагаем, что они существуют)
# Для демонстрации создадим упрощенные версии, если оригинальные недоступны

def read_file_lines(filepath):
    """Чтение файла построчно"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()

def word_frequency_analysis(text, top_n=5):
    """
    Анализ частот слов в тексте
    Возвращает список кортежей (слово, частота) отсортированный по убыванию частоты
    """
    # Простая реализация для демонстрации
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        # Очистка от знаков препинания
        word = word.strip('.,!?;:"()[]{}')
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    
    # Сортировка по частоте (убывание)
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]

def cat_command(args):
    """Реализация команды cat"""
    input_path = Path(args.input)
    
    if not input_path.exists():
        print(f"Ошибка: файл '{args.input}' не найден")
        sys.exit(1)
    
    try:
        lines = read_file_lines(input_path)
        for i, line in enumerate(lines, 1):
            if args.n:
                # Вывод с нумерацией
                print(f"{i:6d}  {line.rstrip()}")
            else:
                # Вывод без нумерации
                print(line.rstrip())
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

def stats_command(args):
    """Реализация команды stats"""
    input_path = Path(args.input)
    
    if not input_path.exists():
        print(f"Ошибка: файл '{args.input}' не найден")
        sys.exit(1)
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        top_words = word_frequency_analysis(text, args.top)
        
        print(f"Топ-{args.top} самых частых слов в файле '{args.input}':")
        print("-" * 40)
        print(f"{'Слово':<20} {'Частота':<10}")
        print("-" * 40)
        
        for word, count in top_words:
            print(f"{word:<20} {count:<10}")
            
    except Exception as e:
        print(f"Ошибка при анализе текста: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="CLI утилиты для работы с текстом",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python -m src.lab06.cli_text cat --input data/samples/text.txt -n
  python -m src.lab06.cli_text stats --input data/samples/text.txt --top 10
        """
    )
    
    subparsers = parser.add_subparsers(
        dest="command",
        title="доступные команды",
        required=True,
        help="выберите команду для выполнения"
    )
    
    # Подкоманда cat
    cat_parser = subparsers.add_parser(
        "cat",
        help="вывести содержимое текстового файла"
    )
    cat_parser.add_argument(
        "--input", "-i",
        required=True,
        help="путь к входному файлу"
    )
    cat_parser.add_argument(
        "-n",
        action="store_true",
        help="нумеровать строки при выводе"
    )
    cat_parser.set_defaults(func=cat_command)
    
    # Подкоманда stats
    stats_parser = subparsers.add_parser(
        "stats",
        help="анализ частотности слов в тексте"
    )
    stats_parser.add_argument(
        "--input", "-i",
        required=True,
        help="путь к входному текстовому файлу"
    )
    stats_parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="количество топ-слов для вывода (по умолчанию: 5)"
    )
    stats_parser.set_defaults(func=stats_command)
    
    args = parser.parse_args()
    
    try:
        args.func(args)
    except AttributeError:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()