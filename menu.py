import bank_class


def menu():

	choice = 0 

	while choice != 5 :
		
		print("\n1.create a new account \n2.view details \n3.deposit amount \n4.withdraw amount \n5.exit")
		choice = int(input("enter your choice :"))
		if choice == 1 :
			bank_class.get_info()
		if choice == 2:
			bank_class.display()
		if choice == 3 :
			bank_class.deposit_amount()
		if choice == 4 :
			bank_class.withdraw_amount()
		if choice == 5 :
			continue

	print("thank you ")