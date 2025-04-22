from fastapi import FastAPI, Request, Depends, HTTPException, status, Form
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from typing import Annotated

app = FastAPI(docs_url=False, redoc_url=False)

# Монтируем папку static для статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Инициализируем Jinja2
templates = Jinja2Templates(directory="templates")

# Храним активные сессии (в реальном приложении используйте базу данных или Redis)
active_sessions = {}

# Конфигурация пользователей (в реальном приложении храните в базе с хешированием паролей)
USERS = {
    "admin": {
        "password": "admin",
        "name": "Administrator"
    }
}

# Защита маршрутов через проверку сессии
async def get_current_user(request: Request):
    session_token = request.cookies.get("session_token")
    if not session_token or session_token not in active_sessions:
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            detail="Not authenticated",
            headers={"Location": "/login"},
        )
    return active_sessions[session_token]

@app.get("/", response_class=HTMLResponse)
async def root_redirect(request: Request):
    session_token = request.cookies.get("session_token")
    if session_token in active_sessions:
        return RedirectResponse(url="/en", status_code=303)
    return RedirectResponse(url="/en/login", status_code=303)  # или /ru/login если хочешь по умолчанию

# Страница логина (EN)
@app.get("/en/login", response_class=HTMLResponse)
async def login_page_en(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "current_language": "en"})

# Страница логина (RU)
@app.get("/ru/login", response_class=HTMLResponse)
async def login_page_ru(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "current_language": "ru"})

# Страница логина
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def perform_login(
    request: Request,
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    if username not in USERS or USERS[username]["password"] != password:
        current_language = "ru" if "ru" in str(request.url.path) else "en"
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Неверный логин или пароль" if current_language == "ru" else "Invalid username or password", "current_language": current_language},
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    
    session_token = secrets.token_urlsafe(32)
    active_sessions[session_token] = {
        "username": username,
        "name": USERS[username]["name"]
    }

    lang = "ru" if "ru" in str(request.url.path) else "en"
    response = RedirectResponse(url=f"/{lang}", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="session_token", value=session_token, httponly=True)
    return response

# Выход из системы
@app.get("/logout")
async def logout(request: Request):
    session_token = request.cookies.get("session_token")
    if session_token in active_sessions:
        del active_sessions[session_token]
    
    response = RedirectResponse(url="/login")
    response.delete_cookie("session_token")
    return response

# Защищенные маршруты
@app.get("/en", response_class=HTMLResponse)
async def read_root(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/index.html", context)

@app.get("/en/docs", response_class=HTMLResponse)
async def docs_page(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs.html", context)

@app.get("/en/docs/alt-linux", response_class=HTMLResponse)
async def alt_linux_docs(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs/alt-linux.html", context)

@app.get("/en/docs/cisco", response_class=HTMLResponse)
async def cisco_docs(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs/cisco.html", context)

@app.get("/en/docs/firewall", response_class=HTMLResponse)
async def firewall_docs(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs/firewall.html", context)

@app.get("/en/docs/cyberbackup", response_class=HTMLResponse)
async def cyberbackup_docs(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs/cyberbackup.html", context)

@app.get("/en/docs/terraform", response_class=HTMLResponse)
async def terraform_docs(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs/terraform.html", context)

@app.get("/ru/", response_class=HTMLResponse)
async def read_root_ru(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/index.html", context)


@app.get("/ru/docs", response_class=HTMLResponse)
async def docs_page_ru(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs.html", context)

@app.get("/ru/docs/not-planed", response_class=HTMLResponse)
async def not_planed_docs(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/not-planed.html", context)

@app.get("/ru/docs/alt-linux", response_class=HTMLResponse)
async def alt_linux_docs(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/alt-linux.html", context)

@app.get("/ru/docs/cisco", response_class=HTMLResponse)
async def cisco_docs(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/cisco.html", context)

@app.get("/ru/docs/firewall", response_class=HTMLResponse)
async def firewall_docs(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/firewall.html", context)

@app.get("/ru/docs/cyberbackup", response_class=HTMLResponse)
async def cyberbackup_docs(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/cyberbackup.html", context)

@app.get("/ru/docs/terraform", response_class=HTMLResponse)
async def terraform_docs(request: Request, user: dict = Depends(get_current_user)):
    context = {
        "request": request,
        "user": user,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/terraform.html", context)

@app.get("/ru/docs/images/screen_in_grub.png", response_class=HTMLResponse)
async def screen_in_grub(request: Request, user: dict = Depends(get_current_user)):
    return FileResponse("templates/ru/docs/images/screen_in_grub.png")

@app.get("/ru/docs/images/screen_bash_in_oneuser.png", response_class=HTMLResponse)
async def screen_bash_in_oneuser(request: Request, user: dict = Depends(get_current_user)):
    return FileResponse("templates/ru/docs/images/screen_bash_in_oneuser.png")