alunos={
    'Jeffersons':
        {
            'nome':'Jefferson Santos',
            'trabalhos':[90,95,80,100],
            'provas':[90,80],
            'laboratorio':[70,85.2]
        },
    'Pedros':
        {
            'nome':'Pedro Silva',
            'trabalhos':[70,95,60,100],
            'provas':[90,60],
            'laboratorio':[70,55.2]
        },
    'Marias':
        {
            'nome':'Jefferson Santos',
            'trabalhos':[77,82,23,39],
            'provas':[89,95],
            'laboratorio':[80,80]
        },
    'Angelas':
        {
            'nome':'Angela Silveira',
            'trabalhos':[67,55,77,21],
            'provas':[80,60],
            'laboratorio':[69,44,56]
        },
    'Marcos':
        {
            'nome':'Marcos Saito',
            'trabalhos':[95,89,90,86],
            'provas':[65,56],
            'laboratorio':[50,40.6]
        }
}
#Obter médias das notas
def obter_media (notas):
    """
    Função para obter a media das notas informadas-Lista-
    :param notas: recebe notas provas, trabalhos e laboratorios
    :return: media das notas informadas
    """
    total_soma = sum(notas)
    total_soma = float(total_soma)
    return total_soma/len(notas)

#Média com base nos pesos
def calc_media_total(aluno):
    """
    Função que calcula a media por tipo/pesos
    :param aluno: Dicionário de alunos
    :return:Média final com base nos pesos
    """
    #25% trabalhos
    #55% provas
    #20% laboratório

    trabalhos = obter_media(aluno['trabalhos'])
    provas = obter_media(aluno['provas'])
    laboratorio = obter_media(aluno['laboratorio'])
    return ((0.25*trabalhos) + (0.55*provas) + (0.20*laboratorio))

#Atribuir a média à letra

def atribuir_letra_nota(nota_final_aluno):
    """Função que atribui a uma letra à nota conforme seu peso

    :param nota_final_aluno: nota com base nos pesos
    :return:noat letra com base na nota final
    """
    if nota_final_aluno >= 90:
        return 'A'
    elif nota_final_aluno >= 80:
        return 'B'
    elif nota_final_aluno >= 70:
        return 'C'
    elif nota_final_aluno >= 60:
        return 'D'
    else:
        return 'F'

#Média da classe

def nota_media_classe ():
    """
    Função para calculo da média da classe
    :return: média final dos alunos
    """
    resultado_lista=[]
    for aluno, detalhes in alunos.items():
        media_aluno = calc_media_total(alunos[aluno])
        resultado_lista.append(media_aluno)
    return obter_media(resultado_lista)

