from plistlib import PlistFormat


def mesImpots(RevenuAImposer, PIndex=3):
    [P2, P3, P4, P5] = [10225, 26070, 74545, 160335]
    Impots = 0
    if RevenuAImposer > P5+1:
        Impots += (RevenuAImposer - P5+1)*45/100
        RevenuAImposer = P5
    if RevenuAImposer > P4+1:
        Impots += (RevenuAImposer - P4+1)*41/100
        RevenuAImposer = P4
    if RevenuAImposer > P3+1:
        Impots += (RevenuAImposer - P3+1)*30/100
        RevenuAImposer = P3
    if RevenuAImposer > P2+1:
        Impots += (RevenuAImposer - P2+1)*11/100
        RevenuAImposer = P2
    return Impots

def mesImpotsRecursif(RevenuAImposer, PIndex, Impots=0):
    '''Calcul l'impot de manière récursive'''
    Plist = [10225, 26070, 74545, 160335]
    Taux = [11, 30, 41, 45]
    
    print(RevenuAImposer)
    print(Impots)

    if RevenuAImposer <= Plist[0]+1:
        print('retour:', Impots)
        return Impots

    if RevenuAImposer > Plist[PIndex]:
        Impots += (RevenuAImposer - Plist[PIndex])*Taux[PIndex]/100
        RevenuAImposer = Plist[PIndex]

    mesImpotsRecursif(RevenuAImposer, PIndex-1, Impots)