# VL 1st Strings Notes

#What is a string


#String examples
sentence = "The quick brown fox jumps over the lazy dog!" 
first_name = "Tia"
month = "September"
book = "The Return of the King"
food = "chocolate"

print(sentence)
#get length of string
length = len(sentence)
print("The sentence is", length, "characters long!")


print('"Inkheart" is the best book ever!')
print("\t'Inkheart' is the best book ever!")
# escape characters
print("\"Inkheart\" is the best book\never!")


#concatnate 
last_name = "LaRose"
full_name = first_name + " " + last_name

print(full_name)

#index 
print(last_name[:2])
print(last_name[2:-2])
print(sentence[10:15])