# Enter your code here. Read input from STDIN. Print output to STDOUT

size = input()
numbers = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]
running_numerator = 0
running_denominator = 0
for number, weight in zip(numbers, weights):
    running_numerator += (number * weight)
    running_denominator += weight
print("{:0.1f}".format(running_numerator / running_denominator))

