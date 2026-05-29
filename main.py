from fastapi import FastAPI
from routes.aluno_routes import router as aluno_router
from routes.exercicio_routes import router as exercicio_router
from routes.auth_routes import router as auth_router
from core.database import engine, Base

Base.metadata.create_all(bind= engine)

app = FastAPI()


app.include_router(aluno_router)
app.include_router(exercicio_router)
app.include_router(auth_router)



