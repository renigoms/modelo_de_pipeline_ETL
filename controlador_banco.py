from ConexaoBanco import ConexaoBanco


def _acessar_bd(comandoSql):
    ditioDadosBd = {
        'host': "localhost",
        'user': "root",
        'password': "",
        'database': "sistemaetl"
    }

    resultado = []

    with ConexaoBanco(**ditioDadosBd) as conBanco:
        conBanco.execute(comandoSql)
        resultado = conBanco.fetchall()

    return resultado


def get_usuarios():
    lista = _acessar_bd("select * from clientes")
    return lista

def update_resgistro(id, coluna, alteracao):
    _acessar_bd(f"update clientes set {coluna} = '{alteracao}' where id = {id}")