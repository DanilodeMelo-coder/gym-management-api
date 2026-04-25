#from database.db import alunos_db, salvar_aluno_db
from datetime import date
from schemas.aluno import Criar_aluno, AlunoUpdate
from sqlalchemy.orm import Session
from models.aluno import Aluno
import uuid



#CRIAR ALUNO
def criar_aluno_service(aluno: Criar_aluno, db: Session):

    if not verificar_cpf(aluno.cpf):
        return {"status": "erro",
        "mensage": "O Cpf informado é invalido",
        "data": None}

    cpf_existente = db.query(Aluno).filter(Aluno.cpf == aluno.cpf).first()
    if cpf_existente:
        return {"status": "erro",
        "mensage": "esse cpf ja esta cadastrado no sistema",
        "data": None}


    if verificar_idade(aluno.data_nascimento):
        return {"status": "erro",
        "mensage": "O usuario ainda não possui a idade minima permitida",
        "data": None}

    email_existente = db.query(Aluno).filter(Aluno.email == aluno.email).first()
    if email_existente:
        return {"status": "erro",
        "mensage": "esse email ja esta cadastrado no sistema",
        "data": None}

    aluno_novo = Aluno(
        id= str(uuid.uuid4()),
        nome= aluno.nome.lower().strip(),
        email= aluno.email,
        cpf= aluno.cpf,
        data_nascimento= aluno.data_nascimento,
        admin= aluno.admin
    )

    db.add(aluno_novo)
    db.commit()
    db.refresh(aluno_novo)

    return {"status": "sucesso",
    "mensage": "Aluno criado com sucesso",
    "data": aluno_novo}


#Listar Alunos
def listar_alunos(db: Session):
    return db.query(Aluno).all()

def buscar_aluno_service(id: str, db: Session):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()

    if not aluno:
        return {"status": "erro", 
        "mensagem": "Aluno não encontrado", 
        "data": None
        }

    return {"status": "sucesso", 
    "mensagem": "Aluno encontrado", 
    "data": aluno
    }

#Atualizar aluno
def atualizar_aluno_service(id: str, dados: AlunoUpdate, db: Session):
    aluno = db.query(Aluno).filter(aluno.id == id).first()

    if not aluno:
        return {"status": "erro",
        "mensage": "Aluno não encontrado",
        "data": None}


    aluno.nome = dados.nome.lower().strip()
    aluno.email = dados.email
    aluno.data_nascimento = dados.data_nascimento

    if dados.admin is not None:
        aluno.admin = dados.admin

    db.commit()
    db.refresh(aluno)


    return {"status": "sucesso",
    "menssage": "dados do aluno atualizados com sucesso",
    "data": aluno
    }


def deletar_aluno_service(id: str, db: Session):
    aluno = db.query(Aluno).filter(aluno.id == id).first()

    if not aluno:
        return {"status": "erro",
        "mensage": "Aluno não encontrado",
        "data": None}

    db.delete(aluno)
    db.commit()

    return {"status": "sucesso",
    "menssage": "Aluno excluido com sucesso",
    "data": aluno
    }


def verificar_idade(data_nascimento):
    hoje = date.today()

    idade = hoje.year - data_nascimento.year

    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -=1

    if idade < 12:
        return True

    return False


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