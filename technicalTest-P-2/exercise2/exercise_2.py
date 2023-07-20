def sum_consecutive_numbers(N):
    if N < 1:
        return 0
    return (N * (N + 1)) / 2


N = 5
print(sum_consecutive_numbers(N)) 
