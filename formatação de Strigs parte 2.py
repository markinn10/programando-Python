palavraComEspaco = "        Curso de Python        "

print(palavraComEspaco)
print(palavraComEspaco.strip()) #remove espaços

#--------------------------

gostoPorFrutas = "Eu gosto de laranja"
print("laranja" in gostoPorFrutas)

resultadoProcura = gostoPorFrutas.find("o")

print(resultadoProcura)

#-----------------------

copa = "Brasil vai ganhar a copa do mundo"

campeao = "Alemanha" not in copa

print(campeao)

#---------------------

aluno = "Marcus Vinicius"
nota1 = 9.75
nota2 = 9.58
media = (nota1 + nota2) /2

print("Aluna: " + aluno + " - Media: " + str(media))

print(f"aluna: {aluno} - media:  {media: 2f}")
ajusteTexto = "Aluno: {} - media: {:.2f}"
print(ajusteTexto.format(aluno, media))