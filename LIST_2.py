# PROGRAM TO FIND NO. OF +VE, -VE, ODD, EVEN, ZEROS FROM A LIST AND AVERAGE OF ALL NUMBERS

def numbers(numbers):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    odd_count = 0
    even_count = 0
    sum = 0

    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        sum += num

    average = sum / len(numbers)

    return positive_count, negative_count, zero_count, odd_count, even_count, average

n = int(input("ENTER NUMBER OF ELEMENTS TO ENTER IN LIST: "))
list = []

for i in range(n):
    num = float(input(f"ENTER NUMBER {i+1}: "))
    list.append(num)

positive, negative, zero, odd, even, avg = numbers(list)

print(f"POSITIVE NUMBERS IN LIST ARE: {positive}")
print(f"NEGATIVE NUMBERS IN LIST ARE: {negative}")
print(f"NUMBER OF ZEROS IN LIST ARE: {zero}")
print(f"ODD NUMBERS IN LIST ARE: {odd}")
print(f"EVEN NUMBERS IN LIST ARE: {even}")
print(f"AVERAGE OF ALL NUMBERS IS: {avg}")
