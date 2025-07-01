
# Strings and Regex Practice Questions
# Difficulty Level : Easy
# Create a function that checks whether a word or phrase is palindrome or not.

# Palindrome Definition : It is a word or sequence that when read from right-to-left or left-to-right mean the same word. Example: madam, kayak, racecar, etc. Note : Try solving this using String Slicing and String Concatenation

# Example :

# def palindrome(string):
#     ### your code here
    
# palindrome('madam')
# >>> 'Palindrome!'

# palindrome('aiadventures')
# >>> 'Not Palindrome!'
# Create a function that splits the string and stores the word and length of the word in a dictionary using dictionary comprehension.

# Note : Use String method as well as Regex method.

# Example :

# def len_words(string):
#     ### your code here

# string1 = "Practice Problems to Drill List Comprehension in Your Head."
# len_words(string1)

# >>> {'Practice': 8, 'Problems': 8, 'to': 2, 'Drill': 5, 'List': 4, 'Comprehension': 13, 'in': 2, 'Your': 4, 'Head.': 5}
# Create a function that partitions the string on Python and changes all the uppercase elements to lowercase and vice versa for the 1st part of the partition and capitalizes the words of the 2nd part of the partition.

# Note : Use String method.

# Example :

# def sentence_partition(string):
#     ### your code here

# string1 = "Students put efforts in learning Python for a successful future in emerging technologies!"
# len_words(string1)

# >>> 'sTUDENTS PUT EFFORTS IN LEARNING Python For A Successful Future In Emerging Technologies!'
# Create a function that takes your full name as argument and returns the abbreviations of the first and middle names except the last name which is displayed as it is.

# Note : Use String method as well as Regex method.

# Example :

# def create_abbreviations(fullname):
#     ### your code here

# name = input('Enter your full name : ')
# create_abbreviations(name)

# >>> 
# Enter your full name : Steve Paul Jobs
# 'S.P.Jobs'
# Difficulty Level : Medium
# Create a function that displays a dictionary that extracts a pattern of a vowel being followed by any number of consonants from a string. The value of the dictionary is the length of the substring extracted and the key is a symmetric combination of the substring alongwith its length. The length of the key should be double the length of the substring and it should contain the substring alongwith its length being added to the left of the substring if the length is less than equal to 3 else it is added to the right.

# Note : Use Regex method and try using dictionary comprehension.

# Example :

# def pattern_finding(string):
#     ### your code here

# string1 = 'ABCDEFGHAWQETEAINDVOPLZABMNPUI'
# pattern_finding(string1)

# >>> {'4444ABCD': 4, '4444EFGH': 4, 'AWQ333': 3, 'ET22': 2, '4444INDV': 4, '4444OPLZ': 4, '55555ABMNP': 5}
# Create a function that replaces all the lowercase words with their uppercase versions and vice versa and centers the entire string in 100 spaces only if the 1st word of the string starts with a lowercase letter or ends with an exclamation mark.

# Note : Use String method as well as Regex method for splitting and replacing string values. This question aims to showcase the similarity between String and Regex methods.

# Note : There is no mistake in the output of string1 for words : Always to AlwAys ; upgradation to upgrAdAtion. Debug what might have caused it!

# Example :

# def string_modification(string):
#     ### your code here

# string1 = "learning data science is too much fun! Always in a process of upgradation."
# string_modification(string1)

# >>> '            LEARNING DATA SCIENCE IS TOO MUCH FUN! AlwAys IN A PROCESS OF upgrAdAtion.             
# '

# string2 = "Artificial Intelligence, BlockChain, Cybersecurity and Networking are going to mould the future!"
# string_modification(string2)

# >>> '  Artificial Intelligence, BlockChain, Cybersecurity AND Networking ARE GOING TO MOULD THE FUTURE!  '
# Difficulty Level : Hard
# Create a function that decodes a message encoded in Morse Code, displays the decoded message and the number of vowels and consonants present.

# Note : Use String methods. Sharing a dictionary to help decode the message.

# Note : Google about Morse Code for more information.

# Note : '/' in the message specifies the space between words. ' ' between codes specifies the individual letters.

# Example :

# def decode_count(message):
#     ### your code here

    
# morse_code_dict = { 'A':'.-', 'B':'-...',
#                     'C':'-.-.', 'D':'-..', 'E':'.',
#                     'F':'..-.', 'G':'--.', 'H':'....',
#                     'I':'..', 'J':'.---', 'K':'-.-',
#                     'L':'.-..', 'M':'--', 'N':'-.',
#                     'O':'---', 'P':'.--.', 'Q':'--.-',
#                     'R':'.-.', 'S':'...', 'T':'-',
#                     'U':'..-', 'V':'...-', 'W':'.--',
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#                     '1':'.----', '2':'..---', '3':'...--',
#                     '4':'....-', '5':'.....', '6':'-....',
#                     '7':'--...', '8':'---..', '9':'----.',
#                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#                     '?':'..--..', '!':'-.-.--','/':'-..-.', 
#                     '-':'-....-','(':'-.--.', ')':'-.--.-',}

# message = '-.-. --- -. ... .. ... - . -. -.-. -.-- / .. ... / -.- . -.-- -.-.--'
# decode_count(message)
    
# >>> 
# Decoded Message :  CONSISTENCY IS KEY! 
# Number of Vowels :  5
# Number of Consonants :  15
# Create a function that extracts information like date, name of the news article, URL extension, category of news, and headline from the list of the links provided and display in a tabular format. To display elements in a tabular format, the string elements and the column names are centered on the length of the longest element present inside that column.

# Note : Use combination of String and Regex method. The links provided below are modified and thus not original links. Hence, observe the links for pattterns to extract information.

# Note : Make sure to decide on the number of variables required for this problem. Google to find out the length of the longest element inside the column.

# Example :

# def extract_info(links):
#     ### your code here
    
# links = ['https://www.washingtonpost.com/TECHNOLOGY/2021/08/31/tips-phone-disasters/',
# 'https://www.nytimes.com/2019/12/30/TELEVISION/indian-tv-amazon-netflix/',
# 'https://www.thestar.net/TERRORISM/2019/06/15/maoist-rebels-kill-5-policemen-in-eastern-india/',
# 'https://www.weforum.org/HEALTH/2022/01/10/covid19-top-stories-omicron-coronavirus/',
# 'https://www.livemint.in/2022/04/22/SPORTS/neeraj-chopra-wins-gold-in-javelin-throw-at-tokyo-olympics/']
# extract_info(links)

# >>>
#    Date     News Article  Ext  Category                           Headline                         
# 2021/08/31 washingtonpost com TECHNOLOGY                    tips-phone-disasters                   
# 2019/12/30    nytimes     com TELEVISION                  indian-tv-amazon-netflix                 
# 2019/06/15    thestar     net TERRORISM       maoist-rebels-kill-5-policemen-in-eastern-india      
# 2022/01/10    weforum     org   HEALTH            covid19-top-stories-omicron-coronavirus          
# 2022/04/22    livemint     in   SPORTS   neeraj-chopra-wins-gold-in-javelin-throw-at-tokyo-olympics
# Happy Learning!