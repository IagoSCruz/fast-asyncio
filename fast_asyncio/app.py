from http import HTTPStatus

from fastapi import FastAPI

from fast_asyncio.schemas import Message, UserPublic, UserSchema

app = FastAPI(title='API de Cadastros')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, mundo!'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user
