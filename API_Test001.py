from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel, NonEmptyStr, PositiveInt
from tortoise.contrib.fastapi import register_tortoise
from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel, constr, conint
muito foda
app = FastAPI()

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    hashed_password = fields.CharField(128)

    class Meta:
        table = "users"

class Competidor(BaseModel):
    nome: constr(min_length=1)
    idade: conint(gt=0)
    peso: float
    altura: float

class Competidor(Model):
    id = fields.IntField(pk=True)
    nome = fields.CharField(50)
    idade = fields.IntField()
    peso = fields.FloatField()
    altura = fields.FloatField()

    class Meta:
        table = "competidores"

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(username=form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": user.username, "token_type": "bearer"}

@app.post("/competidor/")
async def criar_competidor(nome: str, idade: int, peso: float, altura: float):
    competidor = await Competidor.create(nome=nome, idade=idade, peso=peso, altura=altura)
    return competidor

@app.get("/competidores/")
async def listar_competidores():
    return await Competidor.all()

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['__main__']},
    generate_schemas=True,
    add_exception_handlers=True,
)
