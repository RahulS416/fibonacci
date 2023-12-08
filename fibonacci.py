nterms = int(input("How many terms of the fibonacci sequence would you like? "))
n1 = 0
n2 = 1
count = 0
while count < nterms-1:
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1
if count < nterms:
      print(n1)