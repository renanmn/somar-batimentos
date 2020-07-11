nome = input('Informe seu nome: ')
idade = int(input('Sua idade: '))


#batimentos por minuto (Criança, adulto, dormindo)
bpmcri = 130
bpmadu = 80


#batimentos por hora (Criança, adulto, dormindo)
bphcri = bpmcri*60
bphadu = bpmadu*60


#batimentos por dia (Criança, adulto, dormindo)
bpdcri = bphcri*24
bpdadu = bphadu*24


#batimentos por ano (Criança, adulto, dormindo)
bpacri = bpdcri * 365
bpaadu = bpdadu * 365


if idade <= 12:
    calc = bpacri * idade
    print('Olá {}, Seu coração já bateu mais de {} vezes'.format(nome, calc))

if idade > 12:
#batimentos ate 12 anos
    calcc = (bpacri*12)
#idade atual menos 12
    calci = (idade-12)
#soma dos batimentos anuais depois dos 12 anos
    calca = (bpaadu*calci)
#calculo dos batimentos ate 12 anos com o de depois dos 12
    calc = (calcc + calca)
    print('{}, Seu coração já bateu mais de {} vezes'.format(nome, calc))









