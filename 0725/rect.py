def only_square_area(X,Y):
    S=[]
    for x in X:
        if x in Y:
            S.append(x**2)
    return(S)

print(only_square_area([32,55,63],[13,32,40,55]))
