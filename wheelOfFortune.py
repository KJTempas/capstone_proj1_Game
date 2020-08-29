import re, random

def main():
    vowels = ["A", "E", "I", "O", "U"]
    phrase = select_phrase() #call method and return phrase
    coded_phrase = code_phrase(phrase) 
    print('Let\'s play Wheel of Fortune! You will be given a coded phrase. Spin and select a consonant.')
    print('Consonant in phrase means you keep the money.')
    print('Vowels can be purchased for $1000 each.')
    print()
    print(f'Here is your mystery phrase: {coded_phrase}')
    dollar = spin_wheel() #call method and return dollar value
    user_guess(phrase, coded_phrase, dollar, vowels)


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
    coded_phrase = re.sub('[A-Za-z]', 'X', phrase)
    #print(coded_phrase) 
    return coded_phrase

def spin_wheel():
    dollars = [0,500,600,700,800,900]
    dollar = random.choice(dollars)
    print(f'The wheel landed on {dollar}. You get to keep this money if you correctly guess a consonant.')
    return dollar

def user_guess(phrase, coded_phrase,dollar, vowels):
    total = 0
    used_consonants = []
    letter =input('Guess a consonant that you think is in the phrase ->  ')
    if letter.isalpha() and letter not in vowels: #validation that user entered a letter that is not a vowel
        letter = letter.upper()
    else:
        print('That is not a valid consonant')

    if letter in used_consonants:
        print('You have already selected that consonant. Select another. ')
        #user_guess(phrase, code_phrase, dollar) #call method again - or should I say return?
        return
    if letter in phrase:
        print('Yes - that letter is in the phrase!')
        total+= dollar  #add $ to contestant's total
        #modify coded phrase to add letter
        used_consonants.append(letter)
        print('uc', used_consonants)
        update_coded_phrase(letter, phrase, coded_phrase) #call method below sending it 3 parameters
        guess_phrase(phrase) 
    else:
        print('Sorry - that letter is not in the phrase')
        buyOrSpin(dollar)
        
def buyOrSpin(dollar):
    buyOrSpin = input('Do you want to purchase a vowel or spin for a consonant?  Enter V or C')
    if buyOrSpin.upper() == 'V':
        buyVowel(dollar)
    elif buyOrSpin.upper() == 'C':
        spin_wheel()
    else:
        print('Please enter either V or C')
        buyOrSpin(dollar)


def buyVowel(dollar, total, vowels):
    print(f'Your current balance is ${dollar}')
    #vowels = ["A", "E", "I", "O", "U"]
    used_vowels = []
    vowel_cost = 1000
    if total>1000:
        letter = input('You may purchase a vowel for 1000.  Select a vowel - >  ')
        if letter in used_vowels:
            print('Sorry, you have already selected that vowel')
            buyVowel(dollar, total,vowels)
        else:
            total = total - vowel_cost
            used_vowels.append(letter)
            update_coded_phrase(letter, phrase, code_phrase)
        
        return letter, total


def update_coded_phrase(letter ,phrase, code_phrase):
    print(letter) #prints N
    #x=re.findall(letter, phrase)
    iterator= re.finditer(letter, phrase) #finditer -Find all substrings where the RE matches, and returns them 
    #as an iterator. from https://docs.python.org/3/howto/regex.html
    #https://stackoverflow.com/questions/2674391/python-locating-the-position-of-a-regex-match-in-a-string/16360404
    indices = [m.start(0) for m in iterator]
    print(indices)#works - gives [array of ints][0,3,16]
    
    #replace the * at those indices (use regex?) with the letter
    for i in indices:  #loop through indices 
    #make str a list; replace the letter at the index; join list back into a string
    #https://pythonexamples.org/python-string-replace-character-at-specific-position/
        temp = list(code_phrase)
        temp[i] = letter
        code_phrase = "".join(temp)
    print(code_phrase)
    
    return code_phrase

def guess_phrase(phrase):
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
            play_again()
        else:
            print('Sorry, that is not correct')
            user_guess(phrase, code_phrase) #call method to allow another letter guess

def play_again():
    again = input('Would you like to play the game again?')
    again = again.upper()
    main() if again=='Y' else print('Have a nice day') #learned how to do ternary in codeWars
    


main() #call main function