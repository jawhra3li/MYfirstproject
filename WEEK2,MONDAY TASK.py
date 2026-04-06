#task to do
prev= None
total=0
while True:
    num=input('enter your number, if you want to stop enter end')
    if num=="end":
        print('the program end')
        break
    num=int(num)
    if num==prev:
        print('same previous nummber')
        print('sum before repate= ', total)
        break
    else:
        total+=num
        prev=num
    