
import json
import csv
from pathlib import Path
from typing import List, Dict, Any


def json_to_csv(json_path: str, csv_path: str) -> None:

    json_file = Path(json_path)
    csv_file = Path(csv_path)
    
    if not json_file.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")
    
    try:
        with json_file.open('r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {e}")
    
    if not isinstance(data, list):
        raise ValueError("JSON must contain a list of objects")
    
    if not data:
        raise ValueError("Empty JSON array")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("All JSON array elements must be objects")
    
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    fieldnames = sorted(all_keys)
    
    if not fieldnames:
        raise ValueError("No valid fields found in JSON objects")
    
    csv_file.parent.mkdir(parents=True, exist_ok=True)
    
    with csv_file.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in data:
            row = {key: item.get(key, '') for key in fieldnames}
            row = {k: str(v) for k, v in row.items()}
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    
    csv_file = Path(csv_path)
    json_file = Path(json_path)
    
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
   
    rows = []
    with csv_file.open('r', encoding='utf-8') as f:
        try:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                raise ValueError("CSV file has no headers")
            
            rows = list(reader)
            
        except csv.Error as e:
            raise ValueError(f"Invalid CSV format: {e}")
    
    if not rows:
        raise ValueError("Empty CSV file")
    
    json_file.parent.mkdir(parents=True, exist_ok=True)
    
    with json_file.open('w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)