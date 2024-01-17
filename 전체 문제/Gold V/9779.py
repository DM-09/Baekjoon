import re

s = re.compile("^da+dd?(i|y)$")

while 1:
    try: i = input()
    except: break

    if s.match(i): print('She called me!!!')
    else: print('Cooing')
