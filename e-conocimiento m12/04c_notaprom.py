DESC_EXCELENTE: float = 0.20    # descuento con nota excelente
COSTO_MATRICULA = 5000000    # constantes valor pleno matricula
print("eva conocimiento punto4. promedio notas")  # >>> ins notas 1a5 en decimal
alumno = str(input("\n escriba nombre del alumno: "))
nota1 = float(input("Ingrese nota 1taller  1 a 5 : "))
nota2 = float(input("Ingrese nota 2taller  1 a 5 : "))
nota3 = float(input("Ingrese nota 3taller  1 a 5  : "))
nota4 = float(input("Ingrese nota 4taller  1 a 5  : "))
promedio = (nota1 + nota2 + nota3 + nota4) / 4   # operacion de promedio

if 4 <= promedio <= 5:   # condicional >>> clasificar nota
    nota_promcuali = "Excelente"
    descuento = DESC_EXCELENTE
elif 3 <= promedio <= 3.99:
    nota_promcuali = "Bien"
    descuento = 0
else:
    nota_promcuali = "Deficiente"
    descuento = 0
if nota_promcuali == "Excelente":   # Condicion para %20 de matrícula
    costo_final = COSTO_MATRICULA * (1 - descuento)
    print(f"\n {alumno} recibe descuento de 20% en su matrícula")
else:
    costo_final = COSTO_MATRICULA
print(f"\n El estudiante {alumno} obtuvo: ")   # fstr alumno nota costo_final
print(f" promedio {promedio}: {nota_promcuali} valor matricula ${costo_final}")
