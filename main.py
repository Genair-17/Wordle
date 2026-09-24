'''librerias'''
import linecache
import random


''' Primero se elegie la palabra misteriosa desde un documento con 14855 palabras de 5 letras '''
def obtener_palabra ():
    num = random.randint(1, 2315)
    line = linecache.getline("wordles.txt",num)
    return line.rstrip()
    
'''Luego se pediria al usuario una palabra de 5 letras '''
def user_guess ():
    guess = str(input())
    return guess

'''Checa que sea una palabra real comparandola con el archivo'''
def real_word_check(word):
    words = open("allowed.txt","r")
    content = words.read()
    if word in content:
        return word
    else:
        print("Not in word list. Try again")
        return "wrong"


'''Checa que sea de 5 letras (implemente la otra funcion para poder repetir hasta que el usuaro introduzca una respuesta valida)'''
def letter_count (guess):
    guess_num = len(guess)
    if (guess_num == 5):
        guess = real_word_check(guess)
        return guess 
    else:
        print("not a 5 letter word. Try again")
        return "wrong"
    
'''Primero descompone las palabras letra por letra en una lista'''

def word_decompose(word):
    word_list = list(word)
    return word_list

def guess_decompose(guess):
    guess_list = list(guess)
    return guess_list

'''checa una letra del "guess" ante todas las letras de la palabra misteriosa'''

def letter_compare(guess_list, word_list,num):
    if (guess_list[num] == word_list[num]):
        letter_state = "correct"
    elif ((guess_list[num] == word_list[0]) or (guess_list[num] == word_list[1]) or (guess_list[num] == word_list[2]) or (guess_list[num] == word_list[3]) or (guess_list[num] == word_list[4])):
        letter_state = "partial"
    else:
        letter_state = "incorrect"

    return letter_state 

    
'''Si la letra existe en la palabra pero no esta en la misma posicion que en la original se colorea de amarillo,
si la letra esta en la posicion correcta se colorea de verde'''

def letter_coloring(guess_list,letter_0_state, letter_1_state, letter_2_state, letter_3_state, letter_4_state, attempts):
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    RESET = '\033[0m'

    if (letter_0_state == "correct"):
        hint_letter_0 = f"{GREEN}{guess_list[0]}{RESET}"
    elif (letter_0_state == "partial"):
        hint_letter_0 = f"{YELLOW}{guess_list[0]}{RESET}"
    else:
        hint_letter_0 = guess_list[0]

    if (letter_1_state == "correct"):
        hint_letter_1 = f"{GREEN}{guess_list[1]}{RESET}"

    elif (letter_1_state == "partial"):
        hint_letter_1 = f"{YELLOW}{guess_list[1]}{RESET}"
    else:
        hint_letter_1 = guess_list[1]

    if (letter_2_state == "correct"):
        hint_letter_2 = f"{GREEN}{guess_list[2]}{RESET}"
    elif (letter_2_state == "partial"):
        hint_letter_2 = f"{YELLOW}{guess_list[2]}{RESET}"
    else:
        hint_letter_2 = guess_list[2]

    if (letter_3_state == "correct"):
        hint_letter_3 = f"{GREEN}{guess_list[3]}{RESET}"
    elif (letter_3_state == "partial"):
        hint_letter_3 = f"{YELLOW}{guess_list[3]}{RESET}"
    else:
        hint_letter_3 = guess_list[3]

    if (letter_4_state == "correct"):
        hint_letter_4 = f"{GREEN}{guess_list[4]}{RESET}"
    elif (letter_4_state == "partial"):
        hint_letter_4 = f"{YELLOW}{guess_list[4]}{RESET}"
    else:
        hint_letter_4 = guess_list[4]

    print(f"{hint_letter_0}{hint_letter_1}{hint_letter_2}{hint_letter_3}{hint_letter_4} <--Attempt number:", attempts)


def asigns_state(guess_list, word_list): 

    letter_0_state = letter_compare(guess_list,word_list,0)
    letter_1_state = letter_compare(guess_list,word_list,1)
    letter_2_state = letter_compare(guess_list,word_list,2)
    letter_3_state = letter_compare(guess_list,word_list,3)
    letter_4_state = letter_compare(guess_list,word_list,4) 

    letter_state_list = [letter_0_state, letter_1_state, letter_2_state, letter_3_state, letter_4_state]
    return letter_state_list

    

def hint(word_list, guess_list, attempts):

    '''compara cada letra del guess con cada letra de la palabra misteriosa'''
    letter_0_state = letter_compare(guess_list,word_list,0)
    letter_1_state = letter_compare(guess_list,word_list,1)
    letter_2_state = letter_compare(guess_list,word_list,2)
    letter_3_state = letter_compare(guess_list,word_list,3)
    letter_4_state = letter_compare(guess_list,word_list,4)


    if ((letter_0_state == "correct") and 
        (letter_1_state == "correct") and 
        (letter_2_state == "correct") and 
        (letter_3_state == "correct") and 
        (letter_4_state == "correct")):
        
        letter_coloring(guess_list, letter_0_state, letter_1_state, letter_2_state, letter_3_state, letter_4_state, attempts)
        veredict = "win"

    else:
        '''Se hacen excepciones a las letras que ya fueron designadas como correctas, se colorean de gris, para evitar confusiones'''

        if (letter_0_state == "correct"):
            if (guess_list[0] == guess_list[1]):
                letter_1_state = "incocorrect"
            elif (guess_list[0] == guess_list[2]):
                letter_2_state = "incocorrect"
            elif (guess_list[0] == guess_list[3]):
                letter_3_state = "incocorrect"     
            elif (guess_list[0] == guess_list[4]):
                letter_4_state = "incocorrect"
        elif(letter_1_state == "correct"):
            if (guess_list[1] == guess_list[0]):
                letter_0_state = "incocorrect"
            elif (guess_list[1] == guess_list[2]):
                letter_2_state = "incocorrect"
            elif (guess_list[1] == guess_list[3]):
                letter_3_state = "incocorrect"     
            elif (guess_list[1] == guess_list[4]):
                letter_4_state = "incocorrect"        
        elif(letter_2_state == "correct"):
            if (guess_list[2] == guess_list[0]):
                letter_0_state = "incocorrect"
            elif (guess_list[2] == guess_list[1]):
                letter_1_state = "incocorrect"
            elif (guess_list[2] == guess_list[3]):
                letter_3_state = "incocorrect"     
            elif (guess_list[2] == guess_list[4]):
                letter_4_state = "incocorrect"  
        elif(letter_3_state == "correct"):
            if (guess_list[3] == guess_list[0]):
                letter_0_state = "incocorrect"
            elif (guess_list[3] == guess_list[1]):
                letter_1_state = "incocorrect"
            elif (guess_list[3] == guess_list[2]):
                letter_2_state = "incocorrect"     
            elif (guess_list[3] == guess_list[4]):
                letter_4_state = "incocorrect"  
        elif(letter_4_state == "correct"):
            if (guess_list[4] == guess_list[0]):
                letter_0_state = "incocorrect"
            elif (guess_list[4] == guess_list[1]):
                letter_1_state = "incocorrect"
            elif (guess_list[4] == guess_list[2]):
                letter_2_state = "incocorrect"     
            elif (guess_list[4] == guess_list[3]):
                letter_3_state = "incocorrect"  

        letter_coloring(guess_list,letter_0_state, letter_1_state, letter_2_state, letter_3_state, letter_4_state, attempts)
        veredict = "lose"

    return veredict


'''
##FALTA##
#Cambiar sistema de hint para que sea por lista y poder integrar una función
##FALTA#
'''

#Puntos: * a los cuantos intentos se logro la palabra = base de los puntos
def suma_puntos_attempts(attempts):
    attempts = attempts -1

    if attempts == 1:
        puntos = 50
    elif attempts == 2:
        puntos = 40
    elif attempts == 3:
        puntos = 30
    elif attempts == 4:
        puntos = 20
    elif attempts == 5:
        puntos = 10
    return puntos

#        * cuantas palabras amarillas = x cantidad de puntos
#        * cuantas palabras verdes = x+ cantidad de puntos
def suma_puntos_letras(guess_list, word_list):
    letter_state_list = asigns_state(guess_list, word_list)
    puntos = 0
    for x in letter_state_list:
        if x == "correct":
            puntos = puntos + 4
        if x == "partial":
            puntos = puntos + 2
        if x == "incorrect":
            puntos = puntos 
    return puntos

#        * crear archivo con log de intentos y puntos



print("Bienvenido a wordle, hay una palabra misteriosa de 5 letras que tienes que encontrar,")
print("para esto escribe palabras de 5 letras y te indicaremos con colores algunas pistas para ayudarte")
print("amarillo = la letra esta en la palabra pero no en el lugar que indicaste")
print("verde = la letra este en la palabra y en el lugar indicado")
print("blanco = la letra no esta en la palabra")
print("El juego de wordle se juega en ingles")


#word = obtener_palabra() 
word = "music"
"""se repite el proceso de pedir palabra y checar hasta que haya sucedido el ciclo 5 veces (5 intentos) """
attempts = 1
veredict = "lose"
puntos = 0 

while attempts < 6 and veredict == "lose":

    guess = user_guess ()    
    valid_word = letter_count(guess)

    if (valid_word != "wrong"):

        word_list = word_decompose(word)

        guess_list = guess_decompose(guess)

        veredict = hint(word_list, guess_list, attempts)

        puntos = puntos + suma_puntos_letras(guess_list, word_list)
        attempts = attempts +1

if veredict == "win": 
    print("you win !")
    puntos = puntos + suma_puntos_letras(guess_list, word_list)

else: 
    '''si el ciclo termina y no ha adivinado la palabra se revela la palabra y el usuario pierde'''
    print("you lose, the word was", word)


puntos = puntos + suma_puntos_attempts(attempts)
print("puntos: ", puntos)