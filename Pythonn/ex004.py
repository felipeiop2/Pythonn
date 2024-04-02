nome = input('Digite o nome do aluno')
nota = input('Digite uma nota do aluno')
nota2 = input('Digite a segunda nota')
media = (float(nota) + float(nota2)) / 2
print('O aluno {}, {} e {} sua media e : {:.2f}'.format(nome, nota, nota2, media))