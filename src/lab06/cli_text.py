import argparse
from pathlib import Path
import re
from collections import Counter

def normalize(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def tokenize(text):
    return re.findall(r'\b[a-zа-яё0-9]+\b', text, re.IGNORECASE)

def count_freq(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def top_n(freq, n=5):
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")

    subparsers = parser.add_subparsers(dest="command", help="Доступные команды", required=True)

    stats_parser = subparsers.add_parser("stats", help="Частоты слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Входной текстовый файл")
    stats_parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Количество топовых слов (по умолчанию: 5)",
    )
    
    cat_parser = subparsers.add_parser("cat", help="Вывод содержимого файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    args = parser.parse_args()

    if args.command == "cat":
        file = Path(args.input)
        if not file.exists():
            parser.error(f"Файл '{args.input}' не найден")
        
        with open(file, "r", encoding="utf-8") as f:
            number = 1
            for row in f:
                row = row.rstrip("\n")
                if args.n:  
                    print(f"{number}: {row}")
                    number += 1
                else:
                    print(row)

    elif args.command == "stats":
        file = Path(args.input)
        if not file.exists():
            parser.error(f"Файл '{args.input}' не найден")
        
        with open(file, "r", encoding="utf-8") as f:
            data = f.read()
        
        normalized = normalize(data)
        tokens = tokenize(normalized)
        freq = count_freq(tokens)
        top = top_n(freq, n=args.top)
        print(f"Топ {args.top} слов:")
        for i, (word, count) in enumerate(top, 1):
            print(f"{i}. {word} - {count}")


if __name__ == "__main__":
    main()