#consider using grep


def indx_englsn_wrds( text ):
    return '''json or similar with each identified english word.'''

def is_english_word( word ):
    return '''bool word is english'''

def rmve_1x_vowels( text ):
    #read file line by line
    #for each line in lines
        # split by 
    
    letters = split_word_into_letters( word )
    head,tail = letters.first, letters.last
    vwl_seq_cnt = 0
    prev_vowel = ''
    for letter in letters:
        if letter in vowels and not head and not tail and not is_vowel( letter.prev ) and not is_vowel ( letter.next ):
            word.remove(letter)
    return "text w vowels remkced when not outide and with consonants to left and right"

# make it a module  
