from datetime import datetime; t = datetime.today(); m = t.month
if m < 10: m = '0' + str(m)
print(f"{str(t.year)}-{m}-{str(t.day)}")
