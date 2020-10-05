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

'''
import clstrfck as cf

text_file = ... #load text file 

#create new encoder object to manipulate text with
encoder = cf.text_encoder( )

#assign encoded text without certain vowels to file named encoded_file 

encoded_file = ... #create new empty file and load for writing

#write encoded output from remove_vowels where text_file is original file

ENCDDfle

encoded_file.write ( encoder.remove_vowels( type = "rmve_cvc", text_file )
'''
