import controlador_banco
from Transformer_dados import TranformarDados


def update_user():
    for user in TranformarDados().adicionar_frase():
        controlador_banco.update_resgistro(user[0], "mensagem_de_bem_estar", user[3])


if __name__ == '__main__':
    update_user()
