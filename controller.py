from typing import List
from models import Item
from dao import ItemDAO

class ItemController:
    def __init__(self, dao: ItemDAO = None):
        self.dao = dao or ItemDAO()

    def criarItem(self, nome: str, descricao: str, quantidade: int) -> Item:
        nome = nome.strip()
        descricao = descricao.strip() if descricao else ""
        if not nome:
            raise ValueError("Nome do item não pode ser vazio.")
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")

        item = Item(id=None, nome=nome, descricao=descricao, quantidade=int(quantidade))
        saved = self.dao.adicionar(item)
        return saved

    def obterTodosOsItens(self) -> List[Item]:
        return self.dao.listarTodos()