

from collections import Counter	
import urllib.request

  
data = urllib.request.urlopen('https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt') # it's a file like object and works just like a file
for line in data: # files are iterable
    #print (line)

    read_data = data.read()
    per_word = read_data.split()

#print('Total Words:', len(per_word))

#number_of_characters = len(per_word)

#print('Number of characters in text file :', number_of_characters)



c = Counter(per_word)

print(c.items())

   
