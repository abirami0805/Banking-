import csv
import os

def filecall(account_number,name,balance):
    persons=[(account_number,name,balance)]
    csv_file=open("data.csv","a",newline='')
    obj=csv.writer(csv_file)
    obj.writerows(persons)
    csv_file.close()   

def deposit(accnt_num,deposit_amount):
	persons=[]
	csv_file = open("data.csv","r",newline='')
	temp_file = open ("temp.csv","w",newline='')
	obj = csv.reader(csv_file)
	temp= csv.writer(temp_file)
	for line in obj :
		if line[0] == str(accnt_num) :
			bal = float(line[2])
			bal = bal + deposit_amount
			line[2] = str(bal)
			persons.append(line)
		else :
			persons.append(line)
	print("\namount credited \n\n your current balance is : " +str(bal))
	temp.writerows(persons)
	temp_file.close()
	csv_file.close()
	os.remove("data.csv")
	os.rename("temp.csv","data.csv")

def withdraw(accnt_num,withdraw_amount):
	persons=[]
	csv_file = open("data.csv","r",newline='')
	temp_file = open ("temp.csv","w",newline='')
	obj = csv.reader(csv_file)
	temp= csv.writer(temp_file)
	for line in obj :
		if line[0] == str(accnt_num) :
			bal = float(line[2])
			bal = bal - withdraw_amount
			line[2] = str(bal)
			persons.append(line)
		else :
			persons.append(line)
	print("\namount debited \n\nyour current balance is : " +str(bal))
	temp.writerows(persons)
	temp_file.close()
	csv_file.close()
	os.remove("data.csv")
	os.rename("temp.csv","data.csv")	

		
def check(account_number):
	found = 0
	csv_file = open("data.csv","r",newline='')
	obj = csv.reader(csv_file)
	for line in obj :
		if line[0] == str(account_number) :
			found = 1
	return found		

def show_account(account_number):
	found = 0
	csv_file = open("data.csv","r",newline='')
	obj = csv.reader(csv_file)
	for line in obj :
		if line[0] == str(account_number) :
			print("\nACCOUNT INFORMATION :")
			print("\nAccount Number             :" + str(line[0]))
			print("Name Of The Account Holder :" +str(line[1]))
			print("Current Balance            :" + str(line[2]))
			

def bal_check(account_number,amount):
	csv_file = open("data.csv","r",newline='')
	obj = csv.reader(csv_file)
	for line in obj :
		if line[0] == str(account_number) :
			if (float(line[2]) - amount) < 500:
				return 1
			else :
				return 0	

def bal(account_number):
	csv_file = open("data.csv","r",newline='')
	obj = csv.reader(csv_file)
	for line in obj :
		if line[0] == str(account_number) :
			return float(line[2])
