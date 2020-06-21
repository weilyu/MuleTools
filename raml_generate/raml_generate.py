"""
author: weilyu
"""
TYPE_MAPPING = {
    '文字列': 'string',
    '数値': 'number',
    '論理型': 'boolean',
    '日時': 'datetime-only',
    '日付': 'date-only',
    '時刻': 'time-only'
}

FNAME_PRE = '    '
PROP_PRE = '        '


# 数値の場合：maxlen - 整数桁数、minlen - 小数点以下の桁数
def get_field_raml(fname, ftype, maxlen, minlen, required):
    result = FNAME_PRE + fname + ':\n'
    result += PROP_PRE + 'type: ' + TYPE_MAPPING[ftype] + '\n'
    if maxlen.isdigit():
        if ftype == '文字列':
            result += PROP_PRE + 'maxLength: ' + maxlen + '\n'
        if ftype == '数値':
            result += PROP_PRE + 'maximum: ' + '9' * int(maxlen) \
                + ('.' + '9' * int(minlen) if minlen.isdigit() and int(minlen) > 0 else '') \
                + '\n'
    if minlen.isdigit():
        if ftype == '文字列':
            result += PROP_PRE + 'minLength: ' + minlen + '\n'
        if ftype == '数値' and int(minlen) > 0:
            result += PROP_PRE + 'multipleOf: ' + \
                str(1.0 / pow(10, int(minlen))) + '\n'
    result += PROP_PRE + 'required: ' + \
        ('true' if required == 'Y' else 'false') + '\n'
    return result


input_file = open('input.txt', encoding='utf8')
raml = '#%RAML 1.0 DataType\ntype: object\nproperties:\n'
for line in input_file:
    props = line.strip().split('\t')
    if len(props) < 5:
        print('Passed line:', line)
        continue
    raml += get_field_raml(props[0], props[1], props[2], props[3], props[4])
output_file = open('output.txt', encoding='utf8', mode='w')
output_file.write(raml)

print('Done')
