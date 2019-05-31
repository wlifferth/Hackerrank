# Enter your code here. Read input from STDIN. Print output to STDOUT
count = input()
numbers = [int(x) for x in input().split()]
mean = sum(numbers) / len(numbers)
print(mean)
sorted_numbers = sorted(numbers)
if len(sorted_numbers) % 2 == 0:
    upper = len(sorted_numbers) // 2
    lower = upper - 1
    median = (sorted_numbers[lower] + sorted_numbers[upper]) / 2
else:
    median = sorted_numbers[len(sorted_numbers) // 2]
print(median)

counts = {}
mode = None
max_count = 0
for x in numbers:
    if x not in counts:
        counts[x] = 0
    counts[x] += 1
    if counts[x] > max_count or (counts[x] == max_count and x < mode):
        max_count = counts[x]
        mode = x
print(mode)


