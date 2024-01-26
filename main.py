# #Task_1
lst1 = ["Dilso'z", "Xushnoza", "Odina"]
lst2 = []
def task1(lst1, lst2):
    for item in lst1:
       lst2.append(item[0])
       lst2.sort()
    d = "".join(lst2)
    return d


print(task1(lst1, lst2))






# #Task_2
list =[1, 2, 3, 4, 5, 6, 6, 6 ,7]
list2 = []


def clear(list):
    for items in list:
        if items not in list2:
            list2.append(items)
            list2.sort()
    return list2


print(clear(list))







# #Task_4
get_students = {
    "Student 1": "Steve",
    "Student 2": "Becky",
    "Student 3": "John"
}
result = []

def sort(get_students, result):
    for value in get_students.values():
        result.append(value)
        sort = sorted(result)
    print(sort)


sort(get_students, result)







# #Task_5
student = ["Dilso'z", "Xushnoza", "Odina"]


def add_hello(student):
    for items in student:
        print(f"Hello {items}")


add_hello(student)





# #Task_6
lst = [4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]
result = 1
result2 = 1
result3 = 1
result4 = 1

def calculate(lst, result, result2, result3, result4):
    for num in lst[0]:
        result *= num

    for num2 in lst[1]:
        result2 *= num2

    for num3 in lst[2]:
        result3 *= num3

    for num4 in lst[3]:
        result4 *= num4
    all = result + result2 + result3 + result4

print(calculate(lst, result, result2, result3, result4))






# #Task_7
lst = ["arrey", "print", "return", "index", "reverse"]
lst2 = ["arrey", "print", "return", "index", "reserve"]

def clone(msv, msv2):
    for num in msv:
        for num2 in msv2:
            if num == num2:
                print("1")
                break
        else:
            print("-1")


clone(lst,lst2)





# #Task_8
numbers = ["10100010110"]
list = []

def returnTrue_False(numbers, list):
    for items in numbers:
        for i in items:
            if i == '1':
                list.append(True)

            elif i == '0':
                list.append(False)

        return list



print(returnTrue_False(numbers, list))




# #Task_9
lst = [3, 2, 5]
list2 = [5,3, 7, 9, 2]


def subset(lst, lst2):
    for x in lst:
        if x in lst2:
            return True
        else:
            return False

print(subset(list,list2))




#Task_10

list =[1,4,2,6,3,7,8,9,5]


def find(list):
    sort = sorted(list)
    print(sort[1])


find(list)