def ValidarCaracter():
    if len(letra) < 10:
        return "las palabras deben tener almenos 10 letras"
    elif len (letra) > 20:
        return "las palabras no deben mes de 12 caracteres"
    else:
        return True
    
letra = input("ingresa una palabra: ")
print ("ValidaCaracter(letra)")