def multiplication(A,B):
    '''Multiple 2 matrices enter elles.
    Retourne un couple (C,Booleen).
    C est une liste et le Booleen témoigne de la faisabilité du calcul ou non.'''
    AB = []
    if len(A[0]) != len(B): return AB, False

    for i in range(0,len(A)):
        '''Les X[i] sont des lignes'''
        AB.append([])
        for j in range(0,len(B[0])):
            '''j est un element de la ligne i'''
            AB[i].append(0)
            for k in range(0,len(B)):
                AB[i][j] += A[i][k]*B[k][j]
    return AB, True

def MatAffichage(A):
    '''Affiche chaque ligne d'une matrice en colonne'''
    for i in range(0,len(A)):
        print(A[i])