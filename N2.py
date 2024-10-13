a, b, c = [int(input()) for _ in range(3)]
if a == b == c:
    print('Равносторонний')
elif (a == b or a == c or b == c) and (a != b or a != c or b != c):
    print('Равнобедренный')
elif a != b and a != c and b != c:
    print('Разносторонний')

while True:
   pass