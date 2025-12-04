import subprocess
import sys
from pathlib import Path

def run_command(cmd):
    print(f"\n{'='*60}")
    print(f"Выполняем: {cmd}")
    print(f"{'='*60}")
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    
    if result.stderr:
        print(result.stderr)
    
    print(f"Код возврата: {result.returncode}")
    
    return result.returncode == 0

def main():
    # Создаем выходную директорию если её нет
    Path("data/out").mkdir(parents=True, exist_ok=True)
    
    print("ТЕСТИРОВАНИЕ CLI УТИЛИТ ЛАБОРАТОРНОЙ РАБОТЫ №6")
    print("=" * 60)
    
    # Тестирование cli_text.py
    print("\n1. ТЕСТИРОВАНИЕ CLI_TEXT.PY")
    print("-" * 40)
    
    # 1.1. Вывод справки
    run_command("python -m src.lab06.cli_text --help")
    
    # 1.2. Вывод справки по команде cat
    run_command("python -m src.lab06.cli_text cat --help")
    
    # 1.3. Вывод файла без нумерации
    run_command("python -m src.lab06.cli_text cat --input data/samples/text.txt")
    
    # 1.4. Вывод файла с нумерацией
    run_command("python -m src.lab06.cli_text cat --input data/samples/text.txt -n")
    
    # 1.5. Вывод справки по команде stats
    run_command("python -m src.lab06.cli_text stats --help")
    
    # 1.6. Анализ текста (топ-5 по умолчанию)
    run_command("python -m src.lab06.cli_text stats --input data/samples/text.txt")
    
    # 1.7. Анализ текста (топ-3)
    run_command("python -m src.lab06.cli_text stats --input data/samples/text.txt --top 3")
    
    # Тестирование cli_convert.py
    print("\n2. ТЕСТИРОВАНИЕ CLI_CONVERT.PY")
    print("-" * 40)
    
    # 2.1. Вывод справки
    run_command("python -m src.lab06.cli_convert --help")
    
    # 2.2. Конвертация JSON в CSV
    run_command("python -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people.csv")
    
    # 2.3. Конвертация CSV в JSON
    run_command("python -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people.json")
    
    # 2.4. Конвертация CSV в XLSX (демо-режим)
    run_command("python -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx")
    
    # 2.5. Тестирование ошибок
    print("\n3. ТЕСТИРОВАНИЕ ОБРАБОТКИ ОШИБОК")
    print("-" * 40)
    
    # Несуществующий файл
    run_command("python -m src.lab06.cli_convert json2csv --in несуществующий.json --out data/out/test.csv")
    
    # Неверная команда
    run_command("python -m src.lab06.cli_text unknown_command")
    
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("=" * 60)

if __name__ == "__main__":
    main()