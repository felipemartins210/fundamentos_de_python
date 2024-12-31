# Incializa as constantes
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# SOLICITA AS ENTRADAS
grossIncome = float(input("Entre com o salário bruto: "))
numDependents = int(input("Entre com o número de dependentes: "))

# CALCULA O IMPOSTO
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

# Exibe o imposto de renda
print("O imposto de renda é: $" + str(incomeTax))


