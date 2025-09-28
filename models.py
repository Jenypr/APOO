from dataclasses import dataclass
from typing import Optional

@dataclass
class Item:
    id: Optional[int]  # None antes de persistir
    nome: str
    descricao: str
    quantidade: int