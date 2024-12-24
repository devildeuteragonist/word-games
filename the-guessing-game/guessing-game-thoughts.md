# some thoughts on a theoretical word game 

## goal of the word game/about
it's gonna be like 20 questions or charades but stupider. 
i'm going to see if i can try to formulate some logic that would allow me to play a fun word game with the computer if i'm bored out of my mind. 
the aim: computer 'thinks' of a word. this word is concealed from the player, but the player must guess. 
- the computer says something like, 'i'm thinking of a word that begins with the letter c.' and then the human has to guess what that is.
- human guess incorrectly? the computer gets a point, but it gives another letter hint. 
- it'd basically be like wordle but with a points system: for every letter you guess correctly without help from the 'puter, you get a point; for every letter you guess incorrectly, the 'puter gets a point
- maybe you'd have a limit on the number of rounds so that the game has a definite end and clear winner or loser at the end 
- this is very stream of consciousness; i am too tired right now to write my thoughts in a cohesive manner 

## coding logic 
- import a massive library of words into your coding notebook, but the words have to be easy enough to be fair in a guessing game (maybe top 1000 words in human vocabulary 3 letters or longer)
	- the words that meet our criteria can either be sifted out through the library, or we could find a good enough library
- computer randomly selects the word. 
- computer provides hint: 'i'm thinking of a [length of word] letter word beginning with the letter [first letter of word]
- player: provides input
	- if player guesses right, or guesses a set of letters right: computer will display the spaces in the word where the player got letters right, as well as blanks for where the player did not get the right letters (kinda like hangman) 
	- if the player guesses wrong, the computer prompts another hint  
- for each turn the player gets something right: 1 point for each correct letter
- for each turn the player does not get anything right: 1 point for the computer 
- game will keep going up until player finally guesses word
- points will be tallied

yeah i'll clean this up somehow at some point soon. i'm thinking i'll write the game in python or something and it can be played directly from a colab notebook or something