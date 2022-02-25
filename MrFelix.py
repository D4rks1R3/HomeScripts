#Entradas in json
array_input = [
    {   
         '15'  :  50.00 ,   
         '3'  :  10.00,   
         '5.30'  :  15.50  
    },

    {   
         '10'  :  35.00 ,   
         '7'  :  14.00,   
         '5.30'  :  75.30 
    }


]
#Código de cada peça 1
key = array_input[0]

n_keys = [ n for n in key ]

print("Código de uma peça 1 :", n_keys[0])

print("Todas as keys da peça 1: ", " ".join(n_keys))

print("Numero de peças presente: ", len(key) )