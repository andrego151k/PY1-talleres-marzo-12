print("calcuradora de imc ")
peso = float(input("ingrese peso exacto en Kilogramos(kg): "))
altura = float(input("ingrese altura en Metros(m) con punto decimal: "))

# imc operacion imc_corto menos decimales.
imc = peso / (altura * altura)
imc_corto = round(imc, 1)
print("Su índice de masa corporal (IMC) es:", imc_corto)

# Rango de 4 categoria y error
if 12 <= imc < 17:
    print("se considera bajo peso.")
elif 17 <= imc < 27:
    print("se considera un peso normal.")
elif 27 <= imc < 32:
    print("se considera sobrepeso.")
elif 32 <= imc < 85:
    print("se considera alta obsidad.")
else:
    print("parece que ingreso mal sus datos")
