from enum import Enum


class TipoExercicio(str, Enum):
    base = "base"
    customizado = "customizado"