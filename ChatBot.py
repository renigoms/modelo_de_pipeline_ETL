from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


class ChatBotLocal:
    def __init__(self):
        self.chat_bot = ChatBot("Alexa", tagger_language=ENGSM)
        self.trainer = ListTrainer(self.chat_bot)
        self._erro_spacy()

    def _erro_spacy(self):
        download("en_core_web_sm")

    def realizar_treinamento(self, lista_de_treinamento):
        self.trainer.train(lista_de_treinamento)

    def get_resposta(self, pergunta):
        return self.chat_bot.get_response(pergunta)