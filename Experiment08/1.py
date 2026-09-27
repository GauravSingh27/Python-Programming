def max_min(seq):
    mx = mn = seq[0]
    for x in seq:
        if x > mx: mx = x
        if x < mn: mn = x
    return mx, mn

print(max_min([10,3,8,12,5]))  
