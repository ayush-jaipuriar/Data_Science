inputString = input("Enter a sentence : ")
alphabet =  digit = 0
for char in inputString:
	if (char.isalpha()):
		alphabet+=1
	elif (char.isdigit()):
		digit+=1
print("The count of alphabets in sentence : ", alphabet)
print("The count of digits in sentence : ", digit)
