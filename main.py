import layout as lout
lout.titleBar('Poll')
question = 'Do you like music?'
chooseFrom = ['Yes', 'No']
print(question)
noofitem = 0
for i in chooseFrom:
    noofitem = noofitem + 1
    print(noofitem, i)
awnser = []
loop = 'a'
while loop == 'a':
    addin = input('Hello! Choose the number from one of the above. ')
    if addin == 'listresults':
        break
    awnser.append(addin)
for item in awnser:
    print(item)