# Wordle
NYT Wordle game en python

Contexto:

Wordle es un juego en el que se asigna una palabra no conocida de 5 letras al inicio del juego, el usuario escribe una suposición de 5 letras intentando adivinar la palabra misteriosa y el programa le dice cuales de las letras que utilizo están en la palabra orginal (coloreandolas de amarillo el juego original) y cuales de esas están en en la palabra original y además están en la posición correcta dentro de la palabra (coloreandolas de verde en el juego original). Pienso que es interesante por que ocupa mucha lógica al decidir que color aplica a cada letra.

Pseudo Código

    word_list = ("ready","works","loath","hoard","uncut","alone","plane") #lista de palabras

    word_list.random = answer #no se como se haria esto pero es una palabra al azar de la lista

    answer_list = list(answer) #separar la respuesta en caracteres

    guess = input("Escribe tu suposicion") # esto se haria en un ciclo para limitar la cantidad de intentos 

    guess_list = list(guess)
  
    If (guess==answer):
      print("Correcto!!")

    else:
      if(guess_list[1]==answer_list[1]): #la primera letra es igual en ambas
        print("La primera letra es correta y esta en la posición correcta")
        
      elseif(guess_list[1]==answer_list[2] or guess_list[1]==answer_list[3] or guess_list[1]==answer_list[4] or guess_list[1]==answer_list[5]): 
      #la primera letra existe en la palabra pero en otra posicion.
        print("La primera letra es correcta pero no esta en la posicion correcta")

      if(guess_list[2]==answer_list[2]):
        print("La segunda letra es correta y esta en la posición correcta")
        
      elseif(guess_list[2]==answer_list[1] or guess_list[2]==answer_list[3] or guess_list[2]==answer_list[4] or guess_list[2]==answer_list[5]):
        print("La segunda letra es correcta pero no esta en la posicion correcta")
        
      #y asi con todas las 5 letras.

      
      
