daysinsecond = int(input("enterdays"))
hoursinsecond = int(input("enterhours"))
minutesinsecond = int(input("enterminutes"))
seconds = int(input("enterseconds"))
ask_operation = input ('What time format would you like to choose?(days, hours, minutes or seconds? Or all_together?')
if ask_operation == 'days':
    result = (86400*daysinsecond)
    print(result)
elif ask_operation == 'hours':
    result = (3600*hoursinsecond)
    print(result)
elif ask_operation == 'minutes':
    result = (60*minutesinsecond)
    print(result)
elif ask_operation == 'seconds':
    result = (seconds % 60)
    print(result)
elif ask_operation == 'all_together':
    result = (str(daysinsecond) + " days " + str(hoursinsecond) + ":" + str(minutesinsecond) + ":"+ str(seconds))
    print(result)
else: print('unknown operation')