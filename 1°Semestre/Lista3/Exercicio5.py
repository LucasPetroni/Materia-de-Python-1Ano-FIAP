salario = int(input("Qual seu Salario?"))

qtd_he = int(input("Quantas horas extras voce fez esse mes?"))


dias_uteis = (7-2) * 4

horas_trabalhadas = dias_uteis * 8

valor_hora = (salario/dias_uteis) / horas_trabalhadas

hora_extra = (valor_hora / 2) * qtd_he

salario_final = salario + hora_extra


print(valor_hora)
print(hora_extra)
print("O seu salario desse mes vai ser R$", salario_final, " reais")