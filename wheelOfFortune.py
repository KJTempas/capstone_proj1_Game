import re, random

#todo - random phrase

def main():
    phrase = select_phrase() #call method s_p and return phrase
    coded_phrase = code_phrase(phrase) #call method 
    print(f'Here is your mystery phrase: {coded_phrase}')
    user_guess(phrase, coded_phrase)


def select_phrase():
    phrases = ["No news is good news", "An apple a day keeps the doctor away", "A friend in need is a friend indeed"]
    # randomly select from array of phrases
    phrase = random.choice(phrases) #info from https://pynative.com/python-random-choice/-select random from a list
    print(phrase)
    #example phrase for initial testing
    #phrase = "No news is good news"
    phrase = phrase.upper()  #make phrase upper for simpler comparison later (and since Wheel of Fortune uses all caps)
    #print(phrase)
    return phrase

def code_phrase(phrase):
    # show user blanks so they know how many letters and spacing
    #code phrase - let * represent letters
    coded_phrase = re.sub('[A-Za-z]', '*', phrase)
    #print(coded_phrase) 
    return coded_phrase

def user_guess(phrase, coded_phrase):
    letter =input('Guess a letter that you think is in the phrase ->  ')
    #some validation here - is it a letter? isalpha
    #think about upper/lower case -make it all upper
    letter = letter.upper()
    if letter in phrase:
        print('Yes - that letter is in the phrase!')
        #modify coded phrase to add letter
        update_coded_phrase(letter, phrase, coded_phrase) #call method below sending it 3 parameters
        guess_phrase(phrase)
    else:
        print('Sorry - that letter is not in the phrase')

def update_coded_phrase(letter ,phrase, code_phrase):
    print(letter) #prints N
    #x=re.findall(letter, phrase)
    iterator= re.finditer(letter, phrase) #finditer -Find all substrings where the RE matches, and returns them 
    #as an iterator. from https://docs.python.org/3/howto/regex.html
    
    for match in iterator:
        print(match.span()) #span lists the start and end index of the match
        print(match.span([0][0]))  #need to get index of each match; getting tuple
        #re.sub()
    
    #print(x) #shows aray of 3 N's
    #NEED TO WORK ON THIS AREA - need to knowindex of these 3 Ns
    
    #replace the * at those indices (use regex) with the letter
    #sub this with this in this - wont' know where  -need index
      #  re.sub('*',letter, code_phrase)  
       # print(code_phrase)
    #return the recoded phrase
    #pass
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