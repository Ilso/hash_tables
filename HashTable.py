class Hash:
    def __init__(self, tamanho):
        self.tabela = {}
        self.tamanho_maximo = tamanho

    #Função Hash
    def funcao_hash(self, chave):
        v = int(chave)
        return v%self.tamanho_maximo

    #Função para verificar se tabela está cheia
    def tabela_cheia(self):
        return len(self.tabela) == self.tamanho_maximo

    #Função para inserir um valor na tabela
    def inserir(self, valor):
        if self.tabela_cheia():
            print('Tabela está cheia.')
            return
        posicao = self.funcao_hash(valor)
        if self.tabela.get(posicao) == None:
            self.tabela[posicao] = valor
            print(f'Valor {valor} inserido na posição {posicao}!')
        else:
            print(f'Posição já ocupada. {self.tabela.get(valor)}')

    #Função para imprimir um valor
    def imprimir(self):
        for i in self.tabela:
            print(f'Hash {i}')
            print(f'Valor: {self.tabela[i]}')

    #Função para buscar um valor
    def buscar(self, chave):
        posicao = self.funcao_hash(chave)
        if self.tabela.get(posicao) == None:
            return -1
        if self.tabela[posicao] == chave:
            return posicao
        return -1

while True:
    tamanho_hash = int(input('Digite o tamanho da tabela: '))
    tab = Hash(tamanho_hash)
    print(f'Tabela Hash sem colisões com tamanho de {tamanho_hash} espaços!')
    for i in range(0, tamanho_hash):
        print(f'Inserindo elemento {i + 1}')
        valor = input('Digite um valor para inserir: ')
        tab.inserir(valor)
    tab.imprimir()
    valor = input('Digite um valor para buscar: ')
    posicao = tab.buscar(valor)
    if posicao == -1:
        print('Item não encontrado!')
    else:
        print(f'Item encontrado na posição {posicao}!')

    # zuera kkk
    condicao = input('Deseja continuar? ')
    if condicao == 's':
        continue
    else:
        break




