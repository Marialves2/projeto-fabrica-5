nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7.0:
    status = "Aprovado 🎉"
else:
    status = "Reprovado 😢"

print(f"\nNome do aluno: {nome}")
print(f"Notas: {nota1}, {nota2}, {nota3}, {nota4}")
print(f"Média: {media:.2f}")
print(f"Status: {status}")
