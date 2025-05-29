import pandas as pd
from openpyxl import load_workbook
import os

excel_path = "data/ddd3451a-352e-4b5a-9cef-cfc2441d457d.xlsx"

def save_entry(entry_no, date, shift, operation_id, from_time, to_time, quantity):
    df = pd.read_excel(excel_path, sheet_name="Sheet1")

    new_row = {
        "ENTRY NO": entry_no,
        "DATE": date,
        "SHIFT": shift,
        "OPERATION ID": operation_id,
        "FROM": from_time,
        "TO": to_time,
        "QUANTITY": quantity
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    with pd.ExcelWriter(excel_path, engine="openpyxl", mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)

def get_operation_ids():
    try:
        df = pd.read_excel(excel_path, sheet_name="OperationMaster")
        return df["OPERATION ID"].dropna().unique().tolist()
    except:
        return []
