import re

#todo - random phrase

def main():
    phrase = select_phrase() #call method s_p and return phrase
    coded_phrase = code_phrase(phrase) #call method 
    print(f'Here is your mystery phrase: {coded_phrase}')
    user_guess(phrase, coded_phrase)
    
    #play again?


def select_phrase():
    #RANDOM
    # randomly select from array of phrases
    #example phrase
    phrase = "No news is good news"
    phrase = phrase.upper()
    #print(phrase)
    return phrase

def code_phrase(phrase):
    # show user blanks so they know how many letters and spacing
    #code phrase - let * represent letters
    coded_phrase = re.sub('[A-Za-z]', '*', phrase)
    #print(coded_phrase) 
    return coded_phrase

def user_guess(phrase, coded_phrase):
    guess =input('Guess a letter that you think is in the phrase ->  ')
    #some validation here - is it a letter? isalpha
    #think about upper/lower case -make it all upper
    if guess.upper() in phrase:
        print('Yes - that letter is in the phrase!')
        #modify coded phrase to add letter

        
    else:
        print('Sorry - that letter is not in the phrase')


main() #call main function