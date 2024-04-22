import time
produto = float(input('\033[1mValor do produto: '))
pagamento = str(input('\033[1mQual a forma de pagamento?(cartão, cheque ou dinheiro): ')).upper().strip()
print('Por favor, aguarde...')
time.sleep(2)
if pagamento == 'CARTÃO':
    condicao = str(input('\033[1;33mPagamento à vista ou parcelado? ')).lower().strip()
    if condicao == 'à vista':
        print(f'\033[1;32mO valor a ser pago será de R${produto - (produto*0.05):.2f}')
    elif condicao == 'parcelado':
        vezes = str(input('\033[1;33mEm quantas vezes?: ')).strip()
        if vezes == '2':
            print(f'\033[1;32mO valor a ser pago será de R${produto:.2f}')
        elif vezes >= '3':
            print(f'\033[1;32mO valor a ser pago será de R${(produto*0.2) + produto}')
elif pagamento == 'CHEQUE':
    print('\033[1;31mSó é possível pagar à vista.')
    pergunta1 = str(input('Deseja prosseguir?(Sim/Não): ')).upper().strip()
    if pergunta1 == 'SIM':
        print(f'\033[1;32mO valor a ser pago será R${produto - (produto*0.1):.2f}')
    elif pergunta1 == 'NÃO':
        print('\033[1;31mFim da seção.')
elif pagamento == 'DINHEIRO':
    print('\033[1;31mSó é possível pagar à vista.')
    pergunta2 = str(input('\033[1;31mDeseja prosseguir?(Sim/Não): ')).upper().strip()
    if pergunta2 == 'SIM':
        print(f'\033[1;32mO valor a ser pago será R${produto - (produto*0.1):.2f}')
    elif pergunta2 == 'NÃO':
        print('\033[1;31mFim da seção.')