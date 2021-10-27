number = int(input('Enter an integer: '))
previous = 0
next = 1
sum = 0

while next < number:
    sum = next + previous
    previous = next
    next = sum

if number == next:
    print(f'Number: {number}. Success!')
else:
    print(f'Number: {number}. Error!')