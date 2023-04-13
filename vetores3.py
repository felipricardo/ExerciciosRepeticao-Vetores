"""
VETORES3 - Faça um programa para corrigir provas de múltipla escolha com somatória. Cada prova tem dez questões e cada
 questão vale 1 ponto. O primeiro conjunto de dados a ser lido é o gabarito da prova. Os outros dados serão os números
  dos alunos e sua respectivas respostas. Existem 15 alunos matriculados. Calcule e mostre:
- Para cada aluno seu número e sua nota;
- A percentagem de aprovação, sabendo-se que a nota mínima é 6,0
"""
gaba = [0] * 10
print("Digite o gabarito da prova: ")
for i in range(10):
    print("Questao ", i+1, ":")
    gaba[i] = int(input())

for aluno in range(15):
    print("aluno: ", aluno+1)
    nota = 0
    for questao in range(10):
        print("resp questao", questao+1,":")
        resp = int(input())
        if resp == gaba[questao]:
            nota += 1
    print("A nota e :", nota)
