a = eval(input("Enter length of first list"))
b = eval(input("Enter length of first list"))
c = eval(input("Enter length of first list"))
list1 = []
list2 = []
list3 = []
print("Enter data for first list")
for i in range(a):
    ele =  eval(input())
    list1.append(ele)
for j in range(b):
    ele = input()
    list2.append(ele)
for k in range(c):
    ele = eval(input())
    list3.append(ele)

# print(list1)
# print(list2)
# print(list3)
print("calculating ")
# for i in list1:
#     for j in list2:
#         for k in list3:
#             cal =  0
#             if j == '+':
#                 cal = list1[i] + list3[i]
#             elif j == '-':
#                 cal = list1[i] - list3[i]
#             elif j == '*':
#                 cal = list1[i] * list3[i]
#             print(f"{list1[i]} {list2[i]} {list3[i]}  = {cal}")

for i in list1:
    for j in list2:
        for k in list3:
            cal =  0
            if j == '+':
                cal = i + k
            elif j == '-':
                cal = i - k
            elif j == '*':
                cal = i * k
            print(f"{i} {j} {k}  = {cal}")