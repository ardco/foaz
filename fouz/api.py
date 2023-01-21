# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
import frappe
import json
from PyPDF2 import PdfFileWriter
from frappe.utils.print_format import read_multi_pdf
from frappe.utils.print_format import download_pdf
from frappe.utils import getdate
from frappe import _, throw
from datetime import datetime
import json


@frappe.whitelist()

def validate_transaction_date(doc, method):
    joining_date = frappe.db.get_value("Employee", doc.name , "date_of_joining")
    years_of_work = calculate_years_of_work( joining_date)
    frappe.db.set_value("Employee" , doc.name , "years_of_work" , years_of_work)

def calculate_years_of_work( joining_date):
    joining_date =  joining_date 
    current_date = datetime.now()
    years_of_work = current_date.year - joining_date.year
    # if current_date.month < joining_date.month or (current_date.month == joining_date.month and current_date.day < joining_date.day):
    #     years_of_work -= 1
    if joining_date.month > 6:
        years_of_work -= 1
    if years_of_work < 1:
        years_of_work = 0
    return years_of_work
    
def recalculate_years_of_work():
    current_date = datetime.now()
    for employee in frappe.get_all("Employee", filters={ "status": "Active" }):
        joining_date = frappe.db.get_value("Employee", employee.name , "date_of_joining")
        years_of_work = current_date.year - joining_date.year
        if joining_date.month > 6:
            years_of_work -= 1
        if years_of_work < 1:
            years_of_work = 0
        frappe.db.set_value("Employee" , employee.name , "years_of_work" , years_of_work)
    frappe.db.commit()
