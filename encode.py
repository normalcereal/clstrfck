#consider using grep



# Python implementation of alternate vowel 
# and consonant string  

  
# 'ch' is vowel or not  

def isVowel(ch): 

    if(ch == 'a' or ch == 'e' or 

       ch == 'i' or ch == 'o' or 

       ch == 'u'): 

        return True

    return False

  
# create alternate vowel and consonant string  
# str1[0...l1-1] and str2[start...l2-1]  

def createAltStr(str1, str2, start, l): 

    finalStr = "" 

    i = 0

      

    # first adding character of vowel/consonant  

    # then adding character of consonant/vowel  

    for j in range(start, l): 

        finalStr = (finalStr + str1[i]) + str2[j] 

        i + 1

  

    return finalStr 

  
# function to find the required  
# alternate vowel and consonant string  

def findAltStr(str1): 

    nv = 0

    nc = 0

    vstr = "" 

    cstr = "" 

    l = len(str1) 

    for i in range(0, l): 

          

        # count vowels and updaye vowel string  

        if(isVowel(str1[i])): 

            nv += 1

            vstr = vstr + str1[i] 

              

        # count consonants and update  

        # consonant string  

        else: 

            nc += 1

            cstr = cstr + str1[i] 

              

    # no such string can be formed 

    if(abs(nv - nc) >= 2): 

        return "no such string"

      

    # remove first character of vowel string  

    # then create alternate string with  

    # cstr[0...nc-1] and vstr[1...nv-1]  

    if(nv > nc): 

        return (vstr[0] + createAltStr(cstr, vstr, 1, nv)) 

      

    # remove first character of consonant string  

    # then create alternate string with  

    # vstr[0...nv-1] and cstr[1...nc-1] 

    if(nc > nv): 

        return (cstr[0] + createAltStr(vstr, cstr, 1, nc)) 

      

    # if both vowel and consonant  

    # strings are of equal length  

    # start creating string with consonant  

    if(cstr[0] < vstr[0]): 

        return createAltStr(cstr, vstr, 0, nv) 

  

    return createAltStr(vstr, cstr, 0, nc)  

          
# Driver Code 

if __name__ == "__main__": 

    str1 = "geeks"

    print(findAltStr(str1)) 

  
# This code is contributed by Sairahul099  
C#


def indx_englsn_wrds( text ):
    return '''json or similar with each identified english word.'''
Move one line down i'm do thatJUST REMOVE FIRST OR LAST INNER VOWEL

create dictionary such that:


word = new_word

def is_english_word( word ):
    return '''bool word is english'''

def rmve_1x_vowels( text ):
    #read file line by line
    #for each line in lines
        # split by 
        
    words = text.split(" ")
    
    
    
    for word in words:
        
        #adds padding, removed later
        word = word[1:-1]
        
        for place, letter in enumerate(word):
            
            vowels = 'aeiouAEIOU'
            #consonants
            
            window = f'{letter[place]}{letter[place+1]}{letter[place+2]}
            
            # ne
            if not place == 0 and word[place-1] not in vowels and letter
                
        
        
        
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
