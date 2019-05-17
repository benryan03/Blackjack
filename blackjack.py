import random
import time
hand_number = 1
number1 = 0
number2 = 0
total = 0
blackjack = False
answer = "none"
dealertotal = 0
cash = 100
bet = 0
quit = False

def deal():
	global total
	print()
	print ("Dealing.")
	time.sleep(1)
	print ("Dealing..")
	time.sleep(1)
	print ("Dealing...")
	time.sleep(1)
	number = random.randint(2,14)

	print ("You were dealt: ", end='')
	if number < 11:
		print (str(number))
	elif number == 11:
		print ("A")
	elif number == 12:
		print ("J")
		number = 10
	elif number == 13:
		print ("Q")
		number = 10
	elif number == 14:
		print ("K")
		number = 10

	total = total + number
	print ("Total: " + str(total))
	
def buy():
	global total
	global cash
	while total < 21:	
		answer = input("Buy? (Y/N)")
		if answer == "y":
			deal()
		elif answer == "n":
			dealerdraw()
			if dealertotal > 21:
				print ("Dealer busted!")
				win()
			elif dealertotal <= 20:
				if total > dealertotal:
					win()
				else:
					lose()
			elif dealertotal == 21:
				print ("Tie!")
				return
			return
		else:
			print ("Please answer y or n")
			
def double():
	global total
	global dealertotal
	answer = input("Double? (Y/N)")
	if answer == "y":
		deal()
		if total > 21:
			print ("Bust!")
			lose()		
		else:	
			dealerdraw()
			if dealertotal > 21:
				print ("Dealer busted!")
			elif dealertotal < 21:
				win()
			else:
				print ("Tie!")	
	elif answer == "n":
		buy()
		if total == 21:
			dealerdraw()
			if dealertotal > 21:
				print ("Dealer busted!")
			elif dealertotal < 21:
				win()
			else:
				print ("Tie!")	
		elif total < 21:
			dealerdraw()
			if dealertotal > 21:
				print ("Dealer busted!")
			elif dealertotal < 21:
				if total > dealertotal:
					win()
				else:
					lose()		
	else:
		print ("Please answer y or n")
	
def dealerdraw():
	global dealertotal
	while dealertotal < 17:	
		number = random.randint(2,14)
		dealertotal = dealertotal + number
		print()
		print ("Dealing.")
		time.sleep(1)
		print ("Dealing..")
		time.sleep(1)
		print ("Dealing...")
		time.sleep(1)
		print ("Dealer drew: ", end='')
		if number < 11:
			print (number)
		elif number == 11:
			print ("A")
		elif number == 12:
			print ("J")
			number = 10
		elif number == 13:
			print ("Q")
			number = 10
		elif number == 14:
			print ("K")	
			number = 10
		print ("Dealer total: " + str(dealertotal))
	
def win():
	global cash
	global bet
	print ("You win!")
	prize = int(bet) * 2
	print ("You won: $" + str(prize))
	cash = int(cash) + int(prize)
	return
	
def lose():
	global cash
	global bet
	print ("You lose.")
	cash = int(cash) - int(bet)
	return	
		
#GAME START		

print ("Welcome to Blackjack. Aces will be High.")

while quit == False:		
	
	print ("Money: $" + str(cash))
	bet = input ("Enter your bet: $")
	if int(bet) > cash:
		print("You cannot bet more money than you have.")
		continue
	else:
	
		print()
		print ("Dealing.")
		time.sleep(1)
		print ("Dealing..")
		time.sleep(1)
		print ("Dealing...")
		time.sleep(1)
		
		number1 = random.randint(2,14)
		number2 = random.randint(2,14)
		number3 = random.randint(2,14)
		
		dealertotal = number3

		print ("Your cards are: ", end='')
		if number1 < 11:
			print (str(number1) + ", ", end='')
		elif number1 == 11:
			print ("A, ", end='')
		elif number1 == 12:
			print ("J, ", end='')
			number1 = 10
		elif number1 == 13:
			print ("Q, ", end='')
			number1 = 10
		elif number1 == 14:
			print ("K, ", end='')
			number1 = 10
			
		if number2 < 11:
			print (number2)
		elif number2 == 11:
			print ("A")
		elif number2 == 12:
			print ("J")
			number2 = 10
		elif number2 == 13:
			print ("Q")
			number2 = 10
		elif number2 == 14:
			print ("K")	
			number2 = 10

		if number1 + number2 == 21:
			blackjack = True
		
		total = number1 + number2
		print ("Total: " + str(total))
		
		print ("Dealer drew: ", end='')
		if number3 < 11:
			print (number3)
		elif number3 == 11:
			print ("A")
		elif number3 == 12:
			print ("J")
			number3 = 10
		elif number3 == 13:
			print ("Q")
			number3 = 10
		elif number3 == 14:
			print ("K")	
			number3 = 10

	if blackjack == True:
		print ("BLACKJACK! You win!")
		prize = (int(bet)) + (int(bet) * 1.5)
		print ("You won: $" + str(prize))
		
		cash = (int(cash) + int(bet)) + (int(bet) * 1.5)
		blackjack = False

	elif blackjack == False:
		if number1 == number2:
			answer = input("Split? (Y/N) ")
			if answer == "y":
				print ("SPLIT")
			elif answer == "n":
				double()
			else:
				print ("Please answer y or n ")
		else:		
			if 8 <= total <= 12:
				double()
			else:		
				buy()	
	if total > 21:
		print ("Bust!")
		cash = int(cash) - int(bet)
	elif total == 21:
		print ("21!")
		dealerdraw()
		
		
	print ("Money: $" + str(cash))
	answer = input("Another hand? (Y/N) ")
	if answer == "y":
		continue
	elif answer == "n":
		print("Game over.")
		quit = True
	else:
		print ("Please answer y or n ")











