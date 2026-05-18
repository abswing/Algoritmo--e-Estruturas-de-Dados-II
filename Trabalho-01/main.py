class Nodo:
    def __init__(self, valor: int, proximo: 'Nodo' = None):
        self.valor = valor
        self.proximo = proximo


class Lista:
    def __init__(self):
        self.head: Nodo | None = None

    def inserir(self, valor: int):
        novo = Nodo(valor)
        if not self.head:
            self.head = novo
            return
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo

    def listar (self) -> list:
        lista = []
        atual = self.head
        while atual:
            lista.append(atual.valor)
            atual = atual.proximo
        return lista

    def preencher(self, arr: list):
        self.head = None
        for v in arr:
            self.inserir(v)

    # ---------- Merge Sort (lista encadeada) ----------#
    
    def merge_sort(self):
        def dividir(lista):
            if not lista or not lista.proximo:
                return lista
            lento = lista
            rapido = lista.proximo
            while rapido and rapido.proximo:
                lento = lento.proximo
                rapido = rapido.proximo.proximo
            meio = lento.proximo
            lento.proximo = None
            esquerda = dividir(lista)
            direita = dividir(meio)
            return mesclar(esquerda, direita)
        
        def mesclar(no_a, no_b):
            if not no_a:
                return no_b
            if not no_b:
                return no_a
            
            if no_a.valor <= no_b.valor:
                resultado = no_a
                resultado.proximo = mesclar(no_a.proximo, no_b)
            else:
                resultado = no_b
                resultado.proximo = mesclar(no_a, no_b.proximo)
            return resultado

        self.head = dividir(self.head)


    # ---------- Quick Sort (lista encadeada) ----------#

    def quick_sort(self):
        def quicksort(head):
            if head is None or head.proximo is None:
                return head
            
            pivo = head.valor
            esquerda = None
            direita = None
            atual = head.proximo

            while atual:
                if atual.valor < pivo:
                    esquerda = Nodo(atual.valor, esquerda)
                else:
                    direita = Nodo(atual.valor, direita)
                atual = atual.proximo

            esquerda = quicksort(esquerda)
            direita = quicksort(direita)

            nodo_pivo = Nodo(pivo, direita)

            if esquerda is None:
                return nodo_pivo
            else:
                atual_esquerda = esquerda
                
                while atual_esquerda.proximo:
                    atual_esquerda = atual_esquerda.proximo
                atual_esquerda.proximo = nodo_pivo
                return esquerda
            
        self.head = quicksort(self.head)

        
      

        

# 1. Criei a instância da classe
minha_lista = Lista()

# 2. criei a lista bagunçada 
dados_baguncados = [38, 27, 43, 3, 9, 82, 10]

# 3. TESTE DO PREENCHER (Entrada)
# Ele vai pegar o array acima e criar os Nodos um por um
minha_lista.preencher(dados_baguncados)
print(f"Dados carregados na estrutura personalizada.")

# 4. TESTE DO LISTAR (Saida antes da ordenação)
# Ele percorre os Nodos e gera uma lista Python para o print ler
print("Antes de ordenar: ", minha_lista.listar())

#5 teste do listar( saida depois da ordenação)
minha_lista.merge_sort()
print("depois de ordenar: merge_sort ", minha_lista.listar())

minha_lista.quick_sort()
print("depois de ordenar: quick_sort ", minha_lista.listar())