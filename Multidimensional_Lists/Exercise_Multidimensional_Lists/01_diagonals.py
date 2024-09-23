n = int(input())

matrix = [[int(cow) for cow in input().split(', ')]for row in range(n)]
f_diagonal = []
s_diagonal = []
sum_f = None
sum_s = None

for i in range(n):
    f_diagonal.append(matrix[i][i])
    s_diagonal.append(matrix[i][n-i-1])
    sum_f = sum(f_diagonal)
    sum_s = sum(s_diagonal)

print(f"Primary diagonal: {', '.join(str(x) for x in f_diagonal)}. Sum: {sum_f}")
print(f"Secondary diagonal: {', '.join(str(x) for x in s_diagonal)}. Sum: {sum_s}")