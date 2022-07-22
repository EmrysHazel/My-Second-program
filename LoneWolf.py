from datetime import date
from datetime import datetime
#Program  = Vorth
#Idea - To be a your personal butler.
Lastname = input('Enter your last name : ')
print('Welcome sir', Lastname + '. How may I aid you today sire?')
comm1 = str(input('So what is it sire? \nA. Date \nB. Time\n: '))
today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
if comm1 in ['a' , 'A']:
    print('It is ' + str(today) + ' sire.')
elif comm1 in ['b', 'B']:
    print("It is", current_time , 'now sire.')

    












