#domínio = código genético do cromossomo
#hélices (x e y) = variáveis (por enquanto, será utilizada apenas uma variável)
#base (ligação entre as hélices) = resultado da função (imagem)
#maximização = iterações sucessivas segundo o princípio das espécies de Darwin
#A forma das funções está restrita à este formato por enquanto: Número Operação Variável
import operator
f = input('Insira a função: ') #Lista de string da função
f = f.split(' ') #Divide a string de forma a separar cada termo da função em uma nova string
indice_x = f.index('x') #Informa qual o indice da variável da funcao
min_x = int(input('Insira o limite inferior do domínio:')) #Usuário insere o domínio da função
max_x = int(input('Insira o limite máximo do domínio:'))
objetivo = input('Você deseja encontrar o ponto de máximo ou de mínimo da função?'
                 '\nDigite "max" se deseja encontrar o ponto de máximo.' \
                 '\nDigite "min" se deseja encontrar o ponto de mínimo.'
                 '\nSeu objetivo é: ') #Pergunta como a função deve ser otimizada
funcao = []  # Lista de pares ordenados da função : [f(x), x]

if '1' in f: #Transforma os números de string para inteiros operáveis
    int_1 = f.index('1')
    f[int_1] = 1
elif '2' in f:
    int_2 = f.index('2')
    f[int_2] = 2
elif '3' in f:
    int_3 = f.index('3')
    f[int_3] = 3
elif '4' in f:
    int_4 = f.index('4')
    f[int_4] = 4
elif '5' in f:
    int_5 = f.index('5')
    f[int_5] = 5
elif '6' in f:
    int_6 = f.index('6')
    f[int_6] = 6
elif '7' in f:
    int_7 = f.index('7')
    f[int_7] = 7
elif '8' in f:
    int_8 = f.index('8')
    f[int_8] = 8
elif '9' in f:
    int_9 = f.index('9')
    f[int_9] = 9
elif '0' in f:
    int_0 = f.index('0')
    f[int_0] = 0

for x in range(min_x, max_x+1): #Primeira iteração: Vai testar os inteiros do domínio da função.
    f[indice_x] = x #Transforma a string 'x' para variável operável
    if '+' in f: #Transforma as operações que estão na string em operações de fato.
        op_soma = f.index('+')
        calculo = int(f[op_soma - 1]) + x #A forma das funções está restrita à este formato
        funcao.append([calculo, x]) #Insere na lista funcao o par ordenado [f(x), x]
        print(f'f({x}) = {calculo}') #Imprime f(x) = y
    if '-' in f:
        op_subtracao = f.index('-')
        calculo = int(f[op_subtracao - 1]) - x
        funcao.append([calculo, x])
        print(f'f({x}) = {calculo}')
    if '*' in f:
        op_produto = f.index('*')
        calculo = int(f[op_produto - 1]) * x
        funcao.append([calculo, x])
        print(f'f({x}) = {calculo}')
    if '/' in f:
        op_divisao = f.index('/')
        calculo = int(f[op_divisao - 1]) / x
        funcao.append([calculo, x])
        print(f'f({x}) = {calculo}')
    if '^' in f:
        op_potencia = f.index('^')
        calculo = int(f[op_potencia - 1]) ** x
        funcao.append([calculo, x])
        print(f'f({x}) = {calculo}')
if objetivo == 'max': #Reconhece como deve ser otimizada a função
        print ('\n>>>>>>>>Primeira iteração<<<<<<<<\n')
        print(f'f({x}) = {calculo}')
        max_funcao = max(funcao) #Encontra o ponto de máximo da função na primeira iteração

        pos_max = funcao.index(max_funcao) #Reconhece o índice do par ordenado do ponto de máximo da função
        xmax = funcao[pos_max][1] #Define xmax como o 'x' do par ordenado do ponto de máximo da função
        xmax1 = xmax+1
        xmax2 = xmax-1
        print (f'O ponto de máximo da primeira iteração é:\nf({funcao[pos_max][1]}) = {funcao[pos_max][0]}')

        seg_iteracao=[]
        print ('\n>>>>>>>>Segunda iteração<<<<<<<<\n')
        while xmax <= xmax1: #Enquanto o x do ponto de máximo for menor que esse mesmo x somado a um, e enquanto for menor que o limite máximo do domínio da função:
            xmax=xmax+0.1 #Define a taxa de erro de 0,1 para a iteração
            if '+' in f:
             op_soma = f.index('+')
             calculo = int(f[op_soma - 1]) + xmax
             funcao.append([calculo, xmax])
             print(f'f({xmax}) = {calculo}')
            if '-' in f:
             op_subtracao = f.index('-')
             calculo = int(f[op_subtracao - 1]) - xmax
             funcao.append([calculo, xmax])
             print(f'f({xmax}) = {calculo}')
            if '*' in f:
             op_produto = f.index('*')
             calculo = int(f[op_produto - 1]) * xmax
             funcao.append([calculo, xmax])
             print(f'f({xmax}) = {calculo}')
            if '/' in f:
             op_divisao = f.index('/')
             calculo = int(f[op_divisao - 1]) / xmax
             funcao.append([calculo, xmax])
             print(f'f({xmax}) = {calculo}')
            if '^' in f:
             op_potencia = f.index('^')
             calculo = int(f[op_potencia - 1]) ** xmax
             funcao.append([calculo, xmax])
             print(f'f({xmax}) = {calculo}')

            seg_iteracao.append([calculo,xmax])
            print(f'f({xmax}) = {calculo}')
            seg_iteracao_max = max(seg_iteracao)
            pos_max1 = seg_iteracao.index(seg_iteracao_max)
            seg_iteracao_x = seg_iteracao[pos_max1][1]
            seg_iteracao_y = seg_iteracao[pos_max1][0]
        print(f'\nO ponto de máximo da segunda iteração é:\nf({seg_iteracao_x}) = {seg_iteracao_y}')

        print ('\n>>>>>>>>Terceira iteração<<<<<<<<\n')
        ter_iteracao=[]

        while xmax >= xmax2:
            xmax = xmax - 0.1
            if '+' in f:
                op_soma = f.index('+')
                calculo = int(f[op_soma - 1]) + xmax
                funcao.append([calculo, xmax])
                print(f'f({xmax}) = {calculo}')
            if '-' in f:
                op_subtracao = f.index('-')
                calculo = int(f[op_subtracao - 1]) - xmax
                funcao.append([calculo, xmax])
                print(f'f({xmax}) = {calculo}')
            if '*' in f:
                op_produto = f.index('*')
                calculo = int(f[op_produto - 1]) * xmax
                funcao.append([calculo, xmax])
                print(f'f({xmax}) = {calculo}')
            if '/' in f:
                op_divisao = f.index('/')
                calculo = int(f[op_divisao - 1]) / xmax
                funcao.append([calculo, xmax])
                print(f'f({xmax}) = {calculo}')
            if '^' in f:
                op_potencia = f.index('^')
                calculo = int(f[op_potencia - 1]) ** xmax
                funcao.append([calculo, xmax])
                print(f'f({xmax}) = {calculo}')
            ter_iteracao.append([calculo,xmax])
            print(f'f({xmax}) = {calculo}')
            ter_iteracao_max = max(ter_iteracao)
            pos_max2 = ter_iteracao.index(ter_iteracao_max)
            ter_iteracao_x = ter_iteracao[pos_max2][1]
            ter_iteracao_y = ter_iteracao[pos_max2][0]
        print(f'\nO ponto de máximo da terceira iteração é:\nf({ter_iteracao_x}) = {ter_iteracao_y}')

        print (f'\n\n>>>>>>>>Primeira iteração<<<<<<<<\nO ponto de máximo da primeira iteração é:\nf({funcao[pos_max][1]}) = {funcao[pos_max][0]}')
        print(f'\n>>>>>>>>Segunda iteração<<<<<<<<\nO ponto de máximo da segunda iteração é:\nf({seg_iteracao_x}) = {seg_iteracao_y}')
        print(f'\n>>>>>>>>Terceira iteração<<<<<<<<\nO ponto de máximo da terceira iteração é:\nf({ter_iteracao_x}) = {ter_iteracao_y}')

        if max(seg_iteracao)<=max(ter_iteracao): #Define qual é o máximo global da função através de comparações
            print(f'\n>>>>>>>>Conclusão:<<<<<<<<\nO ponto de máximo, definitivo da função é: \nf({ter_iteracao_x}) = {ter_iteracao_y}')
        else:
            print(f'\nO ponto de máximo, definitivo da função é: \nf({seg_iteracao_x}) = {seg_iteracao_y}')

elif objetivo == 'min': #Mesmos passos da procura pelo ponto de máximo
    print('\n>>>>>>>>Primeira iteração<<<<<<<<\n')
    print(f'f({x}) = {calculo}')
    min_funcao = min(funcao)

    pos_min = funcao.index(min_funcao)
    xmin = funcao[pos_min][1]
    xmin1 = xmin+1
    xmin2 = xmin-1
    print(f'O ponto de mínimo da primeira iteração é:\nf({funcao[pos_min][1]}) = {funcao[pos_min][0]}')

    seg_iteracao = []
    print('\n>>>>>>>>Segunda iteração<<<<<<<<\n')
    while xmin <= xmin1:
        xmin = xmin + 0.1
        if '+' in f:
            op_soma = f.index('+')
            calculo = int(f[op_soma - 1]) + xmin
            funcao.append([calculo, xmin])
            print(f'f({xmin}) = {calculo}')
        if '-' in f:
            op_subtracao = f.index('-')
            calculo = int(f[op_subtracao - 1]) - xmin
            funcao.append([calculo, xmin])
            print(f'f({xmin}) = {calculo}')
        if '*' in f:
            op_produto = f.index('*')
            calculo = int(f[op_produto - 1]) * xmin
            funcao.append([calculo, xmin])
            print(f'f({xmin}) = {calculo}')
        if '/' in f:
            op_divisao = f.index('/')
            calculo = int(f[op_divisao - 1]) / xmin
            funcao.append([calculo, xmin])
            print(f'f({xmin}) = {calculo}')
        if '^' in f:
            op_potencia = f.index('^')
            calculo = int(f[op_potencia - 1]) ** xmin
            funcao.append([calculo, xmin])
            print(f'f({xmin}) = {calculo}')

        seg_iteracao.append([calculo, xmin])
        print(f'f({xmin}) = {calculo}')
        seg_iteracao_min = min(seg_iteracao)
        pos_min1 = seg_iteracao.index(seg_iteracao_min)
    print(f'\nO ponto de mínimo da segunda iteração é:\nf({seg_iteracao[pos_min1][1]}) = {seg_iteracao[pos_min1][0]}')

    print('\n>>>>>>>>Terceira iteração<<<<<<<<\n')
    ter_iteracao = []
    while xmin > xmin2:
        xmin = xmin - 0.1
        if '+' in f:
            op_soma = f.index('+')
            calculo = int(f[op_soma - 1]) + xmin
            funcao.append([calculo, xmin])
            print(f'f({xmin}) = {calculo}')
        if '-' in f:
            op_subtracao = f.index('-')
            calculo = int(f[op_subtracao - 1]) - xmin
            funcao.append([calculo, xmin])
            print(f'f({xmin}) = {calculo}')
        if '*' in f:
            op_produto = f.index('*')
            calculo = int(f[op_produto - 1]) * xmin
            funcao.append([calculo, xmin])
            print(f'f({xmin}) = {calculo}')
        if '/' in f:
            op_divisao = f.index('/')
            calculo = int(f[op_divisao - 1]) / xmin
            funcao.append([calculo, xmin])
            print(f'f({xmin}) = {calculo}')
        if '^' in f:
            op_potencia = f.index('^')
            calculo = int(f[op_potencia - 1]) ** xmin
            funcao.append([calculo, xmin])
            print(f'f({xmin}) = {calculo}')
        ter_iteracao.append([calculo, xmin])
        print(f'f({xmin}) = {calculo}')
        ter_iteracao_min = min(ter_iteracao)
        pos_min2 = ter_iteracao.index(ter_iteracao_min)
    print(f'\nO ponto de máximo da terceira iteração é:\nf({ter_iteracao[pos_min2][1]}) = {ter_iteracao[pos_min2][0]}')

    print(
        f'\n\n>>>>>>>>Primeira iteração<<<<<<<<\nO ponto de mínimo da primeira iteração é:\nf({funcao[pos_min][1]}) = {funcao[pos_min][0]}')
    print(
        f'\n>>>>>>>>Segunda iteração<<<<<<<<\nO ponto de mínimo da segunda iteração é:\nf({seg_iteracao[pos_min1][1]}) = {seg_iteracao[pos_min1][0]}')
    print(
        f'\n>>>>>>>>Terceira iteração<<<<<<<<\nO ponto de mínimo da terceira iteração é:\nf({ter_iteracao[pos_min2][1]}) = {ter_iteracao[pos_min2][0]}')

    if seg_iteracao_min <= ter_iteracao_min:
        print(
            f'\n>>>>>>>>Conclusão:<<<<<<<<\nSua função é f(x) = {f[0],f[1],f[2]}\nRestrita no domínio [{min_x, max_x}]'
            f'\nO ponto de mínimo, definitivo da função é: \nf({seg_iteracao[pos_min1][1]}) = {seg_iteracao[pos_min1][0]}')
    elif seg_iteracao_min >= ter_iteracao_min:
        print(
            f'\nO ponto de mínimo, definitivo da função é: \nf({ter_iteracao[pos_min2][1]}) = {ter_iteracao[pos_min2][0]}')
