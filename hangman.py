import random
def hangman(word):
	wrong=0
	stages=["",
	        "_________         ",
	        "|                 ",
		"|        |        ",
		"|        O        ",
		"|       /|\       ",
		"|       / \       ",
                "|                 ",
		]
	rletters=list(word)
	board=["_"]*len(word)
	win=False
	print("Welcom HangMan!!")
	while wrong<len(stages)-1:
		print("\n")
		msg="１文字を予想してね\n(Guess one character of the word)"
		char=input(msg)
		if char in rletters:
			cind=rletters.index(char)
			board[cind]=char
			rletters[cind]="$"
		else:
			wrong+=1
		print(" ".join(board))
		e=wrong+1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print("You are winner!!")
			print(" ".join(board))
			win=True
			break
	if not win:
		print("\n".join(stages[0:wrong+1]))
		print("You are loser, The right answer is {}.".format(word)) 

animals=["dog","cat","pig","bird","turtle"]
hangman(random.choice(animals))

