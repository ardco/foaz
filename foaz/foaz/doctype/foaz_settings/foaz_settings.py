# Copyright (c) 2022, Mai Ismail and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import enqueue


class FoazSettings(Document):
    @frappe.whitelist()
    def enqueue_long_job_fetch_transactions(self):
        enqueue('foaz.api.fetch_transactions', queue="long", timeout=3600)
