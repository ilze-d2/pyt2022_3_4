import string
from string import digits

counts = 0 
d_counts = dict()      #Izveido mainīgos
rel_lst = list()

fname = input("Enter file:") #Faila atvēršana
if len(fname) < 1 : fname = "File Not Found"
fhand = open(fname)

for line in fhand: #Teksta formatēšana - noņem pieturzīmes, skaitļus, izņem atstarpes and pārveido visus burtus uz mazajiem
    line = line.rstrip()
    line = line.lower()
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.translate(str.maketrans('','',digits))

words = line.split() #Saskaita katru burtu biežumam
for word in words:
        for letter in word:
            counts += 1
            if letter not in d_counts:
                d_counts[letter] = 1
            else:
                d_counts[letter] += 1

for key, val in list(d_counts.items()):
    rel_lst.append((val / counts, key))  #Sarēķina biežumu

rel_lst.sort(reverse=True)         #Izveido sarakstu sākot no augstākajiem biežumiem

for key, val in rel_lst:
    print(key, val)