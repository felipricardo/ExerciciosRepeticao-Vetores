* VETORES1 - Faça um programa que carregue dois vetores de dez elementos numéricos cada um e mostre um vetor resultante da intercalação desses dois vetores.

* VETORES2 - Faça um programa que carregue dois vetores, X e Y, com dez números inteiros cada um. Considere que os números de cada vetor digital, X e Y, não podem estar repetidos. Calcule e mostre os seguintes vetores resultantes:
a.	a união de X com Y (todos os elementos de X e os elementos de Y que não estejam em X)
b.	a diferença entre X e Y (todos os elementos de X que não existam em Y)
c.	a soma entre X e Y (soma de cada elemento de X com o elemento de mesma posição em Y)
d.	produto entre X e Y (multiplicação de cada elemento de X com o elemento de mesma posição em Y)
e.	a interseção entre X e Y (apenas os elementos que aparecem nos dois vetores)

* VETORES3 - Faça um programa para corrigir provas de múltipla escolha com somatória. Cada prova tem dez questões e cada questão vale 1 ponto. O primeiro conjunto de dados a ser lido é o gabarito da prova. Os outros dados serão os números dos alunos e sua respectivas respostas. Existem 15 alunos matriculados. Calcule e mostre:
- Para cada aluno seu número e sua nota;
- A percentagem de aprovação, sabendo-se que a nota mínima é 6,0
	VETORES4 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em um vetor. Calcule e mostre a maior e a menor temperatura do ano e em que mês elas ocorreram (mostrar o mês por extenso: 1- Janeiro, 2 – Fevereiro). Desconsidere empates.

* VETORES5 - Faça um programa que receba a quantidade de peças vendidas por vendedor e armazene essas quantidades em um vetor. Receba também o preço da peça vendida de cada vendedor e armazene esses preços em outro vetor. Existem apenas dez vendedores e cada vendedor pode vender apenas um tipo de peça, isto é, para cada vendedor existe apenas um preço. Calcule e mostre a quantidade total de peças vendidas por todos os vendedores e para cada vendedor calcule e mostre o valor total da venda, isto é, a quantidade de peças * o preço da peça.


* VETORES6 - Faça um programa que simule um controle bancário. Para tanto, devem ser lidos os códigos de dez contas e os seus respectivos saldos. Os códigos devem ser armazenados em um vetor de números inteiros (não pode haver mais que uma conta com o mesmo código) e os saldos devem ser armazenados em um vetor de números reais. O saldo deverá ser cadastrado na mesma posição do código. Por exemplo, se a conta 504 for armazenada na quinta posição do vetor de saldos. Depois de fazer a leitura dos valores, mostrar o seguinte menu na tela:

i.	Efetuar depósito
ii.	Efetuar saque
iii.	Consultar o ativo bancário (ou seja, o somatório dos saldos de todos os clientes)
iv.	Finalizar o programa
Para efetuar depósito deve-se solicitar o código da conta e o valor a ser depositado. Se a conta não estiver cadastrada, mostrar a mensagem Conta não encontrada e voltar ao menu. Se a conta existir, atualizar o seu saldo.
Para efetuar saque deve-se solicitar o código da conta e o valor a ser sacado. Se a conta não estiver cadastrada, mostrar a mensagem Conta não encontrada e voltar ao menu. Se a conta existir, verificar se o seu saldo é suficiente para cobrir o saque. (Estamos supondo que a conta não pode ficar com o saldo negativo). Se o saldo for suficiente, realizar o saque e voltar ao menu. Caso contrário mostrar a mensagem Saldo insuficiente e voltar ao menu.
Para consultar o ativo bancário deve-se somar o saldo de todas as contas do banco. Depois de mostrar esse valor, voltar ao menu.
O programa só termina quando for digitada a opção 4 – Finalizar o programa.

* VETORES7 - Uma empresa possui ônibus com 48 lugares (24 nas janelas e 24 no corredor). Faça um programa que utilize dois vetores para controlar as poltronas ocupadas no corredor e na janela. Considere que zero representa poltrona desocupada e um representa poltrona ocupada.

          +---+---+---+---+---+---+---+---+
JANELA    | 0 | 1 | 0 | 0 |   | 1 | 1 | 1 |
          +---+---+---+---+---+---+---+---+
Poltrona    1   2   3   4  ...  22  23  24
          +---+---+---+---+---+---+---+---+
CORREDOR  | 0 | 1 | 0 | 0 |   | 0 | 0 | 1 |
          +---+---+---+---+---+---+---+---+

Esse programa deve controlar a venda de passagens da seguinte maneira:
	O cliente informa se deseja poltrona no corredor ou na janela e, depois, o programa deve informar quais poltronas estão disponíveis para a venda;
	Quando não existirem poltronas livres no corredor, nas janelas ou, ainda, quando o ônibus estiver completamente cheio, deve ser mostrada uma mensagem.
