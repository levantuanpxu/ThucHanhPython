import random
#Tạo 1 số nguyên ngẫu nhiên n trong khoảng [50, 1000] đóng vai trò là số phần tử của List
randomlist = random.sample(range(50, 1000), 5)
print(randomlist)


#Sinh ngẫu nhiên 1 List các số nguyên trong khoảng [-1000, 1000]
randomlist = random.sample(range(-1000, 1000), 5)
print(randomlist)

#3 - Sinh ngẫu nhiên 1 List các số thực tỏng khoảng [-1000.0, 1000.0]
#randomlist = random.sample(range(-1000.0, 1000.0), 5)
#print(randomlist)