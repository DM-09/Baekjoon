s = '''Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna stop'''

for _ in range(int(input())):
    i = input()
    if not i in s: print('Yes'); break
else: print('No')
