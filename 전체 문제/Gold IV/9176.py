l = [('23 * 89 = 2047 = ( 2 ^ 11 ) - 1', 11), ('47 * 178481 = 8388607 = ( 2 ^ 23 ) - 1', 23), ('233 * 1103 * 2089 = 536870911 = ( 2 ^ 29 ) - 1', 29), ('223 * 616318177 = 137438953471 = ( 2 ^ 37 ) - 1', 37), ('13367 * 164511353 = 2199023255551 = ( 2 ^ 41 ) - 1', 41), ('431 * 9719 * 2099863 = 8796093022207 = ( 2 ^ 43 ) - 1', 43), ('2351 * 4513 * 13264529 = 140737488355327 = ( 2 ^ 47 ) - 1', 47), ('6361 * 69431 * 20394401 = 9007199254740991 = ( 2 ^ 53 ) - 1', 53), ('179951 * 3203431780337 = 576460752303423487 = ( 2 ^ 59 ) - 1', 59)]
n = int(input())

for i in l:
  if i[1] > n: break
  print(i[0])
