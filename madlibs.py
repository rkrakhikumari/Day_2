## string concatination (how to put string together.)
# # suppose we want to create a string that says "you should learn ____"
#   language = "python" # sme string variable

#different ways of concatination
#  print("You should learn " + language)  #You shold learn python
#  print("You should learn {}". format(language))  #You shold learn python
#  print(f"You should learn {language}")  #You shold learn python

adj = input("adjective: ")
verb1 = input("Verb1: ")
verb2 = input("verb2: ")
famous_person = input("Famous person: ")


madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \nI love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}! "

print(madlib)
