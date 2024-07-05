some_list = list(input())

consonants = 0

a = 0
e = 0
i = 0
o = 0
u = 0


for item in some_list:
  if item == 'a':
    a += 1
  elif item == 'e':
    e += 1
  elif item == 'i':
    i += 1
  elif item == 'o':
    o += 1
  elif item == 'u':
    u += 1
  else:
    consonants += 1


print("Колличество a:", a or False)
print("Колличество e:", e or False)
print("Колличество i:", i or False)
print("Колличество o:", o or False)
print("Колличество u:", u or False)
print("Колличество согласных:", consonants)
    