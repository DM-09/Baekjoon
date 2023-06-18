floor_max, class_max, classes = map(int, input().split())
closest = 99999999
closest_room = 0

for i in range(classes):
  floor, class_room = map(int, input().split())
  distance = class_max + 1 - class_room + floor - 1
  
  if distance < closest:
    closest_room = i + 1
    closest = distance

print(closest_room)
