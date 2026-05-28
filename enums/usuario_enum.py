from enum import Enum


class TipoUsuario(str, Enum):
    aluno = "aluno"
    personal = "personal"
    admin = "admin"