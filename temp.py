print("Linha de Produção")

produtoDescartado = 0 #tipo int
produtoDentroDoEsperado = 0 #tipo int
pesoTotalRejeitado = 0.0 #tipo float ou double

while True: #utilizar for
    print("Peso do produto em gramas: ")
    pesoDoProduto = float(input('')) #Equivalente ao scanf, estou lendo um double ou float
    if pesoDoProduto > 250:
        produtoDescartado += 1 # Essa linha é equivalente à produtoDescartado = produtoDescartado + 1
        pesoTotalRejeitado += pesoDoProduto
    else:
        produtoDentroDoEsperado += 1 # Equivalente à produtoDentroDoEsperado = produtoDentroDoEsperado + 1

    print("Digite\n1 para continuar\n2 para mostrar os resultados")
    opcao = int(input("")) #scanf, int
    if opcao == 1:
        continue # continue é usado dentro de um laço de repetição, for, while, dowhile, ele para nesta linha e executa o laço de reptição novamente
    elif opcao == 2: #Equivalente ao else if(opcao==2)
        break # diz para sair do laço de repetição

print("Produtos dentro do esperado: {}".format(produtoDentroDoEsperado))
print("Produtos descartado: {}".format(produtoDescartado))
print("Peso total descartado: {}".format(pesoTotalRejeitado))
