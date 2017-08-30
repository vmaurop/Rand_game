#coding=utf8
from random import randint

def kataliksi(n): # Η συνάρτηση καθορίζει την κατάληξη της λέξης προσπάθεια / ες
    if n<9 : return "ες"
    else : return "α"

number = randint(1,100)

for i in range(10):
    print "Προσπάθησε να μαντέψεις τον κρυφό αριθμό (1-100). Έχεις %d προσπάθει%s:" %(10-i,kataliksi(i)),
    guess = input()
    if guess>number:
        if i==9: #Αν βρισκόμαστε στη 10η προσπάθεια, τότε ο παίκτης χάνει
            print "Δεν τα κατάφερες... Ο κρυφός αριθμός ήταν το %d." %(number)
            break
        print "O κρυφός αριθμός είναι μικρότερος από το %d." %(guess)
        continue
    if guess<number:
        if i==9: #Αν βρισκόμαστε στη 10η προσπάθεια, τότε ο παίκτης χάνει
            print "Δεν τα κατάφερες... Ο κρυφός αριθμός ήταν το %d." %(number)
            break
        print "O κρυφός αριθμός είναι μεγαλύτερος από το %d." %(guess)
        continue
    else:
        print "Το βρήκες!!!"
        break