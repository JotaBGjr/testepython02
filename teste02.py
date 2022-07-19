nome = input('Qual o seu nome?')
print('É um prazer te conhecer', nome.format())
n1 = int(input('Me fala um número de 0 à 10?'))
n2 = int(input('Me fala mais um valor?'))
s = n1 + n2
print(' A soma destes dois valores {} + {} é {}'.format(n1, n2, s))
print('Valor total é', s)

a = input('Digite algumacoisa:')
print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('é maiúsculas?', a.isupper())
print('é minúscula?', a.islower())
print('Está Capitalizada?', a.istitle())

n = float(input('Digite um número:'))
n2 = float(input(('Vamos lá quero um número grande! :')))
média = (n + n2) / 2
s2 = n + n2
print('Analisando o valor {}, o seu antecessor é {} e seu sucessor é {:.2f}'.format(n, (n - 1), (n + 1)))
print('A soma destes dois valores {} + {} é {}'.format(n, n2, s2))
print('O dobro de {} vale {}.'.format(n, (n * 2), (n1 * 2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n * 3), n, n ** (1 / 2)))
print('A média entre {} e {} é {}:'.format(n, n2, média))

m = float(input('AGORA, vamos lá! me fala uma distância em metros:'))
'km hm dam m dm cm mm'
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A medida {}metros corresponde à: {} KM,{} HM, {} DAM, {} DM, {} CM, {} MM'.format(m, km, m, dam, dm, cm, mm))
real = float(input('Quantos reais você tem na carteira? :R$'))
dolar = float(input('Qual o valor do dólar hoje? :R$'))
resultado = (real / dolar )
print('Com R${:.2f}, você consegue comprar: {:.2f} Dólar americano'.format(real, resultado, dolar))
vardólar = (dolar - 5.41)/dolar
print('O Dólar variou: {:2f}%'.format(vardólar*100))capital = float(input('Vamos cálcular o Juros compostos de um empréstimo! Me fala um valor para empréstimo: R$'))
juros = float(input('Qual a taxa de juros anual: %'))
i = juros/100
y = 1
y1 = y+1
y2 = y1+1
y3 = y2+1

montante1 = capital*(1 + i)**y
montante2 = capital*(1 + i)**y1
montante3 = capital*(1 + i)**y2
montante4 = capital*(1 + i)**y3

pormês1 = montante1 / 12*y
pormês2 = montante2 / 12*y1
pormês3 = montante3 / 12*y2
pormês4 = montante4 / 12*y3

print('Em {} ano o valor final será: {:.2f} em {}x R${:.2f}'.format(y, montante1, (12*y), pormês1))
print('Em {} anos o valor final será: {:.2f} em {}x R${:.2f}'.format(y1, montante2, (12*y1), pormês2))
print('Em {} anos o valor final será: {:.2f} em {}x R${:.2f}'.format(y2, montante3, (12*y2), pormês3))
print('Em {} anos o valor final será: {:.2f} em {}x R${:.2f}'.format(y3, montante4, (12*y3), pormês4))

