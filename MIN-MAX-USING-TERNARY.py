# AUTHOR:- KUSH SHAH
a,b,c = 120,110,130
print((a,b)[a<b]or(b,c)[b<c]and(c,a)[c<a])

max = a if a>b else b
print(max)