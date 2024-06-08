# validando cpf
import os


os.system('cls')

cpf = input('entre com o seu cpf: ').strip()
quantidade_caracteres = len(cpf)

if( 0 <= quantidade_caracteres > 11):
    print(f'o cpf{cpf} é invalido.')
else:
    print(f'o cpf{cpf} é valido')  

if(cpf.isnumeric() ):
    print(f' o cpf esta correto ')
else:
    print(f' o cpf esta errado ')
