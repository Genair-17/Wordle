'''librerias'''
import linecache
import random

YELLOW = '\033[33m'
GREEN = '\033[32m'
RESET = '\033[0m'

''' Primero se elegie la palabra misteriosa desde un documento con 14855 palabras de 5 letras '''
def obtener_palabra():
    num = random.randint(1, 2315)
    line = linecache.getline("wordles.txt", num)
    return line.rstrip()
    
'''Luego se pediria al usuario una palabra de 5 letras '''
def user_guess():
    guess = str(input())
    guess = guess.lower()
    return guess

'''Checa que sea una palabra real comparandola con el archivo'''
def real_word_check(word):
    words = open("allowed.txt", "r")
    content = words.read()
    if word in content:
        return word
    else:
        print("Not in word list. Try again")
        return "wrong"


'''Checa que sea de 5 letras (implemente la otra funcion para poder repetir 
hasta que el usuaro introduzca una respuesta valida)'''
def letter_count(guess):
    guess_num = len(guess)
    if (guess_num == 5):
        guess = real_word_check(guess)
        return guess 
    else:
        print("not a 5 letter word. Try again")
        return "wrong"
    
'''Primero descompone las palabras letra por letra en una lista'''
# manipulacion de cadenas
def word_decompose(word):
    word_list = list(word)
    return word_list
# manipulacion de cadenas
def guess_decompose(guess):
    guess_list = list(guess)
    return guess_list

'''checa una letra del "guess" ante todas las letras de la palabra misteriosa'''

def letter_compare(guess_list, word_list, num):
    if (guess_list[num] == word_list[num]):
        letter_state = "correct"
    elif ((guess_list[num] == word_list[0]) or 
          (guess_list[num] == word_list[1]) or 
          (guess_list[num] == word_list[2]) or 
          (guess_list[num] == word_list[3]) or 
          (guess_list[num] == word_list[4])):
        letter_state = "partial"
    else:
        letter_state = "incorrect"

    return letter_state 

    
'''Si la letra existe en la palabra pero no esta en la misma posicion que en la original se colorea de amarillo,
si la letra esta en la posicion correcta se colorea de verde'''

def letter_coloring(guess_list, 
                    letter_state_list, 
                    attempts):
    hint_letter_list = []

    for i in range(5):
        if (letter_state_list[i]== "correct"):
            hint_letter_list.append(f"{GREEN}{guess_list[i]}{RESET}")
        elif (letter_state_list[i] == "partial"):
            hint_letter_list.append(f"{YELLOW}{guess_list[i]}{RESET}")
        else:
            hint_letter_list.append(guess_list[i])

    hint = "".join(hint_letter_list)

    print(f"{hint} <--Attempt number:", attempts)


def asigns_state(guess_list, word_list): 

    letter_state_list = []
    lenght = len(guess_list)
    for i in range(lenght):
        letter_state_list.append(letter_compare(guess_list, word_list, i))

    return letter_state_list


def makes_exeptions(letter_state_list, guess_list, num_exepcion, num1, num2, num3, num4):

    if (letter_state_list[num_exepcion] == "correct"):

        if (guess_list[num_exepcion] == guess_list[num1]) and (letter_state_list[num1] != "correct"):
            letter_state_list[num1] = "incorrect"

        elif (guess_list[num_exepcion] == guess_list[num2]) and (letter_state_list[num2] != "correct"):
            letter_state_list[num2] = "incorrect"

        elif (guess_list[num_exepcion] == guess_list[num3]) and (letter_state_list[num3] != "correct"):
            letter_state_list[num3] = "incorrect"     

        elif (guess_list[num_exepcion] == guess_list[num4]) and (letter_state_list[num4] != "correct"):
            letter_state_list[num4] = "incorrect"

    return letter_state_list[num1], letter_state_list[num2], letter_state_list[num3], letter_state_list[num4]

    

def hint(word_list, guess_list, attempts):

    letter_state_list = asigns_state(guess_list, word_list)


    if ((letter_state_list[0] == "correct") and 
        (letter_state_list[1] == "correct") and 
        (letter_state_list[2] == "correct") and 
        (letter_state_list[3] == "correct") and 
        (letter_state_list[4] == "correct")):

        letter_coloring(guess_list,letter_state_list, attempts)
        veredict = "win"

    else:
        '''Se hacen excepciones a las letras que ya fueron designadas como correctas, 
        se colorean de gris, para evitar confusiones'''

        letter_state_list[1], letter_state_list[2], letter_state_list[3], letter_state_list[4] = makes_exeptions(letter_state_list,guess_list,0,1,2,3,4)
        letter_state_list[0], letter_state_list[2], letter_state_list[3], letter_state_list[4] = makes_exeptions(letter_state_list,guess_list,1,0,2,3,4)
        letter_state_list[0], letter_state_list[1], letter_state_list[3], letter_state_list[4] = makes_exeptions(letter_state_list,guess_list,2,0,1,3,4)
        letter_state_list[0], letter_state_list[1], letter_state_list[2], letter_state_list[4] = makes_exeptions(letter_state_list,guess_list,3,0,1,2,4)
        letter_state_list[0], letter_state_list[1], letter_state_list[2], letter_state_list[3] = makes_exeptions(letter_state_list,guess_list,4,0,1,2,3)

        letter_coloring(guess_list, letter_state_list, attempts)
        veredict = "lose"   

    return veredict


#Puntos: * a los cuantos intentos se logro la palabra = base de los puntos
def suma_puntos_attempts(attempts, puntos):
    attempts = attempts - 1

    if attempts == 1:
        puntos = int(puntos + 60)
    elif attempts == 2:
        puntos = int(puntos + 50)
    elif attempts == 3:
        puntos = int(puntos + 40)
    elif attempts == 4:
        puntos = int(puntos + 30)
    elif attempts == 5:
        puntos = int(puntos + 20)
    elif attempts == 6:
        puntos = int(puntos + 10)
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
 
    return puntos

#        * crear archivo con log de intentos y puntos
def abre_archivo():
    f = open("registro.txt", "r")
    print(f.read())
    f.close()

def escribe_score(puntos):
    puntos = str(puntos)
    nombre = str(input("escribe tu nombre\n"))
    f = open("registro.txt", "a")
    f.write("Nombre:"+ " " + nombre + ",  " + "puntaje: " + " "+ puntos + "\n")
    f.close()

def main():
    print("Bienvenido a wordle, \nhay una palabra misteriosa de 5 letras que tienes que encontrar," 
    "\npara esto escribe palabras de 5 letras y te indicaremos con colores algunas pistas para ayudarte"
    "\namarillo = la letra esta en la palabra pero no en el lugar que indicaste"
    "\nverde = la letra este en la palabra y en el lugar indicado"
    "\nblanco = la letra no esta en la palabra"
    "\nEl juego de wordle se juega en ingles")



    """se repite el proceso de pedir palabra y checar hasta que haya sucedido el ciclo 5 veces (5 intentos) """

    word = obtener_palabra() 
    attempts = 1
    veredict = "lose"
    puntos = 0 

    while attempts < 7 and veredict == "lose":

        guess = user_guess()    
        valid_word = letter_count(guess)

        if (valid_word != "wrong"):

            word_list = word_decompose(word)

            guess_list = guess_decompose(guess)

            veredict = hint(word_list, guess_list, attempts)

            puntos = puntos + suma_puntos_letras(guess_list, word_list)
            attempts = attempts + 1

    if veredict == "win": 
        print("you win !")
        puntos = puntos + suma_puntos_letras(guess_list, word_list)

    else: 
        '''si el ciclo termina y no ha adivinado la palabra se revela la palabra y el usuario pierde'''
        print("you lose, the word was", word)


    if puntos > 100:
        putnos = 100

    puntos = suma_puntos_attempts(attempts,puntos)
    print("puntos: ", puntos)
    return puntos

puntos = main()

ans_2 = input("Quieres guardar tu puntaje? S/N\n")

if ans_2 == "S":
    escribe_score(puntos)
    print("El registro de puntajes es:")
    abre_archivo()


ans_1 = input("quieres jugar de nuevo ? S/N\n")

if ans_1 == "S":
    main()

