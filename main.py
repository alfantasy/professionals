from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(docs_url=False, redoc_url=False)

# Монтируем папку static для статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Инициализируем Jinja2
templates = Jinja2Templates(directory="templates")

# Главная страница
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Страница документации
@app.get("/docs", response_class=HTMLResponse)
def docs_page(request: Request):
    return templates.TemplateResponse("docs.html", {"request": request})

@app.get("/ru/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index_ru.html", {"request": request})

@app.get("/ru/docs", response_class=HTMLResponse)
def docs_page(request: Request):
    return templates.TemplateResponse("docs_ru.html", {"request": request})