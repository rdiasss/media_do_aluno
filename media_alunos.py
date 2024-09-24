alunos = {}

for i in range(5):
    nome = input(f'Digite o nome do aluno {i+1}: ')
    
    notas = []
    for j in range(3):
        nota = float(input(f'Digite a nota {j+1} de {nome}: '))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    
    alunos[nome] = media

print('\nMédia dos Alunos:')
for nome, media in alunos.items():
    print(f"{nome}: {media:.2f}")
