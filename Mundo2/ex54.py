from datetime import date

today = date.today().year
tAdult = 0
tUnderAge = 0

for x in range(1, 8):
    birth = int(input('Em que ano a {}º pessoa nasceu? '.format(x)))
    if today - birth >= 18:
        tAdult += 1
    else:
        tUnderAge += 1

print('\n{} pessoas são maior de idade.\n{} pessoas são menor de idade.\n'.format(tAdult, tUnderAge))
