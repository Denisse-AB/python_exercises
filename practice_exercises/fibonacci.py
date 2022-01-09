num = 10

def fibonacci(n):
  #complete the recursive function
  if n <= 1:
    return (n)
  else:
    return (fibonacci(n - 1) + fibonacci(n - 2))


for x in range(0, num):
  print(fibonacci(x))

fibonacci(num)