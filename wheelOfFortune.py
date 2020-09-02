import re, random

def main():
    vowels = ['A', 'E', 'I', 'O', 'U'] #these first 4 variable are used in many methods
    used_consonants = []
    used_vowels = []
    total = 0 #money player has
    phrase = select_phrase() #call method and return phrase
    coded_phrase = code_phrase(phrase) 
    print('Let\'s play Wheel of Fortune! You will be given a coded phrase. Spin and select a consonant.')
    print('Consonant in phrase means you keep the money.')
    print('Vowels can be purchased for $1000 each.')
    print()
    print(f'Here is your mystery phrase: {coded_phrase}')
    print()
    spin_wheel(phrase, coded_phrase, vowels, total, used_consonants,used_vowels) #call method and return dollar value

def select_phrase():
    phrases = ['No news is good news', 'An apple a day keeps the doctor away', 
    'A friend in need is a friend indeed','A fool and his money are soon parted', 'Haste makes waste', 
    'Curiosity killed the cat']  #could add more here
    # randomly select from array of phrases
    phrase = random.choice(phrases) #info from https://pynative.com/python-random-choice/-select random from a list
    phrase = phrase.upper()  #make phrase upper for simpler comparison later (and since Wheel of Fortune uses all caps)
    return phrase

def code_phrase(phrase):
    # show user blanks so they know how many letters and spacing- let * represent letters
    coded_phrase = re.sub('[A-Za-z]', '*', phrase) #regex sub * for each letter in phrase
    return coded_phrase

def spin_wheel(phrase, coded_phrase, vowels, total, used_consonants,used_vowels):
    dollars = [0,500,600,700,800,900] #when user spins wheel, these values are options
    dollar = random.choice(dollars) #randomly chose dollar amount from above list
    print(f'The wheel landed on ${dollar}.')
    user_guess(phrase, coded_phrase, dollar, vowels, total, used_consonants,used_vowels) #call method below
    return dollar

def user_guess(phrase, coded_phrase, dollar, vowels, total, used_consonants, used_vowels):
    letter =input('Guess a consonant that you think is in the phrase ->  ')
    
    if letter.isalpha() and letter.upper() not in vowels: #validation that user entered a letter that is not a vowel
        letter = letter.upper()
    else:
        print('That is not a valid consonant')
        user_guess(phrase, coded_phrase, dollar, vowels, total,user_guess,used_vowels) #go back to top of method
    
    if letter in used_consonants: #see it letter has already been guessed - is it in the list
        print('You have already selected that consonant. Select another. ')
        user_guess(phrase, coded_phrase, dollar, vowels, total, used_consonants, used_vowels) #call method again 
        
    if letter in phrase:
        total+= dollar  #add $ to contestant's total
        print(f'Yes - that letter is in the phrase! You now have ${total}')
        used_consonants.append(letter) # add to list of cons. already chosen
        coded_phrase = update_coded_phrase(letter, phrase, coded_phrase, total) #call method below to update the phrase w/ letter
        guess_phrase(phrase, total, dollar, vowels, coded_phrase, used_consonants, used_vowels)  #give option to guess the phrase
    else:
        print('Sorry - that letter is not in the phrase')
        buy_or_spin(total, dollar, vowels, phrase, coded_phrase,used_consonants, used_vowels)
        
    return used_consonants

def buy_or_spin(dollar, total, vowels, phrase, coded_phrase, used_consonants, used_vowels):
   
    if total>=1000:

        buyOrSpin = input('Do you want to purchase a vowel or spin for a consonant?  Enter V or C')
        if buyOrSpin.upper() == 'V' and total>=1000:
            buy_vowel(total, vowels, phrase, coded_phrase,dollar,used_consonants, used_vowels)  #go to this method
        elif buyOrSpin.upper() =='V' and total<1000: 
            print('Sorry, you do not have enough money for a vowel. Try another consonant instead. ')
            spin_wheel(phrase, coded_phrase, vowels, total, used_consonants,used_vowels)
        elif buyOrSpin.upper() == 'C':
            spin_wheel(phrase, coded_phrase, vowels, total, used_consonants,used_vowels)
        else:
            print('Please enter either V or C')
            buy_or_spin(dollar, total, vowels, phrase, coded_phrase, used_consonants, used_vowels)#return to top of method
    else:
        spin_wheel(phrase, coded_phrase, vowels, total, used_consonants, used_vowels)


def buy_vowel(total, vowels, phrase, coded_phrase,dollar, used_consonants, used_vowels):
    print(f'Your current balance is ${total}')
    vowel_cost = 1000
    if total>=1000:
        letter = input('You may purchase a vowel for $1000.  Select a vowel - >  ')
        letter = letter.upper()
        if letter not in vowels: # if they select a consonant or some other character
            print('Sorry, that is not a vowel') #then return to top of method
            buy_vowel(total, vowels, phrase, coded_phrase,dollar, used_consonants, used_vowels)
        if letter in used_vowels: #letter already selected
            print('Sorry, you have already selected that vowel')
            buy_vowel(total,vowels, phrase, coded_phrase, dollar, used_consonants, used_vowels) #back to top of method
        elif letter in phrase:
            total = total - vowel_cost #subtract cost of a vowel from total
            used_vowels.append(letter) #add vowel to the used list
            print(f'Yes! That letter is in the phrase. Your new balance is ${total}')
            coded_phrase = update_coded_phrase(letter, phrase, coded_phrase, total) #update the coded phrase with the vowel
            guess_phrase(phrase, total, dollar, vowels, coded_phrase, used_consonants, used_vowels)  
        else: #letter is not in phrase
            total = total-vowel_cost #subtract cost of vowel from total
            used_vowels.append(letter) #add to list already chosen
            print('Sorry, that vowel is not in the phrase')
            print(f'Your current balance is ${total}') 
            buy_or_spin(dollar, total, vowels, phrase, coded_phrase, used_consonants, used_vowels) #give option of buying another vowel or selecting a consonant
           
    return letter, total, coded_phrase, used_vowels

def update_coded_phrase(letter ,phrase, coded_phrase, total):
    iterator= re.finditer(letter, phrase) #finditer -Find all substrings where the RE matches, and returns them 
    #as an iterator. from https://docs.python.org/3/howto/regex.html
    #https://stackoverflow.com/questions/2674391/python-locating-the-position-of-a-regex-match-in-a-string/16360404
    indices = [m.start(0) for m in iterator] #make a list of the start indices where the letter is found
    
    #replace the * at those indices with the letter
    for i in indices:  #loop through indices 
    #make str a list; replace the letter at the index; join list back into a string
    #https://pythonexamples.org/python-string-replace-character-at-specific-position/
        temp = list(coded_phrase)
        temp[i] = letter
        coded_phrase = "".join(temp)
    print(f' Here is the revised phrase with your letter revealed {coded_phrase}')
    print() #blank line for ease in reading
    #if user has guessed all letters
    if coded_phrase.replace(" ", "") == phrase.replace(" ", ""):
        print(f'You have completed the phrase! You have ${total}')
        play_again(total)
    return coded_phrase

def guess_phrase(phrase, total, dollar, vowels,coded_phrase,used_consonants, used_vowels):
    want_to_guess_phrase = input('Would you like to guess the phrase? Enter Y or N')
    if want_to_guess_phrase.upper() == 'Y':
        total_guess =input('Enter you guess for the whole phrase ->  ')
        #remove all spaces in total_guess for simpler comparison
        if total_guess.replace(" ", "").upper() == phrase.replace(" ", "").upper():
            print('Congratulations! You correctly identified the phrase!')
            print(f'You have ${total} in the bank')
            play_again(total)
        else:
            print('Sorry, that is not correct')
            buy_or_spin(dollar, total, vowels, phrase, coded_phrase,used_consonants, used_vowels) #send user back to get a V or C
    elif want_to_guess_phrase.upper() == 'N':
        buy_or_spin(dollar, total, vowels, phrase, coded_phrase,used_consonants, used_vowels)
    else:
        print('Not a valid input') #call method again
        guess_phrase(phrase, total, dollar, vowels, coded_phrase, used_consonants, used_vowels)

def play_again(total):
    again = input('Would you like to play the game again?')
    again = again.upper()   #send to main to start again and clear lists if Y                                                              #is they typed in a letter other than Y or N
    main() if again=='Y' else print(f'You won ${total}! Have a nice day.') if again =='N' else play_again(total) #learned how to do ternary in codeWars
    
main() #call main function