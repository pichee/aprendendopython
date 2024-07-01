horas = float(input("Que horas são?"))
if horas >= 0 and horas <= 11:
    print("Bom dia")
if  horas >= 12 and horas <= 17:
    print("Boa tarde")
if  horas >= 18 and horas <= 23:
    print("Boa noite")
if  horas > 23:
    print("Voce digitou a hora errada")