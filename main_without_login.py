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

@app.get("/en", response_class=HTMLResponse)
async def read_root(request: Request):
    context = {
        "request": request,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/index.html", context)

@app.get("/en/docs", response_class=HTMLResponse)
async def docs_page(request: Request):
    context = {
        "request": request,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs.html", context)

@app.get("/en/docs/alt-linux", response_class=HTMLResponse)
async def alt_linux_docs(request: Request):
    context = {
        "request": request,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs/alt-linux.html", context)

@app.get("/en/docs/cisco", response_class=HTMLResponse)
async def cisco_docs(request: Request):
    context = {
        "request": request,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs/cisco.html", context)

@app.get("/en/docs/firewall", response_class=HTMLResponse)
async def firewall_docs(request: Request):
    context = {
        "request": request,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs/firewall.html", context)

@app.get("/en/docs/cyberbackup", response_class=HTMLResponse)
async def cyberbackup_docs(request: Request):
    context = {
        "request": request,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs/cyberbackup.html", context)

@app.get("/en/docs/terraform", response_class=HTMLResponse)
async def terraform_docs(request: Request):
    context = {
        "request": request,
        "current_language": "en"
    }
    return templates.TemplateResponse("en/docs/terraform.html", context)

@app.get("/ru/", response_class=HTMLResponse)
async def read_root_ru(request: Request):
    context = {
        "request": request,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/index.html", context)


@app.get("/ru/docs", response_class=HTMLResponse)
async def docs_page_ru(request: Request):
    context = {
        "request": request,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs.html", context)

@app.get("/ru/docs/not-planed", response_class=HTMLResponse)
async def not_planed_docs(request: Request):
    context = {
        "request": request,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/not-planed.html", context)

@app.get("/ru/docs/alt-linux", response_class=HTMLResponse)
async def alt_linux_docs(request: Request):
    context = {
        "request": request,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/alt-linux.html", context)

@app.get("/ru/docs/cisco", response_class=HTMLResponse)
async def cisco_docs(request: Request):
    context = {
        "request": request,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/cisco.html", context)

@app.get("/ru/docs/firewall", response_class=HTMLResponse)
async def firewall_docs(request: Request):
    context = {
        "request": request,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/firewall.html", context)

@app.get("/ru/docs/cyberbackup", response_class=HTMLResponse)
async def cyberbackup_docs(request: Request):
    context = {
        "request": request,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/cyberbackup.html", context)

@app.get("/ru/docs/terraform", response_class=HTMLResponse)
async def terraform_docs(request: Request):
    context = {
        "request": request,
        "current_language": "ru"
    }
    return templates.TemplateResponse("ru/docs/terraform.html", context)

@app.get("/ru/docs/images/screen_in_grub.png", response_class=HTMLResponse)
async def screen_in_grub(request: Request):
    return FileResponse("templates/ru/docs/images/screen_in_grub.png")

@app.get("/ru/docs/images/screen_bash_in_oneuser.png", response_class=HTMLResponse)
async def screen_bash_in_oneuser(request: Request):
    return FileResponse("templates/ru/docs/images/screen_bash_in_oneuser.png")