# Copyright (c) 2025, Abel Gezahegn and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Loan(Document):
    def before_save(self):
        if self.type == "Issue":
            self.validate_issue()
            # set the article status to be Issued
            book = frappe.get_doc("Book", self.book)
            # book.issued_to =  frappe.session.user
            book.status = "Issued"
            book.save()

        elif self.type == "Return":
            self.validate_return()
            # set the book status to be Available
            book = frappe.get_doc("Book", self.book)
            book.status = "Available"
            book.save()

    def validate_issue(self):
        book = frappe.get_doc("Book", self.book)
        # book cannot be issued if it is already issued
        if book.status == "Issued":
            frappe.throw("book is already issued by another member")

    def validate_return(self):
        book = frappe.get_doc("Book", self.book)
        # loan = frappe.get_doc("Loan", self.member)
        # book cannot be returned if it is not issued first
        if book.status == "Available":
            frappe.throw("book cannot be returned without being issued first")



