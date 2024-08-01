import hashlib as h
print(h.sha384(input().encode()).hexdigest())
