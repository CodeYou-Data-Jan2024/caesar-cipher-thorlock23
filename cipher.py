# add your code here

    #defining the alphabet 
abc = "abcdefghijklmnopqrstuvwxyz"
#user prompt 
shift = int(input ("please input the number of places to shift"))
if shift > 25:
     raise ValueError("enter a number less than 25")
sentance = input ("please enter a sentance")
# output 
new_word = "" # defining new word for putting it on one line 
for letter in sentance:
    if letter == " ":
        encrypted_char = " "
    else: 
        char_index = abc.find(letter)
        shifted_char_index = char_index + shift
        if shifted_char_index > 25:
            shifted_char_index = shifted_char_index -26 
        encrypted_char = abc[shifted_char_index]
    new_word += encrypted_char #putting it all on one line
print (new_word)