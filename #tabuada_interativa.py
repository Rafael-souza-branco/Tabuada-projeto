#tabuada 

# Passo 1. pedir o numero que sera mostrado a tabuada # e agora o sinal

numero = int(input("Digite o numero: "))
sinal = int(input("""
Digite o sinal
              
1 - +
2 - -
3 - *
4 - / 
:  """))

#Passo 2. Mostrar a tabuada desse numero # com sinal agora 
soma = 0        #valor armazenado
diminuição = 0
multi = 0
divisão = 0


if sinal == 1:   # damos a possibilidade de escolher oq cada numero ira fazer
 
    for i in range (1,11):   #cria loop para colocar de 0 a 10 /// o i serve pra ser uma variavel global do range (1,11)
        soma = numero + i                  # aqui somamos o valor armazenado com i para que a interação seja sempre somando 1 em 1 ///// # e sobre o + é pra se for igual a ele mesmo ele soma 
        print(f"""
{numero} + {i} = {soma} """)
    
elif sinal == 2:
    for i in range (1,11):
        diminuição = numero - i
        print(f"""
{numero} - {i} = {diminuição}""")
        
elif sinal == 3:
    for i in range (1,11):  
        multi = numero * i                  
        print(f"""
{numero} * {i} = {multi} """)
    
elif sinal == 4:
    for i in range (0,11):  # aqui é 0,11 pois se for 1,11 vai dar erro pois nao teremos 0 para ver se podese dividir ou  nao. 
        if i != 0:                  # ele verifica se o numero é 0 ou igual a zero 
            divisão = numero / i
            print(f"""
{numero} / {i} = {divisão:.2f} """) #formatamos pra q seja 2 casas decimais :.2f ex: 10.00
        else:               #else diz q caso for zero ele vai dar erro
            print("""
impossivel dividir por zero! """)