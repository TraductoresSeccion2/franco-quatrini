def ValidaNum(num):
    if len(num) < 12:
        return "Debe contener al menos 10 números"
    elif not num.isalnum():
        return  "Debera contener solamente números"
    else:
        return True
    num = input("ingresar numeros: ")
    print ("ValidaNum(num)")
