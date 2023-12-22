#lists
list = ["this", "is", "a", "list"]
list[0] = "thus"
print(list[0]) #first
print(list[-1]) #last
print(list[0:3]) #0, 1, 2
print(list) #all
numberList = [1,2,3,4,5]
numberList.append(6)
print(numberList)
numberList.insert(0, 'new')
numberList.remove(3)
print(numberList)
print(1 in numberList)
print(len(numberList))