#https://docs.python.org/zh-cn/3/library/itertools.html

import itertools

#实参 start, [step]，输出： start, start+step, start+2*step, ...
natuals = itertools.count(3, 2)

for n in natuals:
    print(n)
    if n >= 10:
        break
print("\n")

# 循环遍历字符 "A" "B" "C"
cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t -= 1
    if t == 0:
        break
print("\n")

# 字符串 Vance 重复 6 次
myRepeat = itertools.repeat("Vance", 6)
for i in myRepeat:
    print(i)