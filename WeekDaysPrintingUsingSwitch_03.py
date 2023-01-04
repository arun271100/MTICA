def day1():
    print('Sunday')
def day2():
    print('Monday')
def day3():
    print('Tuesday')
def day4():
    print('Wednesday')
def day5():
    print('Thursday')
def day6():
    print('Friday')
def day7():
    print('Saturday')

select={1:day1,2:day2,3:day3,4:day4,5:day5,6:day6,7:day7}
opt=0
while True:
    opt=int(input())
    if opt<1 or opt>7:
        print('INVALID INPUT :  ')
        break
    select[opt]()
