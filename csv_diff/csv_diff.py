# author: weilyu
import csv
from itertools import chain


def is_float(value: str) -> bool:
    try:
        float(value)
    except ValueError:
        return False
    return True


def compare_value(exp_val: str, act_val: str) -> bool:
    if is_float(exp_val) and is_float(act_val):
        return float(exp_val) == float(act_val)
    return exp_val == act_val


with open('actual.csv', encoding='utf8') as act_file, open('expected.csv', encoding='utf8') as exp_file, open('result.csv', mode='w', encoding='utf8') as res_file:
    act_reader = csv.DictReader(act_file)
    exp_reader = csv.DictReader(exp_file)
    fieldnames = exp_reader.fieldnames  # 実際ファイルに余計な項目を無視
    res_file = csv.DictWriter(res_file, fieldnames=fieldnames)
    res_file.writeheader()
    diff_count = 0
    for exp_row, act_row in zip(exp_reader, act_reader):
        row_diff = {}
        for field in fieldnames:
            if field not in act_row.keys():
                row_diff[field] = exp_row[field] + ' -> ' + 'null'
                diff_count += 1
            elif not compare_value(act_row[field], exp_row[field]):
                row_diff[field] = exp_row[field] + ' -> ' + act_row[field]
                diff_count += 1
        res_file.writerow(row_diff)

    print('Found', diff_count, 'differents. ')
