def IsBissextile(Y):
    if Y%4 == 0 and str(Y)[-1:-3:-1] != "00":
        return True
    elif Y%400 == 0:
        return True
    else:
        return False

def NbDayInMonthOfYearY(M, Y):              ###Retourne le nombre de jours dans le mois de l'année demandé.
    NbDays = 31
    ThirtyOne = [1,3,5,7,8,10,12]
    Thirty = [4,6,9,11]
    Febuary = 2
    if 1 <= M <= 12:
        for n in Thirty:
            if M == n:
                NbDays = 30
        if M == Febuary:
            if IsBissextile(Y) == True:
                NbDays = 29
            else:
                NbDays = 28
        return NbDays
        
    else:
        return "Erreur dans le mois demandé"


def DateValide(Date):                  
    D = int(Date[0:2])              
    M = int(Date[3:5])
    Y = int(Date[6:])
    DayValid = False
    MonthValid = False

    if 1 <= M <= 12:
        MonthValid = True
    
    nbDays = NbDayInMonthOfYearY(M,Y)
    if isinstance(nbDays,int) and 1 <= D <= nbDays:
        DayValid = True

    if MonthValid == True and DayValid == True:
        return True

    else:
        return False
