# VL 2nd string methods notes

name = input("What is your name").strip().title()
# .lower() => makes it all lower case
# .upper() => all upper case
# .capitalize() => capitalizes the first letter
# .title() => capitalizes the first letter of every word
age = int(input("Bro how old are you?"))

print("Hello {}, it is nice to meet you! I can't belive you are {:.2f}!".format(name, age))

print(f"Hello {name}, it is nice to meet you! I can't belive you are {age:.1f}!")


#age = input("Bro how old are you?")

#print(age.isdigit())

#print("Really? " + age + "is old")

sentence = "The quick brown fox jumps over the lazy dog!"

word = "brown"
start = sentence.find(word)
length = len(word)


#print(sentence.replace(word, "yellow"))
