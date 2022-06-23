
import numpy as np	
import urllib.request

  
data = urllib.request.urlopen('https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt') # it's a file like object and works just like a file
for line in data: # files are iterable
   
    #print (line)

    read_data = data.read()
    per_word = read_data.split()
    print(per_word)    

