n = len(arr)
    positivos = 0
    negativos = 0
    ceros = 0
    for i in arr:
        if i > 0:
            positivos += 1
        elif i < 0:
            negativos += 1
        else:
            ceros += 1
            
    print(positivos/n )
    print(negativos/n )
    print(ceros/n )
