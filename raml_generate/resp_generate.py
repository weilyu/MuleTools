"""
author: weilyu
"""
TYPE_MAPPING = {
    '文字列': 'string',
    '数値': 'number',
    '論理型': 'boolean',
    '日時': 'datetime',
    '日付': 'date-only',
    '時刻': 'time-only'
}

FNAME_PRE = '  '
PROP_PRE = '    '

def sfname_to_jsonname(sfname: str):
    return sfname.replace('__c', '')


# 数値の場合：maxlen - 整数桁数、minlen - 小数点以下の桁数
def get_field_raml(fname, description, ftype, example):
    result = FNAME_PRE + sfname_to_jsonname(fname) + ':\n'
    result += PROP_PRE + 'type: ' + TYPE_MAPPING[ftype] + '\n'
    result += PROP_PRE + 'description: ' + description + '\n'
    result += PROP_PRE + 'example: ' + example + '\n'
    return result


input_file = open('input.txt', encoding='utf8')
raml = '#%RAML 1.0 DataType\ntype: object\nproperties:\n'
for line in input_file:
    props = line.strip().split('\t')
    if len(props) < 3:
        print('Passed line:', line)
        continue
    raml += get_field_raml(props[0], props[1], props[2], props[3])
output_file = open('output.txt', encoding='utf8', mode='w')
output_file.write(raml)

print('Done')
