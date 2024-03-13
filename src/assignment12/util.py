def min_along_axis_1(matrix):
    return [min(row) for row in matrix]

def max_of_min(values):
    return max(values)

# Input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

