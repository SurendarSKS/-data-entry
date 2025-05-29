# AI Industrial Manager

A simple FastAPI web app to log manufacturing operations into an Excel sheet.

## Features

- Auto-generated Entry Number (0001A to 9999Z)
- Calendar for date selection
- Shift selection (1/2/3)
- Operation ID validated from master
- Excel logging with OpenPyXL

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
