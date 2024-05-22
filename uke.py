import random
#this is or cords 
Cord_C = ["C","Cm","C7","Cm7","C6","Cm6","Csus4","Cdim"]
Cord_D = ["D","Dm","D7","Dm7","D6","Dm6","Dsus4","Ddim"]
Cord_E = ["E","Em","E7","Em7","E6","Em6","Esus4","Edim"]
Cord_F = ["F","Fm","F7","Fm7","F6","Fm6","Fsus4","Fdim"]
Cord_G = ["G","Gm","G7","Gm7","G6","Gm6","Gsus4","Gdim"]
Cord_A = ["A","Am","A7","Am7","A6","Am6","Asus4","Adim"]
Cord_B = ["B","Bm","B7","Bm7","B6","Bm6","Bsus4","Bdim"]

#this stores the cords in a dictionary so its easier to access them
scale  = {"C":Cord_C,"D":Cord_D,"E":Cord_E,"F":Cord_F,"G":Cord_G,"A":Cord_A,"B":Cord_B}

def ran_cord_progression(scale):
    #this is the random cord progression
    for i in scale:
        s = print(random.choice(scale.get(i)))

    
random_cord_progression = ran_cord_progression(scale)
