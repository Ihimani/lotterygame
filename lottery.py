import random
lttry = []
while True:
  a = input("Please enter your name")
  if a=="exit":
    rnd = random.randint(0,len(lttry))
    print(f"Winner is {lttry[rnd]}")
    break
  lttry.append(a)