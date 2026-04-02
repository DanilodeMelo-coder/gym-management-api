from database.db import alunos_db, salvar_aluno_db


def criar_aluno_service(aluno):

    aluno.nome = aluno.nome.lower().strip()

    duplicado = verificar_nome_duplicados(aluno.nome)
    nome_vazio = verificar_nome_vazio(aluno.nome)
    idade_verificada = verificar_idade(aluno.idade)

    if nome_vazio:

        return {"status": "erro",
                "mensage": "Nome vazio",
                "data": None}
    else:
        if duplicado:
            return {"status": "erro",
                "mensage": "Nome duplicado",
                "data": None}

        else:
            if idade_verificada:
                return {"status": "erro",
                "mensage": "O usuario ainda não possui a idade minima permitida",
                "data": None}

            else:
                salvar_aluno_db(aluno)

                return {"status": "sucesso",
                    "mensage": "Aluno criado com sucesso",
                    "data": aluno}


def verificar_nome_duplicados(nome):
    for nome_db in alunos_db:
        if nome_db.nome== nome:

            return True
    return False

def verificar_nome_vazio(nome):
    if nome == "":

        return True
    return False

def verificar_idade(idade):
    if idade <= 12:

        return True
    return False
