import re


def printer(t, b):
    txt = f'<{t}> is not acceptable.'
    if b: txt = f'<{t}> is acceptable.'

    print(txt)

def is_(t):
    if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i:
        ct = re.sub('aa|bb|cc|dd|ff|gg|hh|ii|jj|kk|ll|mm|nn|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz', '^', i)
        if ct.count('^') != 0:
            return False

        cct = re.sub('b|c|d|f|g|h|j|k|l|n|m|p|q|r|s|t|v|w|x|y|z', '#', i)
        cct = re.sub('a|e|i|o|u', '@', cct)
        if '###' in cct or '@@@' in cct:
            return False
        else:
            return True
    return False

while True:
    i = input()
    if i == 'end': break
    printer(i, is_(i))
