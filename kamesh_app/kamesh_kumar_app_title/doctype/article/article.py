# Copyright (c) 2022, kamesh kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Article(Document):
	
	def validate(doc):
		frappe.msgprint(doc.name)
