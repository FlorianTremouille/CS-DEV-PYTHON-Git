from Fcts import DateValide

Day = str(input("Tapez le jour : "))
Month = str(input("Tapez le mois : "))
Year = str(input("Tapez l'année : "))

if len(Day) == 1:
    Day = "0" + Day
if len(Month) == 1:
    Month = "0" + Month

Date = Day + "/" + Month + "/" + Year
print(Date)

if DateValide(Date) == True:
    print("La date est valide")
else:
    print("La date est invalide")
