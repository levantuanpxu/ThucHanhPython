import random
a=int(input())
b=int(input())
print("mời sếp nhập giá trị 1 :", a)
print("mời sếp nhập giá trị 2:", b)

c=randomlist = random.sample(range(a, b), 5)
print(c)
gia_tri_max = c[0]
for item in c:
    if gia_tri_max < item:
        gia_tri_max = item
print('Gia tri lon nhat la: ', gia_tri_max)