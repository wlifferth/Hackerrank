# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_quartiles(a):
    a = sorted(a)
    q_2_i = (len(a) - 1) * 0.5
    if q_2_i % 1 != 0:
        q_2 = get_split_index(q_2_i, a)
        lower_half = a[:int(q_2_i + 1)]
        upper_half = a[int(q_2_i + 1):]
    else:
        q_2 = a[int(q_2_i)]
        lower_half = a[:int(q_2_i)]
        upper_half = a[int(q_2_i + 1):]
    q_1_i = (len(lower_half) - 1) * 0.5
    if q_1_i % 1 != 0:
        q_1 = get_split_index(q_1_i, lower_half)
    else:
        q_1 = lower_half[int(q_1_i)]
    q_3_i = (len(upper_half) - 1) * 0.5
    if q_3_i % 1 != 0:
        q_3 = get_split_index(q_3_i, upper_half)
    else:
        q_3 = upper_half[int(q_3_i)]
    return q_1, q_2, q_3


def get_split_index(i, a):
    lower_i = int(i)
    upper_i = int(i + 1)
    return int((a[lower_i] + a[upper_i]) / 2)

if __name__ == "__main__":
    input_len = input()
    a = [int(x) for x in input().split()]
    for q in get_quartiles(a):
        print(q)

