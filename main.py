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
alunos={
    'Jeffersons':
        {
            'nome':'Jefferson Santos',
            'trabalhos':[90,95,80,100],
            'provas':[90,80],
            'laboratorio':[70,85.2]
        }
    'Pedros':
        {
            'nome':'Pedro Silva',
            'trabalhos':[70,95,60,100],
            'provas':[90,60],
            'laboratorio':[70,55.2]
        }
    'Marias':
        {
            'nome':'Jefferson Santos',
            'trabalhos':[77,82,23,39],
            'provas':[89,95],
            'laboratorio':[80,80]
        }
    'Angelas':
        {
            'nome':'Angela Silveira',
            'trabalhos':[67,55,77,21],
            'provas':[80,60],
            'laboratorio':[69,44,56]
        }
    'Marcos':
        {
            'nome':'Marcos Saito',
            'trabalhos':[95,89,90,86],
            'provas':[65,56],
            'laboratorio':[50,40.6]
        }
}