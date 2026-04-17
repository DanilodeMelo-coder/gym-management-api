from database.db import alunos_db, salvar_aluno_db
from datetime import date

#FUNÇOES SERVICES PRINCIPAIS

def criar_aluno_service(aluno):

    aluno.nome = aluno.nome.lower().strip()

    cpf_existente = verificar_cpf_duplicados(aluno.cpf)
    nome_vazio = verificar_nome_vazio(aluno.nome)
    idade_verificada = verificar_idade(aluno.data_nascimento)

    if nome_vazio:

        return {"status": "erro",
                "mensage": "Nome vazio",
                "data": None}
    else:
        if cpf_existente:
            return {"status": "erro",
                "menssage": "esse cpf ja esta cadastrado no sistema",
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

def verificar_cpf_duplicados(cpf):
    for nome_db in alunos_db:
        if nome_db.cpf== cpf:

            return True
    return False

def verificar_nome_vazio(nome):
    if nome == "":

        return True
    return False


def verificar_idade(data_nascimento):
    hoje = date.today()

    idade = hoje.year - data_nascimento.year

    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -=1

    if idade < 12:
        return True

    return False


def buscar_aluno_id(id):

    for aluno in alunos_db:
        if aluno.id == id:

            return aluno
        
    return None