print('This is the available bank ussd code:')
print('Access: *901#\n')
def menu ():
	print("you have entered the code for",bank, "bank")
	print('1. check your balance\n 2. Transfer\n 3. Airtime\n 4. Transaction history')
	option = eval(input("please select an option: "))
	if (option == 1):
		print('Your account balance is 34566 naira')
		print('Enter 1 to return to menu\n Enter 2 to End')
		top = eval(input( ))
		if (top ==1):
			menu ()
		elif(top==2):
			exit()
		else:
				print('wrong input')
				exit()
	elif(option==2):
		trans=eval(input('Enter the account no you want to transfer money to:'))
		amount= eval(input("Enter amount:"))
		pin= eval(input("Enter four digits:"))
		assure= eval(input(f"Do you want to send {amount} to {trans} \n 1. Yes \n 2. No"))
		if (assure==1):
			print('Transaction Successful')
			top=eval(input('Enter 1 to return to menu\n Enter 2 to end'))
			if (top==1):
				menu()
			elif(top==2):
				exit()
			else:
					print('wrong input')
	elif (option==3):
		airtime= eval(input('1. for self\n 2. for others'))
		if (airtime==1):
			amount=eval(input('enter amount:'))
			print('transaction successful')
		elif(airtime==2):
			amount=eval(input('enter amount'))
			number=eval(input('enter the Number you want to buy airtime for: '))
			assure=eval(input(f"do you want to buy {amount} naira worth of airtime for {number} ?\n1.Yes\n2.No"))								
			if (assure==1):
				print('Transaction Successful')
				top=eval(input('Enter 1 to return to menu\nEnter 2 to end'))
				if (top==1):
					menu()
				else:
					print('wrong input')
	elif (option==4):
			print('an sms message would be sent to you shotly')
ussd= eval(input('please type in your bank ussd code:'))
if (ussd==901):
	bank= 'Access'
	menu()
else:
	print('wrong input')										