import random

print('starting the game of hangman ...')


def game_start_home():
    global attempts
    print('')
    attempts=(input('how many incorrect attempts do you want ?[1-25] '))
    while attempts not in [str(x) for x in range(1,26)]:
        print(attempts , 'is not between [1-25]')
        attempts=(input('how many incorrect attempts do you want ?[1-25] '))
    
def word_selection():
    global hidden_ver_of_given_word
    global word_given
    
    print( '  ')
    word_length=attempts
    '''input('what is the minimum word length do you want ? [1-14]')
    while word_length not in [str(x) for x in range(1,15)]:
        print(word_length, 'not in between [1-14]')
        word_length=input('what is the minimum word length do you want ? [1-14]')'''
    print('selecting a word ...')
    words_list_file=open('words.txt','r')
    h=words_list_file.read()
    words_list_file.close()
    h=h.split(',')
    word_length_words_list=[]
    for i in h:
        if len(i)>=9:
            word_length_words_list.append(i)

    word_given=random.choice(word_length_words_list)
    word_given_length=len(word_given)
    word_given=word_given.lower()
    
    
    hidden_ver_of_given_word='*'*word_given_length


def game_start():
    global hidden_ver_of_given_word
    global word_given
    global attempts
    attempts=int(attempts)
    print('word :',hidden_ver_of_given_word)
    print('attempts remaining : ', attempts)
    print('')
    guessed_letter=input('guess the letter : ')
    
    while attempts !=1:
     if '*' not in hidden_ver_of_given_word:
         print('hurry !! you won ')
         another_game()
        
     if guessed_letter in word_given:
        print(guessed_letter, 'is in the word ! :)')
        hidden_ver_of_given_word_list=list(hidden_ver_of_given_word)
        hidden_ver_of_given_word=''
        for i in range(len(word_given)):
            if guessed_letter ==word_given[i]:
                hidden_ver_of_given_word_list[i]=guessed_letter

        for j in hidden_ver_of_given_word_list:
            hidden_ver_of_given_word+=j

     else:
        print(guessed_letter,'is not in the word')
        attempts-=1
        
     print('word :',hidden_ver_of_given_word)
     print('attempts remaining : ', attempts)
     print('')
     guessed_letter=input('guess the letter : ')
     

    if '*' in hidden_ver_of_given_word:
        print('oh ohoo !! you loose the game ')
        print ('the word is' , word_given)
        another_game()

    else :
        print('hurray !!! you won ')
        another_game()

def another_game():
    another_game =input('do you want to play another game ? [y/n]')
    if another_game == 'y':
        game_start_home()   
        word_selection()
        game_start()

    else:
        print('thanks for playing !!!')
        exit()
                
        
    
    
    
game_start_home()   
word_selection()
game_start()

    



    

