# utility.py

import json
import logging
import pathlib
import re
from typing import List


def write_to_file(data):
    output = []
    with open('./perf_001.json', 'r+') as fin: 
        try:
            output = json.load(fin)
        except:
            logging.info('File Empty or corrupt json data')
            
    output.append(data)
    
    with open('./perf_001.json', 'w') as fin: 
        json.dump(output, fin, indent=2)


def stats_file_handler():
    cwd = pathlib.Path('.')
    perf_files = [path.stem for path in cwd.glob('perf_*.json')]

    new_file_number = get_new_file_number(perf_files)
    filename = f"perf_{new_file_number}.json"
    return filename



def get_new_file_number(perf_files: List[str]) -> int:
    file_numbers = []
    for perf_file in perf_files:
        match = re.search('perf_(\d{3})\.json', perf_file)
        if match:
            file_numbers.append(int(match.group(1)))
    max_number = max(file_numbers) if file_numbers else 0
    new_file_number = max_number + 1
    return new_file_number

    
