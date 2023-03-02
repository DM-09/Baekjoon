input(); vote = input();
A, B = vote.count('A'), vote.count('B')

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')
