fname = input('Enter the file name: ')  #izsaukt faila nosaukuma ievadi, nosaukums mbox-short.txt
try:
    fhand = open(fname, 'r')            #atver failu, lai to lasītu
except:
    print('Wrong file name: ', fname)   #izdrukā, ka ievadītais faila vārs nav pareizs
    quit()    

count = 0
for line in fhand:                      #ciklā lasa katru rindu
    if line.startswith('From '):        #If pārbaudē, ja rinda sākas ar "From "
        word_split = line.split()       #ja rindā tiek atrasts "From ", rinda tiek sadalīta vārdos
        print(word_split[1])            #izdrukā tās e-pasta adreses, kas sūtīja e-pastus 
        count = count + 1               #tiek saskaitītas rindas kuras sākas ar "From "
print('There were', count, 'lines in the file with From as the first word.')   #izdrukā rindu skaitu, kas sākas ar "From "