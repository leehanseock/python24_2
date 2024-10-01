a = 33
b = 44

print(id(a))
print(id(b))

b=a

print(id(b))

b = 5
print(id(a))
print(id(b))

print(a)
print(b)
print("===========================")
s = "K-pop star"
L = []
for ch in s :
    L.append(ch)
print(L)
print("===========================")
list =[x**3 for x in range(4) if x%2==1]
print(list)

list2=[]
for y in range(4):
    if y%2 ==1 :
        list2.append(y**3)
print(list2)
print("===========================")
list3 = ["1","9","3","2"]
print(list3[1]+list3[3])

list4 = [int(x) for x in list3]
print(list4[1]+list4[3])
print("===========================")
list5=[1,9,3,2]
print(list5[len(list5)-1])
print(list5[-1])
print("===========================")
res = list5[0:3]
print(res)
res2 = list5[:3]
print(res2)
res3 = list5[1:]
print(res3)
print("===========================")
tmp= []
for i in list5 :
    if i == 9:
        tmp.append(7)
    tmp.append(i)
list5 = tmp
print(list5)
print("===========================")
list6= [1, "abcd", 9, 3, 2]
list6.sort()
print(list6)