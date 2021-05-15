print('Hey Elvis...')
#brain
set1 = {'quest': ['hello', 'hi'], 'response':'Hey,\nI am Elvis, your virtual assistant.'}
set2 = {'quest': ['what is the time', 'what says the time', 'what is time', 'time'], 'response':'the time is...'}
set3 = {'quest': ['whats up', 'sup'], 'response':'I...am good'}

profiles = [set1, set2, set3]

chat_on = True

while chat_on:
	reciever = input('') #ear
	if reciever:
		if reciever == 'exit':
			chat_on = False
		else:
			for profile in profiles:
				if reciever.strip().lower() in profile['quest']:
					print(profile['response']) #mouth
	else:
		print('I am a chatbot... use me!')