# Python program to get numbers in a array and find the total count of even, odd numbers in array


def even_odd_count (numbers):
    even = 0
    odd = 0
    for i in numbers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd


numbers = input("Enter the elements: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print(numbers)

odd_count,even_count = even_odd_count(numbers)
prime_count,composite_count = prime_composite_count(numbers)

print("Odd Count = ",odd_count)
print("Even Count = ",even_count)
print("prime_count = ",prime_count)
print("Composite Count = ",composite_count)
