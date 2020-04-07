#https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c
from collections import Counter

def trace(a, size):
    s = 0
    for i in range(size):
        s = s + a[i][i]
    return s;
    
def count_rows(a):
    re = []
    for i in a:
        d = Counter(i)
        val_counts = d.values()
        a = all(i == 1 for i in val_counts)
        re.append(a)
    return re


trace_vals = []
test_cases = int(input())
repeat_rows = []
repeat_cols = []

for i in range(test_cases):
    col_matrix = []
    matrix_size = int(input())
    matrix_val = []
    for i in range(matrix_size):
        a = input()
        a_list = a.split()
        map_obj = map(int, a_list)
        list_a = list(map_obj)
        matrix_val.append(list_a)
    #calculating trace
    t = trace(matrix_val, matrix_size)
    trace_vals.append(t)
    #get count of rows
    row_count = count_rows(matrix_val)
    r = row_count.count(False)
    repeat_rows.append(r)
    #get the column_values
    for i in range(matrix_size):
        col_v = [row[i] for row in matrix_val]
        col_matrix.append(col_v)
    #get count of cols using the same function
    col_count = count_rows(col_matrix)
    c = col_count.count(False)
    repeat_cols.append(c)
    
for i in range(test_cases):
    k = trace_vals[i]
    r = repeat_rows[i]
    c = repeat_cols[i]
    print("Case #%d: %d %d %d" % (i+1, k, r, c))
