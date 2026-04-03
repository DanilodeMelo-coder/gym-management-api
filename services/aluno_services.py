from database.db import alunos_db, salvar_aluno_db

#FUNÇOES SERVICES PRINCIPAIS

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
                "menssage": "Nome duplicado",
                "data": None}

        else:
            if idade_verificada:
                return {"status": "erro",
                "menssage": "O usuario ainda não possui a idade minima permitida",
                "data": None}

            else:
                salvar_aluno_db(aluno)

                return {"status": "sucesso",
                    "menssage": "Aluno criado com sucesso",
                    "data": aluno}


def atualizar_aluno_service(id, nome, idade):

    nome = nome.lower().strip()

    aluno_procurado= buscar_aluno_id(id)

    nome_vazio = verificar_nome_vazio(nome)

    if aluno_procurado is not None:

        if nome_vazio:

            return {"status": "erro",
                "mensage": "Nome vazio",
                "data": None}
        
        else:

            aluno_procurado.nome = nome
            aluno_procurado.idade = idade

            return {"status": "sucesso",
                        "menssage": f"dados do aluno {aluno_procurado.nome} atualizados com sucesso",
                        "data": aluno_procurado
                        }

    else:
        return {"status": "Erro",
                    "menssage": "Aluno não encontrado",
                    "data": None
                    }

def deletar_aluno_service(id):
    
    aluno_procurado = buscar_aluno_id(id)

    if aluno_procurado is not None:

        alunos_db.remove(aluno_procurado)

        return {"status": "sucesso",
                "menssage": "Aluno excluido com sucesso",
                "data": aluno_procurado
                }

    return {"status": "Erro",
            "menssage": "Aluno não encontrado",
            "data": None
            }



#FUNÇOES SERVICES SECUNDARIAS

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

def buscar_aluno_id(id):

    for aluno in alunos_db:
        if aluno.id == id:

            return aluno
        
    return None