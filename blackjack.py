import random #used to generate random numbers for card dealing.
import time #time.sleep is used while dealing is happening to add suspense.

hand_number = 1
card1 = 0
card2 = 0
total = 0
blackjack = False
answer = "none"
dealertotal = 0
cash = 100
bet = 0
quit = False
			
#Defining functions

#Double down option is triggered after player's initial hand.
#Double down doubles the player's bet, and player is dealt a single additional card.
def double():

	global total
	global dealertotal
	answer = input("Double? (Y/N)")

	if answer == "y": #Player accepts double down
		deal_card()
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

	elif answer == "n": #Player declines double down
		hit()
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

	else: #Player entered an invalid input
		print ("Please answer y or n")
	
#Hit - Player is offered another card.
def hit():
	global total
	global cash
	while total < 21:	
		answer = input("Buy? (Y/N)")
		if answer == "y":
			deal_card()
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

#deal_card is triggered if the player accepts an additional card.
def deal_card():
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

#dealerdraw is triggered if the player decides to Stay.
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

#Player wins the hand.
def win():
	global cash
	global bet
	print ("You win!")
	prize = int(bet) * 2				#Win pays out 2:1 odds.
	print ("You won: $" + str(prize))
	cash = int(cash) + int(prize)		#Adding winnings to player's cash total.
	return

#Player loses the hand.
def lose():
	global cash
	global bet
	print ("You lose.")
	cash = int(cash) - int(bet)			#Removing losing bet from player's cash total.
	return	
		
#GAME START		

print ("Welcome to Blackjack. Aces will be High.")

while quit == False: #At the end of each hand, player is asked if they want to Quit.
	
	print ("Money: $" + str(cash))
	bet = input ("Enter your bet: $")

	#Initial hand is dealt.
	if int(bet) > cash: #Prints error and returns to bet input.
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
		
		card1 = random.randint(2,14) #Random numbers are generated for each card.
		card2 = random.randint(2,14)
		card3 = random.randint(2,14)
		
		dealertotal = card3

		print ("Your cards are: ", end='')

		#Prints player's first card as number or J/Q/K/Q if applicable.
		if card1 < 11:
			print (str(card1) + ", ", end='')
		elif card1 == 11:
			print ("A, ", end='')
		elif card1 == 12:
			print ("J, ", end='')
			card1 = 10
		elif card1 == 13:
			print ("Q, ", end='')
			card1 = 10
		elif card1 == 14:
			print ("K, ", end='')
			card1 = 10

		#Prints player's second card as number or J/Q/K/Q if applicable.
		if card2 < 11:
			print (card2)
		elif card2 == 11:
			print ("A")
		elif card2 == 12:
			print ("J")
			card2 = 10
		elif card2 == 13:
			print ("Q")
			card2 = 10
		elif card2 == 14:
			print ("K")	
			card2 = 10

		#Triggers a hand win for the player after the dealer's card is shown.
		if card1 + card2 == 21:
			blackjack = True
		
		 #Print total of player's cards.
		total = card1 + card2
		print ("Total: " + str(total))
		
		#Prints player's second card as number or J/Q/K/Q if applicable.
		print ("Dealer drew: ", end='') 
		if card3 < 11:
			print (card3)
		elif card3 == 11:
			print ("A")
		elif card3 == 12:
			print ("J")
			card3 = 10
		elif card3 == 13:
			print ("Q")
			card3 = 10
		elif card3 == 14:
			print ("K")	
			card3 = 10

	#Initial hand dealing is complete.
	#Possible options are Blackjack, Split, Double, Hit.

	if blackjack == True:
		print ("BLACKJACK! You win!")
		prize = (int(bet)) + (int(bet) * 1.5)				#Blackjack pays out 3:2 odds.
		print ("You won: $" + str(prize))					
		cash = (int(cash) + int(bet)) + (int(bet) * 1.5)	#Adding winnings to player's cash total.
		blackjack = False

	else:
		if card1 == card2:
			answer = input("Split? (Y/N) ")
			if answer == "y":
				print ("SPLIT") #I still need to code for this condition.
			elif answer == "n":
				double()
			else:
				print ("Please answer y or n ")
		else:		
			if 8 <= total <= 12:
				double()
			else:		
				hit()	

	#player input for the current hand is over.

	if total > 21:
		print ("Bust!")
		cash = int(cash) - int(bet)
	elif total == 21:
		print ("21!")
		dealerdraw()
		
	#Hand is over.	

	print ("Money: $" + str(cash))
	answer = input("Another hand? (Y/N) ")
	if answer == "y":
		continue
	elif answer == "n":
		print("Game over.")
		quit = True
	else:
		print ("Please answer y or n ")