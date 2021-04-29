def origem_destino_iguais(origem, destino, lista_de_erros):
    """ Verifica se origem do destino sao iguais"""
    if origem == destino:
            lista_de_erros ['destino'] = 'Origem e destino nao pode ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """ Verifica se existe algum caractere numerico"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros [nome_campo]= 'Nao inclua numeros neste campo'

def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """ verifica se data de ida e maior que data de volta  """
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta nao pode ser maior que data de ida'

def data_ida_menor_que_data_de_hoje(data_ida, data_pesquisa, lista_de_erros):
    """ Verifica se data de ida e mmenor que data de hoje """
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida nao pode ser menor que hoje'