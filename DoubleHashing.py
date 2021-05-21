# Implementação de Double Hashing

class doubleHashTable:

    def __init__(self):
        self.size = int(input("Digite o tamanho do hash table: "))
        self.num = 5
        #Inicializando as posições em 0
        self.table = list(0 for i in range(self.size))
        self.elementCount = 0
        self.comparisons = 0

    # Método para verificar se a tabela está cheia
    def isFull(self):
        if self.elementCount == self.size:
            return True
        return False

    # método hash 1
    def h1(self, element):
        return element % self.size

    #método hash 2
    def h2(self, element):
        return element % self.num

    def doubleHashing(self, element, position):
        posFound = False
        # limit variable is used to restrict the function from going into infinite loop
        limit = 50
        i = 2
        #Iniciando o looping para encontrar uma posição
        while i <= limit:
            newPosition = (i * self.h1(element) + self.h2(element)) % self.size
            # Se a nova posição estiver vazia retorna a nova posição e da um break
            if self.table[newPosition] == 0:
                posFound = True
                break
            else:
                # se a nova posiçaõ não estiver vazia, aumenta o valor de i
                i += 1
        return posFound, newPosition

    #Método para inserir os valores na tabela
    def insert(self, element):
        #Verificando se a tabela está cheia
        if self.isFull():
            print("Hash Table cheia.")
            return False

        posFound = False

        position = self.h1(element)

        #Checando se a posição está vazia
        if self.table[position] == 0:
            # posição encontrada, inserindo o valor na posição e imprimindo a mensagem
            self.table[position] = element
            print("Elemento " + str(element) + " na posição " + str(position))
            isStored = True
            self.elementCount += 1
        #verifica se ocorreu alguma colisão e busca nova posição para o elemento
        else:
            while not posFound:
                print("Colisão ocorreu para o elemento " + str(element) + " na posição " + str(
                    position) + " buscando nova posição.")
                posFound, position = self.doubleHashing(element, position)
                if posFound:
                    self.table[position] = element
                    self.elementCount += 1

        return posFound

    # método para buscar um elemento na tabela
    def search(self, element):
        found = False
        position = self.h1(element)
        self.comparisons += 1

        if (self.table[position] == element):
            return position
        else:
            limit = 50
            i = 2
            newPosition = position
            # começando um loop para encontrar a posição
            while i <= limit:
                # calculando a nova posição pelo double hashing
                position = (i * self.h1(element) + self.h2(element)) % self.size
                self.comparisons += 1

                if self.table[position] == element:
                    found = True
                    break
                elif self.table[position] == 0:
                    found = False
                    break
                else:
                    i += 1
            if found:
                return position
            else:
                print("Elemento não encontrado.")
                return found
    # método para remover um elemento do hash table
    def remove(self, element):
        position = self.search(element)
        if position is not False:
            self.table[position] = 0
            print("Elemento " + str(element) + " foi deletado.")
            self.elementCount -= 1
        else:
            print("Elemento não se encontra no Hash Table")
        return

    # método para mostrar os valores do hash table
    def display(self):
        print("\n")
        for i in range(self.size):
            print(str(i) + " = " + str(self.table[i]))
        print("O número de elementos da tabela hash são: " + str(self.elementCount))

table1 = doubleHashTable()

table1.insert(12)
table1.insert(26)
table1.insert(31)
table1.insert(17)
table1.insert(90)
table1.insert(28)
table1.insert(88)
table1.insert(40)
table1.insert(77)

table1.display()
print()

print("A posição do elemento 31 é: " + str(table1.search(31)))
print("A posição do elemento 28 é: " + str(table1.search(28)))
print("A posição do elemento 90 é: " + str(table1.search(90)))
print("A posição do elemento 77 é: " + str(table1.search(77)))
print("A posição do elemento 1 é: " + str(table1.search(1)))
print("\nNúmero total de comparações na busca = " + str(table1.comparisons))
print()

table1.display()