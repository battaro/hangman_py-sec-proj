#importing the random external module
import random
#importing the scripts
import hangman_art
import hangman_words

#here i print the hangman logo taken from the external module
print(hangman_art.logo)

#here i putted all vars we will use it on the program
stages = list(hangman_art.stages) #new list from stages, the pictures on the game (go to the hangman_art.py to know exactly what i mean)
word_list = list(hangman_words.word_list) #new list from all words we will use in the game (go to hangman_words.py to know exactly what i mean)
chosen_word = random.choice(word_list) #picking a random word from the list in (hangman_words.word_list)
isWin = False # bollean var will help us on the loop
word_on_list = [] #list have the words on the (chosen_word)
guessed_letters = [] #list will contain the guessed letter so as not to wrong the player
lives = 6 #if the player guessed wrong letter we will take away from this 1 live

#making the word_on_list like (_,_,_,_,) as number of characters present
for _ in range(len(chosen_word)):
    word_on_list += "_"

#The game 
#Update -- i forget to write (not) on isWin lol 
while not isWin and lives > 0: #if the player didn't win and the lives stay greater than zero stay on the game
    
    guess = input("Guess a letter: ").lower() #input the guess letter 

    #for loop to check if the guessed letter can be on the (word_on_list)
    for number_of_letter_on_the_list in range(len(chosen_word)): 
        #if the number¹ letter on the (chosen_word) equal to the guessed letter put the letter on the (word_on_list) on the same place
        #number¹ is the (number_of_letter_on_the_list) from 0 to number no body no it because maybe gonna be 3,4,5,6,7,8...
        if chosen_word[number_of_letter_on_the_list] == guess: 
            word_on_list[number_of_letter_on_the_list] = guess
            
    #if the player guess a same letter tow times
    if guess in guessed_letters:
        print(f"You\'ve already guessed {guess}") 
        print(f"{' '.join(word_on_list)} \n") #make the word like this : from [_pp_e] to _ p p _ e 
        print(stages[lives]) #print the stage we have reached
        
    #if the guess on the chosen_word print the new (word_on_list) we got
    elif guess in chosen_word:
        print(f"{' '.join(word_on_list)} \n")

    #if the guess not on  chosen_word do this
    elif guess not in chosen_word:
        print(f"You guessed {guess}, that\'s not in the word. You Lose a life. " +"\n") 
        print(f"{' '.join(word_on_list)} \n")
        lives -= 1 #take away from the lives just one of them
        print(stages[lives]) 

    #take away from the lives just one of them
    if "_" not in word_on_list:
        isWin = True #making the win true to stop the while loop i mean (game)
        print(f"the word is {chosen_word} You Win")
        
    #If the lives become zero, the player guessed too many incorrect letters and this means that he was hanged and lost ! 
    if lives <= 0:
        print(f"the word is {chosen_word} You Lost")
        
    guessed_letters.append(guess) #adding the old letter we guessed to to the (guessed_letters) list

#IDK if this is the best way to make a hangman game but put this in ur mind 
#i programmed this cute program in 3 hour and just in 7 days of learning python
#u can use my code when u want and as u need not matter with me but...
#Game Developed by (Brimo Battaro) :O
