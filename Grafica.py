# decoração para o titulo
def borda(s1):
    tam = len(s1)
    # lógica
    if tam:
        print('\033[95m+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+\033[0m')

# cabeçalho com as escolhas
# escolha do serviço principal
def escolha_pedido():
    while True:
        servico = input('Entre com o tipo de serviço desejado!\n'
                        '\033[1mDIG\033[0m - Digitalização\n'
                        '\033[1mICO\033[0m - Impressão Colorida\n'
                        '\033[1mIPB\033[0m - Impressão Preto e Branco\n'
                        '\033[1mFOT\033[0m - Fotocópia\n'
                        '>> ').upper()
        if servico in ['DIG', 'ICO', 'IPB', 'FOT']:
            return servico
        else:
            print('\033[91mEscolha inválida, entre com o tipo do serviço novamente!\033[0m')

# escolha dos numeros de paginas
def num_pagina():
    while True:
        try:
            paginas = int(input('Entre com o número de páginas: '))
            if paginas < 20:
                return paginas
            elif 20 <= paginas < 200:
                return int(paginas * 0.85)
            elif 200 <= paginas < 2000:
                return int(paginas * 0.80)
            elif 2000 <= paginas < 20000:
                return int(paginas * 0.75)
            else:
                print('\033[91mNão aceitamos tantas páginas de uma vez.\n'
                      'Por favor, entre com o número de páginas novamente!\033[0m')
        except ValueError:
            print('\033[91mDigite um valor, por favor!\033[0m')

# escolha dos serviços extras
def servico_extra():
    while True:
        extra = input('Deseja adicionar algum serviço?\n'
                      '\033[1m1\033[0m - Encadernação Simples - R$ 15,00\n'
                      '\033[1m2\033[0m - Encadernação Capa Dura - R$ 40,00\n'
                      '\033[1m0\033[0m - Não desejo mais nada\n'
                      '>> ')
        if extra in ['0', '1', '2']:
            return int(extra)
        else:
            print('\033[91mOpção de serviço inválida!\033[0m')

# titulo
borda('Copiadora da Camila!')

# escolha dos serviços
servico = escolha_pedido()

# desconto das paginas
paginas = num_pagina()

# escolha dos adicionais
extra = servico_extra()

# calculos dos valores finais
valor_servico = 0
if servico == 'DIG':
    valor_primario = 1.10
    valor_servico = 1.10 * paginas
elif servico == 'ICO':
    valor_primario = 1.00
    valor_servico = 1 * paginas
elif servico == 'IPB':
    valor_primario = 0.40
    valor_servico = 0.4 * paginas
elif servico == 'FOT':
    valor_primario = 0.20
    valor_servico = 0.2 * paginas

# calculo dos adicionais
valor_extra = 0
if extra == 1:
    valor_extra = 15
elif extra == 2:
    valor_extra = 40

# total
total = valor_servico + valor_extra

print(f'Total de R$ {total:.2f} \033[1m(serviço: {valor_primario:.2f} * páginas: {paginas} '
      f'+ extra: {valor_extra:.2f})\033[0m')
