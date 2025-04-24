seq = [input().strip() for _ in range(3)]
rst = 0

for i in range(3):
    if seq[i] == "Fizz" or seq[i] == "Buzz" or seq[i] == "FizzBuzz":
        continue
    else:
        rst = int(seq[i]) + (3 - i)
        break

if rst % 3 == 0 and rst % 5 == 0:
    print("FizzBuzz")
elif rst % 3 == 0:
    print("Fizz")
elif rst % 5 == 0:
    print("Buzz")
else:
    print(rst)
