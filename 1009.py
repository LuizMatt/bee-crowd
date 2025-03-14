def calcSalary(name, salary, valueSold):
    finalSalary = salary + (valueSold * 0.15)
    return f"TOTAL = R$ {finalSalary:.2f}"


nome = str(input())
salary = float(input())
valueSold = float(input())

print(calcSalary(nome, salary, valueSold))
