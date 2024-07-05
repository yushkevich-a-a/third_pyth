print("Минимальная сумма инвестиций")
sum = float(input())

print("Средства Mike")
m = float(input())

print("Средства Ivan")
i = float(input())


print('\nУчастие в проекте:')

if m >= sum and i >= sum:
  print(2)
elif (m < sum) and (i < sum) and ((m + i) >= sum):
  print(1)
elif (m >= sum) and (i < sum):
  print("Mike")
elif (i >= sum) and (m < sum):
  print("Ivan")
else:
  print(0)