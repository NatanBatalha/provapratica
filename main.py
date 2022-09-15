## Questao 1

valor1 = int(input('escreva seu primeiro numero'))

valor2 = int(input('escreva seu segundo numero'))

valor3 = int(input('escreva seu terceiro numero'))

if valor1 > valor2 and valor1 > valor3:
 print(valor1)
elif valor2 > valor1 and valor2 > valor3:
 print(valor2)
else:
 print(valor3)

## questao 2

idade = int(input('escreva sua idade'))
tempodeservico = int(input('escreva quanto tempo vc trabalhou'))

if idade >= 65 or tempodeservico == 30:
 print(' voce pode se aposentar')
elif idade >= 60 and tempodeservico >= 25:
 print(' voce pode se aposentar')
else:
 print(' voce ainda nao pode se aposentar')

## questao3

letradefinida = 'a'

turn = 0

letraescolhida = input(' sua vez, escreva uma letra')

while turn < 5:
 if letraescolhida != letradefinida:
  input(' tente outra vez, escreva outra letra')
 turn = turn + 1
else:
 print(' voce ganhou' )

## questao4
escolha = int(input(' Escolha dentro as opcoes: 1 - consultar saldo,2- sacar, 3 - deposito, 4 - sair'))
withdraw = int(input(' quanto vc deseja ')
saldo = 0
put = int(input(' quanto vc deseja')
while escolha != 4:
 if escolha == 1:
  print(saldo)
 elif escolha == 2:
  print(withdraw)
saldo = saldo - withdraw
print (saldo)
else:
  print(put)
saldo = saldo + put

