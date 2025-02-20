# Copyright (c) 2025, Abel Gezahegn and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Book(WebsiteGenerator):
	pass

# # for storing all books 
# def get_context(context):
#     context.books = frappe.get_all("Book", fields=["title", "author", "isbn", "image"])

# def get_context(context):
# 	context.books = frappe.db.get_all("Book", fields=["title", "author", "image", "route"])
# 	return context

# In your custom app's controller (e.g., my_app/my_app.py)
# @frappe.whitelist()
# def get_context(context):
#     context.books = [
#         {
#             "title": "Book 1",
#             "author": "Author 1",
#             "published_year": "2021",
#             "image": "/assets/my_app/images/book1.jpg"
#         },
#         {
#             "title": "Book 2",
#             "author": "Author 2",
#             "published_year": "2022",
#             "image": "/assets/my_app/images/book2.jpg"
#         },
#         # Add more books
#     ]
#     return context