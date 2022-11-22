from unittest import result
from Fcts import multiplication,MatAffichage

A = [[1,2,3],
     [1,2,3],
     [1,2,3]]

B = [[1,2,3],
     [1,2,3]]


C, Valid = multiplication(A,B)

if Valid == True:
     MatAffichage(C)
else:
     print("Dimensions incompatibles !")