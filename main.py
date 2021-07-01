"""
-Programa - criação de uma calculadora de notas em python
-Notas com pesos diferentes e notas de alunos, resultando em notas finais
As pontuações finais do provas é baseado nas seguintes formulas:
25% das notas obtidas na submissão de trabalhos/
55% das notas obtidas via prova/provase
20% das notas obtidas via laboratório
 --A nota será calculada de acordo com:--
1- Pontuação > = 90 : "A"
2- Pontuação > = 80 : "B"
3- Pontuação > = 70 : "C"
4- Pontuação > = 60 : "D"

 Além disso calcule a média total da classe e a média da classe

"""
from helpers import alunos,calc_media_total,atribuir_letra_nota,nota_media_classe
#Aqui começa a execução do código de uma aplicação, usando if__name__=='__name__':
if __name__=='__main__':
    #for looping na lista de alunos e calculo de madias
    for aluno,detalhes in alunos.items():
        print(f"\n{alunos[aluno]['nome']} ")
        print("----------------------")
        media_total_aluno = round(calc_media_total(alunos[aluno]),1)
        print(f"Média de notas do aluno(a) {alunos[aluno]['nome']} é: {media_total_aluno}")
        print(f"Média final do aluno(a) {alunos[aluno]['nome']} é: {atribuir_letra_nota(media_total_aluno)}")
    #nota media classe
    media_classe= nota_media_classe()
    print(f"\nA média da classe é {round(media_classe),1}")
    print(f"Nota final da classe é: {atribuir_letra_nota(media_classe)}")
