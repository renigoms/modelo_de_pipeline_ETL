import controlador_banco
from ChatBot import ChatBotLocal
from Extract import Extract


class TranformarDados:
    def __init__(self):
        self.chatbot = ChatBotLocal()

    def _gerar_mensagens_de_bem_estar(self, user):
        lista_de_mensagens = [
            "A prática regular de exercícios físicos pode melhorar sua saúde mental e seu humor.",
            "Uma alimentação balanceada é essencial para manter a saúde em dia.",
            "Dormir bem é fundamental para a recuperação física e mental.",
            "A meditação pode ajudar a reduzir o estresse e a ansiedade.",
            "Manter-se hidratado é importante para todas as funções do corpo.",
            "Passar tempo ao ar livre pode melhorar seu bem-estar geral.",
            "Rir é um ótimo remédio para o estresse e pode melhorar o sistema imunológico.",
            "O equilíbrio entre trabalho e vida pessoal é crucial para o bem-estar.",
            "Estabelecer metas realistas pode aumentar sua satisfação com a vida.",
            "A gratidão pode melhorar seu bem-estar emocional e sua saúde."
        ]

        lista_de_mensagens.extend([
            "A determinação de hoje é o sucesso de amanhã.",
            "A determinação é o caminho para o sucesso.",
            "Com determinação, todos os obstáculos podem ser superados.",
            "A determinação é a chave para alcançar seus sonhos.",
            "Nunca subestime o poder da determinação.",
            "A determinação é a força motriz por trás de todas as conquistas.",
            "A determinação é a faísca que acende a chama do sucesso.",
            "A determinação é o que transforma sonhos impossíveis em realidades alcançáveis.",
            "A determinação é o motor que nos impulsiona a superar os desafios mais difíceis.",
            "A determinação é a ponte entre o sonho e a realização.",
            "A determinação é o ingrediente secreto do triunfo.",
            "A determinação é o que nos faz persistir quando tudo parece perdido."
        ])

        self.chatbot.realizar_treinamento(lista_de_mensagens)
        return self.chatbot.get_resposta(user[1])

    def adicionar_frase(self):
        extract = Extract()
        self.chatbot.chat_bot.storage.drop()
        lista_users = []
        for user in extract.users:
            frase = self._gerar_mensagens_de_bem_estar(user)
            listaUser = list(user)
            listaUser[3] = frase
            lista_users.append(listaUser)
        return lista_users



# TranformarDados().adicionar_frase()