from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


class ChatBotLocal:
    def __init__(self):
        self.chat_bot = ChatBot("Alexa", tagger_language=ENGSM)
        self.trainer = ListTrainer(self.chat_bot)
        self.erro_spacy()

    def erro_spacy(self):
        download("en_core_web_sm")

    def realizar_treinamento(self, lista_de_treinamento):
        self.trainer.train(lista_de_treinamento)

    def get_resposta(self, pergunta):
        return self.chat_bot.get_response(pergunta)

    def limpar_banco_chatbot(self):
        if input("Digite a senha ->") == "renan123":
            self.chat_bot.storage.drop()
            return
        print("Senha inválida!")

# chatbot = ChatBotLocal()
# chatbot.limpar_banco_chatbot()