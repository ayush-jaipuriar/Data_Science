import random 

while True: 
	print("Enter userChoice \n 1. Rock \n 2. paper \n 3. scissor \n") 
	userChoice = int(input("Your turn: ")) 
	while userChoice > 3 or userChoice < 1: 
		userChoice = int(input("enter valid input: ")) 
		
	if userChoice == 1: 
		choice_name = 'Rock'
	elif userChoice == 2: 
		choice_name = 'paper'
	else: 
		choice_name = 'scissor'
		
	print("Your userChoice is: " + choice_name) 
	print("\nNow the CPU will play") 
	
	comp_choice = random.randint(1, 3) 

	while comp_choice == userChoice: 
		comp_choice = random.randint(1, 3) 

	if comp_choice == 1: 
		comp_choice_name = 'Rock'
	elif comp_choice == 2: 
		comp_choice_name = 'paper'
	else: 
		comp_choice_name = 'scissor'
		
	print("Computer userChoice is: " + comp_choice_name) 

	print(choice_name + " V/s " + comp_choice_name) 

	if((userChoice == 1 and comp_choice == 2) or
	(userChoice == 2 and comp_choice ==1 )): 
		print("paper wins => ", end = "") 
		result = "paper"
		
	elif((userChoice == 1 and comp_choice == 3) or
		(userChoice == 3 and comp_choice == 1)): 
		print("Rock wins =>", end = "") 
		result = "Rock"
	else: 
		print("scissor wins =>", end = "") 
		result = "scissor"

	if result == choice_name: 
		print("<== User wins ==>") 
	else: 
		print("<== Computer wins ==>") 
		
	print("Do you want to play again? (Y/N)") 
	ans = input() 
	if ans == 'n' or ans == 'N': 
		break


