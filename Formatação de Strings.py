nome = "Marcus Vinicius"

print(nome)
print("Total de caracteres: " + str(len(nome)))

print(nome[0:12])
print(nome[5:10])
print(nome[7:15])
print(nome[5:])

#-----------------------

frase = "CurSo de LoGica de PRogramaçaõ PYthOn"
#upper retorna todas as letras em maisculas
print(frase.upper())

#lower retorna todas minusculas
print(frase.lower())


#------------------------

notaProva = "Tirei nota seis na prova"

#replace  muda o nome
print(notaProva.replace("seis", "dez"))

#--------------------------

cpf = "123.456.789.10"

cpfPartes = cpf.split(".")

#split separa
print(cpfPartes)

print(cpfPartes[0])
print(cpfPartes[1])
print(cpfPartes[2])

cpfPartes = cpfPartes[2].split(("."))
print(cpfPartes2[0])
print(cpfPartes2[1])

print("CPF: " + cpfPartes[0] + cpfPartes[1] + cpfPartes2[1])




