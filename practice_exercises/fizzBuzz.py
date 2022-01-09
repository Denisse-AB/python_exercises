# Example fizzBuzz skipping even numbers.
n = int(20)

for x in range(1, n):
  if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
  elif x % 2 == 0:
    continue
  elif x % 3 == 0:
    print("Fizz")
  elif x % 5 == 0:
    print("Buzz")
  else:
    print(x)

# Whithout skipping even numbers
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)
