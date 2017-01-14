def mstomin():
    ms = raw_input("Please insert a value you'd like to convert to seconds: ")
    print "\nDoing some math...\n"

    sec = int(ms) / 1000

    print "Your value in seconds is: " + str(sec) + " seconds\n"

    print "Would you like to convert this number to minutes? (Y/N)"

    choice = raw_input('> ')

    if choice == "y":
        minut = sec / 60
        print "Your result is: " + str(float(minut)) + " minutes.\n"
    else:
        exit()
