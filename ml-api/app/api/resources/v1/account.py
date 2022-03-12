from fastapi import (APIRouter, Depends, Form, HTTPException)
# from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

# from databases.connect import get_db
from api.entities import account as account_entity
from securities import token as token_helper
from settings import config


router = APIRouter()


@router.post("/login/access-token", response_model = account_entity.Token)
def login_access_token( 
    # db_session: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)
):
    if form_data.username != config.USER or form_data.password != config.PASSWORD:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    token_create = account_entity.TokenCreate(user_name= form_data.username,password= form_data.password)
    access_token, access_token_expire  = token_helper.create_access_token(token_create.__dict__)
    refresh_token, refresh_token_expire = token_helper.create_fresh_token(token_create.__dict__)
    
    token = account_entity.Token(
        access_token = access_token, 
        refresh_token = refresh_token,
        expire_token= access_token_expire,
        expire_refresh_token= refresh_token_expire,
    )
    return token


@router.post("/login/refresh-token", response_model = account_entity.Token)
def refresh_token( 
    *, 
    # db_session: Session = Depends(get_db),
    refresh_token: str = Form(...),
):
    token = token_helper.decrypt_renew(refresh_token)
    if token == False:
        raise HTTPException(status_code=403, detail="token wrong")
    if token['user_name'] != config.USER or token['password'] != config.PASSWORD:
        raise HTTPException(status_code=400, detail="token wrong")
    token_create = account_entity.TokenCreate(
        user_name= token['user_name'],
        password= token['password'],
    )
    access_token, access_token_expire  = token_helper.create_access_token(token_create.__dict__)
    refresh_token, refresh_token_expire = token_helper.create_fresh_token(token_create.__dict__)
    token = account_entity.Token(
        access_token = access_token, 
        refresh_token = refresh_token,
        expire_token= access_token_expire,
        expire_refresh_token=refresh_token_expire,
    )
    return token
