import mstosec

mstosec.mstomin()

print "Would you like to do another? (Y/N)"

ans = raw_input('> ')

if ans == 'y':
    converttest.mstomin()
else:
    exit()
