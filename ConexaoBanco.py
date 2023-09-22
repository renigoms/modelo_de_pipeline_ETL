import mysql.connector
class ConexaoBanco:
    def __init__(self, **dictDadosConection):
        self.dictDadosConection = dictDadosConection
        self.connection = None
        self.cursorBD = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(**self.dictDadosConection)
            self.cursorBD = self.connection.cursor()
            return self.cursorBD
        except:
            raise Exception("Conexão mal sucedida!!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.cursorBD.close()
        self.connection.close()




