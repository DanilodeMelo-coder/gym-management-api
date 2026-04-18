from database.db import alunos_db, salvar_aluno_db
from datetime import date
from models.aluno import Criar_aluno, Aluno

#FUNÇOES SERVICES PRINCIPAIS

def criar_aluno_service(aluno: Criar_aluno):

    aluno = Aluno(**aluno.model_dump())

    aluno.nome = aluno.nome.lower().strip()

    if verificar_nome_vazio(aluno.nome):
        return {"status": "erro",
        "mensage": "Nome vazio",
        "data": None}

    if not verificar_cpf(aluno.cpf):
        return {"status": "erro",
        "mensage": "O Cpf informado é invalido",
        "data": None}

    if verificar_cpf_duplicados(aluno.cpf):
        return {"status": "erro",
        "mensage": "esse cpf ja esta cadastrado no sistema",
        "data": None}


    if verificar_idade(aluno.data_nascimento):
        return {"status": "erro",
        "mensage": "O usuario ainda não possui a idade minima permitida",
        "data": None}

    salvar_aluno_db(aluno)

    return {"status": "sucesso",
    "mensage": "Aluno criado com sucesso",
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


def verificar_cpf(cpf):

    cpf = cpf.replace(".", "").replace("-","")

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range (9))
    digito1 = (soma * 10 % 11) % 10

    if digito1 != int(cpf[9]):
        return False


    soma = sum(int(cpf[i]) * (11 - i) for i in range (10))
    digito2 = (soma * 10 % 11) % 10

    if digito2 != int(cpf[10]):
        return False

    return True