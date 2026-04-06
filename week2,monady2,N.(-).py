## n.negative
negc = 0
while True:
    inputstr = input('Enter a value (empty to end): ')
    
    if inputstr == '':
        break
    try:
        val = int(inputstr)
        if val < 0:
            negc += 1
    except ValueError:
        continue
print("number of negstive number: ", negc)