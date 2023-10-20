#variavel

pontuação1 = 0
pontuação2 = 100

if pontuação1 < pontuação2:
    print("Pontuação dois maior que um. ")

"""

Utilize a estrutura de controle if-elif-else para classificar a pontuação do seguinte modo:

Se a pontuação for maior ou igual a 90, imprima "Sua classificação é A. Parabéns!" (FEITO)

Se a pontuação for maior ou igual a 80 e menor que 90, imprima "Sua classificação é B. Muito bom!"

Se a pontuação for maior ou igual a 70 e menor que 80, imprima "Sua classificação é C. Bom trabalho!"

Se a pontuação for maior ou igual a 60 e menor que 70, imprima "Sua classificação é D. Precisa melhorar!"

Se a pontuação for menor que 60, imprima "Sua classificação é F. Estude mais!"
"""

classificação = "Parabens"
pontuacao = 90

if classificação == "Parabens" and pontuacao == 90:
    print("Sua classificação é 90: Parabéns.")
else:
    print("pontuacao ou classificação inválida. ")