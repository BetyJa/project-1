usernames = ['bob','Ann','mike','liz','liz']
passwords = ['123','pass123','password123','pass123','1234']
mezera = "----------------------------------------"
print(mezera)
print("Welcome to the app. Please log in:")
name = input("USERNAME: ")
password = input("PASSWORD: ")
print(mezera)
index = 0
found = False

while index < len(usernames):
    if name.lower() == usernames[index] and password == passwords[index]:
        found = True
    index += 1
if not found:
    exit("USERNAME not found")


TEXTS = [
    "Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley.",

"At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.",

"The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present."

]



user_choice = input('Enter a number between 1 and 3 to select: ')

if int(user_choice) in range(1, 4) and user_choice.isnumeric():
    print(mezera)
else:
    print("You can only choose from values 1-3")
    quit()


chosen_text = TEXTS[int(user_choice) - 1]

all_words = (chosen_text.count(" ") + 1 )
print("There are", all_words, "words in the selected text.")

count = 0
for word in chosen_text.split(" "):
    if word[0].isupper():
        count = count + 1
print("There are",count, "titlecase words")

count = 0
for word in chosen_text.split(" "):
    if word.isupper():
        count = count + 1
print("There are", count, "uppercase words")

count = 0
for word in chosen_text.split(" "):
    if word.islower():
        count = count + 1
print("There are",count, "lowercase words")

count = 0
sum_numeric = 0
for word in chosen_text.split(" "):
    if word.isnumeric():
        count = count + 1
        sum_numeric = sum_numeric + int(word)
print("There are",count, "numeric strings")
print(mezera)

word_counts = {}
for word in chosen_text.split(" "):
    word_counts[len(word)] = word_counts.setdefault(len(word), 0) + 1

for key in sorted(word_counts):
    print(key,"*" * word_counts[key], word_counts[key])

print(mezera)

print("If we summed all the numbers in this text we would get: ", float(sum_numeric))
print(mezera)
