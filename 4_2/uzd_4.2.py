fname = input('Enter file name: ')              # Tekta ievade
fhand = open(fname)                             # Atver ievadīto failu
histogram = {}                                  # Izveido tukšu vārdnīcu
for line in fhand:                              # Ciklā interē cauri teksta rindām
    domain = line.strip()                       # Ar strip() metodi noņem no abiem galiem visas nevajadzīgās atstarpes
    if not line.startswith('From:') :           # If pārbaudē, ja rindā teksts nesākas ar "From:" pārejam uz else bloku
        continue
    else:
        domain = line.split('@')[1].rstrip()    # No rindas ar "From:", atrod to teksta daļu, kur ir "@" un sadala to divās daļās.
                                                # Ar indeksu [1] norāda kuru no divam daļām pievienot "domain".
                                                # Papildus, rstrip() funkcija noņem jaunās rindkopas "\n" no labās puses.
        histogram[domain] = histogram.get(domain, 0 ) + 1     # Pievieno domēnu klāt vārdnīcai. 
                                                              # Atgriež vērtību +1, ja adrese atkārtojas vārdnīcā.

print(histogram)                                # Izprintē vārdnīcu
