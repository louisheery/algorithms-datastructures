# PROBLEM: Merge List a and b (which can be assumed to be sorted) so that the resulting list is also sorted

# Input Lists
a = [1, 5, 8, 10, 14, 19]
b = [6, 9, 12, 18]

# Resulting List
c = []

# Solution
positionA = 0
positionB = 0

while (positionA < len(a)) and (positionB < len(b)):

  if a[positionA] < b[positionB]:
    c.append(a[positionA])
    positionA += 1

  else:
    c.append(b[positionB])
    positionB += 1

while positionA < len(a):
  c.append(a[positionA])
  positionA += 1

while positionB < len(b):
  c.append(b[positionB])
  positionB += 1

print(c)
