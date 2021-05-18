import file 

def get_info():
	result = 1
	while result == 1 :
		
		while True:
			try:
				account_number = int(input("\nenter the account number :"))
			except:
				print("\nsorry that was not an expected number !!")
			else:
				break		
		
		result=file.check(account_number)
		if result == 1 :
			print("\naccount exists...enter a different one ..")
			continue	
	
	name = input("\nenter name :")
	balance = float(input("\nenter the account balance :"))
	file.filecall(account_number,name,balance)
	print("\naccount created")

def deposit_amount():
	result = 0
	while result == 0 :
		
		while True:
			try:
				account_number = int(input("\nenter the account number :"))
			except:
				print("\nsorry that was not an expected number !!")
			else:
				break		
		
		result=file.check(account_number)
		if result == 0 :
			print("\naccount does not exist...enter a valid one ..")
			continue
	bal = file.bal(account_number)
	print("\nyour current balance is : " + str(bal))
	amount = float(input("\nenter the amount to be deposited :"))
	file.deposit(account_number,amount)

def withdraw_amount():
	result = 0
	while result == 0 :
		
		while True:
			try:
				account_number = int(input("\nenter the account number :"))
			except:
				print("\nsorry that was not an expected number !!")
			else:
				break		
		
		result=file.check(account_number)
		if result == 0 :
			print("\naccount does not exist...enter a valid one ..")
			continue
	bal = file.bal(account_number)
	print("\nyour current balance is : " + str(bal))
	res = 1 
	while res == 1 :
		amount = float(input("\nenter the amount to be withdrawn :"))
		res=file.bal_check(account_number,amount)
		if res == 1 :
			print("Sorry ! amount cannot be less than the minimum balance of 500")
			continue
		else :
			continue	
	file.withdraw(account_number,amount)

def display():	
	result = 0
	while result == 0 :
		
		while True:
			try:
				account_number = int(input("\nenter the account number :"))
			except:
				print("\nsorry that was not an expected number !!")
			else:
				break		
		
		result=file.check(account_number)
		if result == 0 :
			print("\naccount does not exist...enter a valid one ..")
			continue

	file.show_account(account_number)		


