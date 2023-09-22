import pandas as pd

import controlador_banco


class Extract:
    def __init__(self):
        self.data_frame = pd.read_csv("ArqIds.csv")
        self.user_id = self.data_frame['ID_CLIENTES'].tolist()
        self.users = self._extrair_usuario()

    def get_user(self, id):
        for cliente in controlador_banco.get_usuarios():
            if cliente[0] == id:
                return cliente

    def _extrair_usuario(self):
        return [user for id in self.user_id if (user := self.get_user(id)) is not None]

    def users_list(self):
        print(self.users)
#
# extract = Extract()
# print(extract.get_user(1)[1])
