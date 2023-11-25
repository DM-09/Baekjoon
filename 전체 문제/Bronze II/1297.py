d, h, w = map(int, input().split())
side = (h ** 2 + w ** 2) ** 0.5
ratio = d / side
print(int(h * ratio), int(w * ratio))
