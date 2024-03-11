Hr = int(input("ingrese total de horas trabajadas: "))
Horasext = int(input("ingrese horas extras trabajadas si tiene: "))
Valor_hora = 10
bono_hextra = 5

if Hr <= 40:
    pagohoras = Valor_hora * Hr
    print(pagohoras)
elif Hr > 40:
    pagoextras = (Valor_hora * Hr) + (Horasext * bono_hextra)
    print(pagoextras)
