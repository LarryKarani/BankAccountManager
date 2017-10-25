import datetime

history = {}

class Account(object):
	def __init__(self):

		self.pin = 10000
		self.balance = 0

	
	def check_code(self, value):

		return self.pin == value



	def deposit(self):
		attempts = 4
		while attempts > 0:
			value = int(input("please insert your pin attempts remaining {} {}".format(attempts, ">") ))

			if self.check_code(value):
				amount = int(input("please input the amount you want to deposit> "))
				self.balance += amount
				history[str(datetime.datetime.now())] = 'deposited {}'.format(amount)
				print("your account has been credited with {}".format(amount))

				break

			else:
				print("wrong pin please try a gain")


			attempts -= 1

			if attempts == 0:

				print("you have entered the wrong pin 4 times, your acoount \n has been blocked\
				 contact customer care for \n assistance ")

				break

	def widhthraw(self):
		attempts = 4
		while attempts > 0:
			value = int(input("please insert your pin attempts remaining {} {}".format(attempts, ">")))

			if self.check_code(value):
				amount = int(input("please input the amount you want to widhthraw> "))
				if amount <= self.balance:
					self.balance -= amount
					history[str(datetime.datetime.now())] = 'widhthraw {}'.format(amount)
					print("your account has been debited with {}". format(amount))
                
					break

				else:
					print("dear customer your acount balance is insufficient\
					 to make this transaction \n you balance is {}   ".format(balance))

			else:
				print("wrong pin please try again")

			attempts -= 1

			if attempts == 0:

				print("you have entered the wrong pin 4 times, \n your accouunt has \
				 been blocked please contact customer care \n for assistance")
                
				break

	def check_balance(self):

		return print(self.balance)

	def bank_statement(self):

		return print(history)

larry= Account()
larry.deposit()
larry.widhthraw()
larry.check_balance()
larry.bank_statement()