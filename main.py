from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.utils import generate_entry_number
from app.excel_handler import save_entry, get_operation_ids
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    operation_ids = get_operation_ids()
    return templates.TemplateResponse("form.html", {"request": request, "operation_ids": operation_ids})

@app.post("/submit", response_class=HTMLResponse)
async def submit_form(
    request: Request,
    date: str = Form(...),
    shift: int = Form(...),
    operation_id: str = Form(...),
    from_time: str = Form(...),
    to_time: str = Form(...),
    quantity: int = Form(...)
):
    entry_number = generate_entry_number()
    save_entry(entry_number, date, shift, operation_id, from_time, to_time, quantity)
    return RedirectResponse("/", status_code=303)
