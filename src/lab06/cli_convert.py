import argparse
import sys
import json
import csv
from pathlib import Path

def json_to_csv_converter(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        if not data:
            print("Ошибка: JSON файл пуст или имеет неверный формат")
            return False
        headers = list(data[0].keys())
        
        with open(output_path, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Успешно конвертировано: {input_path} -> {output_path}")
        print(f"Записей обработано: {len(data)}")
        return True
        
    except Exception as e:
        print(f"Ошибка при конвертации JSON в CSV: {e}")
        return False

def csv_to_json_converter(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
        
        print(f"Успешно конвертировано: {input_path} -> {output_path}")
        print(f"Записей обработано: {len(data)}")
        return True
        
    except Exception as e:
        print(f"Ошибка при конвертации CSV в JSON: {e}")
        return False

def csv_to_xlsx_converter(input_path, output_path):
    try:
        import warnings
        warnings.warn("Для полной функциональности установите openpyxl: pip install openpyxl")
        print(f"Демо-режим: конвертация CSV -> XLSX")
        print(f"Входной файл: {input_path}")
        print(f"Выходной файл: {output_path}")
        print("Для реальной конвертации используйте функции из lab05")
        
        with open(output_path, 'w') as f:
            f.write("XLSX file placeholder - use lab05 functions for real conversion\n")
        
        return True
        
    except ImportError:
        print("Для работы с XLSX файлами требуется библиотека openpyxl")
        print("Установите её: pip install openpyxl")
        return False
    except Exception as e:
        print(f"Ошибка при конвертации CSV в XLSX: {e}")
        return False

def validate_paths(input_path, output_path, parser=None):
    input_path = Path(input_path)
    output_path = Path(output_path)
    
    if not input_path.exists():
        error_msg = f"Входной файл не найден: {input_path}"
        if parser:
            parser.error(error_msg)
        else:
            print(error_msg)
            return False
    output_dir = output_path.parent
    if not output_dir.exists():
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            error_msg = f"Не удалось создать директорию {output_dir}: {e}"
            if parser:
                parser.error(error_msg)
            else:
                print(error_msg)
                return False
    
    return True

def json2csv_command(args):
    if validate_paths(args.input, args.output):
        success = json_to_csv_converter(args.input, args.output)
        sys.exit(0 if success else 1)

def csv2json_command(args):
    if validate_paths(args.input, args.output):
        success = csv_to_json_converter(args.input, args.output)
        sys.exit(0 if success else 1)

def csv2xlsx_command(args):
    if validate_paths(args.input, args.output):
        success = csv_to_xlsx_converter(args.input, args.output)
        sys.exit(0 if success else 1)

def main():
    parser = argparse.ArgumentParser(
        description="Конвертер данных между форматами JSON, CSV и XLSX",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python -m src.lab06.cli_convert json2csv --in data.json --out data.csv
  python -m src.lab06.cli_convert csv2json --in data.csv --out data.json
  python -m src.lab06.cli_convert csv2xlsx --in data.csv --out data.xlsx
        """
    )
    
    subparsers = parser.add_subparsers(
        dest="command",
        title="доступные команды конвертации",
        required=True,
        help="выберите тип конвертации"
    )
    json2csv_parser = subparsers.add_parser(
        "json2csv",
        help="конвертировать JSON в CSV"
    )
    json2csv_parser.add_argument(
        "--in", dest="input",
        required=True,
        help="входной JSON файл"
    )
    json2csv_parser.add_argument(
        "--out", dest="output",
        required=True,
        help="выходной CSV файл"
    )
    json2csv_parser.set_defaults(func=json2csv_command)
    
    csv2json_parser = subparsers.add_parser(
        "csv2json",
        help="конвертировать CSV в JSON"
    )
    csv2json_parser.add_argument(
        "--in", dest="input",
        required=True,
        help="входной CSV файл"
    )
    csv2json_parser.add_argument(
        "--out", dest="output",
        required=True,
        help="выходной JSON файл"
    )
    csv2json_parser.set_defaults(func=csv2json_command)
    
    csv2xlsx_parser = subparsers.add_parser(
        "csv2xlsx",
        help="конвертировать CSV в XLSX"
    )
    csv2xlsx_parser.add_argument(
        "--in", dest="input",
        required=True,
        help="входной CSV файл"
    )
    csv2xlsx_parser.add_argument(
        "--out", dest="output",
        required=True,
        help="выходной XLSX файл"
    )
    csv2xlsx_parser.set_defaults(func=csv2xlsx_command)
    
    args = parser.parse_args()
    
    try:
        args.func(args)
    except AttributeError:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()