word = input("Digite uma palavra: ")

letters = []

inverse = ''

for letter in word:
    letters.append(letter)
    
size = len(letters) - 1

while size >= 0:
    inverse += (letters[size])
    size-=1
    
print("Palavra invertida:", inverse)
