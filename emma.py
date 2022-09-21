import sys 
def process(string):
    print(string)
    return
def test_code():
    string=sys.stdin.readline()
    process(string)
    
test_code()
days_week=7
def find(num_of_days):
    week=int((num_of_days% 365)/days_week)
    days=(num_of_days%365)%days_week
    if(days==0):
        print(week,"weeks")
    else:
        print(week,"weeks +", days,"days")

find(7 )
#find(num_of_days)
