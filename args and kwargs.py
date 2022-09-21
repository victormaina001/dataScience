def adder(*num):
    sum=0
    for n in num:
        sum = sum+n
    print("sum:",sum)
    
adder(3,5)
adder(6,7,8)
adder(9,10,11)


def intro(**data):
    print("\n Data of argument:",type(data))
    for key,value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)