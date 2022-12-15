def seven(value=0): #your code here
    if value == 0:
        print("h")
        return 7
    
    print("H")
    global num1 
    num1 = 7
    ans = value
    return ans 

def times(num): #your code here
    return num1*num

import time

# num = 0
# while True:
#     num = (num+1)%4
#     print(num)
#     time.sleep(0.5)


fruit = {"apple": 5, "banana": 3, "orange": 4}

print(fruit[5])