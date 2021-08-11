import datetime as dt

now = dt.datetime.now()
this_hour = now.hour
this_day = dt.date.today()

def greeting():
	if 0 <= this_hour <= 11:
		return 'Good morning!'
	elif 16 >= this_hour >= 12:
		return 'Good afternoon!'
	elif 22 >= this_hour >= 17:
		return 'Good evening!'
	else:
		return 'Good day!'
print(greeting())
print('I am Elvis, a virtual assistant being developed by the Ife Jeremiah Organization.\nHow may I help you?')

#Data Structure
set1 = {'quest': ['what is the time', 'what says the time', 'what is time', 'time'], 'response':f'The time is {now:%I:%M%p}'}

profiles = [set1]
chat_on = True

# Algorithm
while chat_on:
	reciever = input('')
	if reciever:
		if reciever == 'q':
			chat_on = False
		else:
			for profile in profiles:
				if reciever.strip().lower() in profile['quest']:
					print(profile['response'])