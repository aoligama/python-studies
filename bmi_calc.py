weight = float(input('Digite o Peso(kg): '))
height = float(input('Digite a Altura(m): '))

bmi = weight/(height ** 2)

if bmi < 16.00:
    print('Baixo peso Grau III')
elif 16.00 <= bmi < 16.99:
    print('Baixo peso Grau II')
elif 17.00 <= bmi < 18.49:
    print('Baixo peso Grau I')
elif 18.5 <= bmi < 24.99:
    print('Peso Ideal')
elif 25.00 <= bmi < 29.99:
    print('Sobrepeso')
elif 30.00 <= bmi < 34.99:
    print('Obseidade Grau I')
elif 35.00 <= bmi < 39.99:
    print('Obesidade Grau II')
elif bmi >= 40.00:
    print('Obesidade Grau III')