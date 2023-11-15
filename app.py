from fastapi import FastAPI, Request, Response, Form, status, Depends
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session

import models
from database import SessionLocal,engine

templates = Jinja2Templates(directory='templates')

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    return templates.TemplateResponse('base.html',
                                      {'request': request, 'todo_list': todos})


