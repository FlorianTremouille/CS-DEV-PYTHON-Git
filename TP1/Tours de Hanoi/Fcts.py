def Hanoi(nPalets,a=1,b=2,c=3):
    print("Nombre de disques : ",nPalets)
    if n > 0:
        Hanoi(n-1,c,b,a)
        print("Déplace ",a, " sur ", c)