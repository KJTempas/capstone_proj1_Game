import re, random

def main():
    vowels = ["A", "E", "I", "O", "U"]
    total = 0 #money for player
    phrase = select_phrase() #call method and return phrase
    coded_phrase = code_phrase(phrase) 
    print('Let\'s play Wheel of Fortune! You will be given a coded phrase. Spin and select a consonant.')
    print('Consonant in phrase means you keep the money.')
    print('Vowels can be purchased for $1000 each.')
    print()
    print(f'Here is your mystery phrase: {coded_phrase}')
    spin_wheel(phrase, coded_phrase, vowels, total) #call method and return dollar value
   # user_guess(phrase, coded_phrase, dollar, vowels, total)


def select_phrase():
    phrases = ["No news is good news"]#, "An apple a day keeps the doctor away", 
   # "A friend in need is a friend indeed"] #add these back after rest running
    # randomly select from array of phrases
    phrase = random.choice(phrases) #info from https://pynative.com/python-random-choice/-select random from a list
    print(phrase)
    #example phrase for initial testing
    #phrase = "No news is good news"
    phrase = phrase.upper()  #make phrase upper for simpler comparison later (and since Wheel of Fortune uses all caps)
    return phrase

def code_phrase(phrase):
    # show user blanks so they know how many letters and spacing- let * represent letters
    coded_phrase = re.sub('[A-Za-z]', '*', phrase)
    #print(coded_phrase) 
    return coded_phrase

def spin_wheel(phrase, coded_phrase, vowels, total):
    dollars = [0,500,600,700,800,900]
    dollar = random.choice(dollars)
    print(f'The wheel landed on ${dollar}.')
    user_guess(phrase, coded_phrase, dollar, vowels, total) #call method below
    return dollar

def user_guess(phrase, coded_phrase, dollar, vowels, total):
    #total = 0
    used_consonants = []
    letter =input('Guess a consonant that you think is in the phrase ->  ')
    if letter.isalpha() and letter not in vowels: #validation that user entered a letter that is not a vowel
        letter = letter.upper()
    else:
        print('That is not a valid consonant')
        user_guess(phrase, coded_phrase, dollar, vowels, total) #go back to top of method
    if letter in used_consonants:
        print('You have already selected that consonant. Select another. ')
        user_guess(phrase, coded_phrase, dollar, vowels, total) #call method again 
        
    if letter in phrase:
        total+= dollar  #add $ to contestant's total
        print(f'Yes - that letter is in the phrase! You now have ${total}')
        used_consonants.append(letter) # add to list of cons. already chosen
        print('used cons list', used_consonants)
        coded_phrase = update_coded_phrase(letter, phrase, coded_phrase) #call method below to update the phrase w/ letter
        guess_phrase(phrase, total, dollar, vowels, coded_phrase)  #give option to guess the phrase
    else:
        print('Sorry - that letter is not in the phrase')
        buy_or_spin(total, dollar, vowels, phrase, coded_phrase)
    return used_consonants

def buy_or_spin(dollar, total, vowels, phrase, coded_phrase):
    #determine if enough money and only ask if have >1000
    if total>=100:

        buyOrSpin = input('Do you want to purchase a vowel or spin for a consonant?  Enter V or C')
        if buyOrSpin.upper() == 'V' and total>=1000:
            buy_vowel(total, vowels, phrase, coded_phrase)  #go to this method
        elif buyOrSpin.upper() =='V' and total<1000: 
            print('Sorry, you do not have enough money for a vowel. ')
            spin_wheel(phrase, coded_phrase, vowels, total)
        elif buyOrSpin.upper() == 'C':
            spin_wheel(phrase, coded_phrase, vowels, total)
        else:
            print('Please enter either V or C')
            buy_or_spin(dollar, total, vowels, phrase, coded_phrase)#return to top of method


def buy_vowel(total, vowels, phrase, coded_phrase):
    print(f'Your current balance is ${total}')
    #vowels = ["A", "E", "I", "O", "U"]
    used_vowels = []
    print('used vowels', used_vowels)
    vowel_cost = 1000
    if total>=1000:
        letter = input('You may purchase a vowel for 1000.  Select a vowel - >  ')
        letter = letter.upper()
        if letter in used_vowels:
            print('Sorry, you have already selected that vowel')
            buy_vowel(total,vowels, phrase, coded_phrase) #back to top of method
        else:
            total = total - vowel_cost
            used_vowels.append(letter)
            update_coded_phrase(letter, phrase, coded_phrase)
    
    return letter, total, coded_phrase


def update_coded_phrase(letter ,phrase, coded_phrase):
    print(letter) 
    iterator= re.finditer(letter, phrase) #finditer -Find all substrings where the RE matches, and returns them 
    #as an iterator. from https://docs.python.org/3/howto/regex.html
    #https://stackoverflow.com/questions/2674391/python-locating-the-position-of-a-regex-match-in-a-string/16360404
    indices = [m.start(0) for m in iterator] #make a list of the start indices where the letter is found
    print(indices)#works - gives [array of ints][0,3,16]
    
    #replace the * at those indices with the letter
    for i in indices:  #loop through indices 
    #make str a list; replace the letter at the index; join list back into a string
    #https://pythonexamples.org/python-string-replace-character-at-specific-position/
        temp = list(coded_phrase)
        temp[i] = letter
        coded_phrase = "".join(temp)
    print(f' Here is the revised phrase with your letter revealed {coded_phrase}')
    
    return coded_phrase

def guess_phrase(phrase, total, dollar, vowels,coded_phrase):
    want_to_guess_phrase = input('Would you like to guess the phrase? Enter Y or N')
    if want_to_guess_phrase.upper() == 'Y':
        total_guess =input('Enter you guess for the whole phrase ->  ')
        #remove all spaces in total_guess to simpler comparison
        print(total_guess)
        total_guess_no_space = total_guess.replace(" ", "").upper()
        print(total_guess_no_space)
        phrase_no_space = phrase.replace(" ", "")
        print(phrase_no_space)
        if total_guess_no_space == phrase_no_space:
            print('Congratulations! You correctly identified the phrase!')
            print(f'You have ${total} in the bank')
            play_again(total)
        else:
            print('Sorry, that is not correct')
            #user_guess(phrase, code_phrase, dollar, vowels, total) #call method to allow another letter guess
            buy_or_spin(dollar, total, vowels, phrase, coded_phrase) #send user back to get a V or C
    else:
        buy_or_spin(dollar, total, vowels, phrase, coded_phrase)

def play_again(total):
    again = input('Would you like to play the game again?')
    again = again.upper()
    main() if again=='Y' else print(f'You won ${total}! Have a nice day') #learned how to do ternary in codeWars
    


main() #call main function