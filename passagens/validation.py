def origem_destino_iguais(origem, destino, lista_erros):
    """ Verifica se os campos de origem de destino não são iguais """
    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não podem ser iguais!'
    
def campo_sem_numero(valor_campo, nome_campo, lista_erros):
    """ Verifica se os campos não possuem números """
    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = 'O campo origem não pode conter números!'

def data_ida_menor_que_data_volta(data_ida, data_volta, lista_erros):
    """ Verifica se a data de ida é menor que a data de volta """
    if data_ida > data_volta:
        lista_erros['data_volta'] = 'A data volta não pode ser menor que a data de ida!'

def data_ida_menor_que_data_atual(data_ida, data_pesquisa, lista_erro):
    """ Verifica se a data de ida não é menor que a data atual """
    if data_ida < data_pesquisa:
        lista_erro['data_ida'] = 'A data de ida não pode ser menor que a data de hoje'