m = float(input('Insert the value in meters to be converted. '))
cm = float(m * 100)
mm = float(m * 1000)
print('{}m\n{:.0f}cm\n{:.0f}mm.'.format(m, cm, mm))
