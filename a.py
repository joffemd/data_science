
# repeatedly ask user for a word
# concatenate the words
# when user enters ! ? or . end and display the sentence

sentence = ""

while True:
    new_word = raw_input("Enter a word (, ! or ? to end): ")

    if new_word in (".","!","?"):
        print sentence[0:len(sentence)-1] + new_word
        break
    else:
        sentence += new_word + " "

        
        
