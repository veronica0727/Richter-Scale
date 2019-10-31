#Python Richter Scale Calculation
#Your First and Last: Veronica Marquez
#Your ID: s1125739

scale = True

while scale == True:
    richter = float(input('Enter a Richter scale value (Enter -99 to QUIT): ' ))
    if richter == -99:
        break
    while richter < 0:
        richter = float(input('Value must be greater than 0! Enter a new value: '))
    if richter >= 8:
            print('Most Structures Fall')
    elif richter >= 7:
            print('Many Buildings Destroyed')
    elif richter >= 6:
            print('Many Buildings Considerably Damaged, some Collapse')
    elif richter >= 4.5:
            print('Damage to Poorly Constructed Buildings')
    else:
            print('No Destruction of Buildings')
