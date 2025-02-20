import frappe
from frappe import _

# Create a new Book
@frappe.whitelist(allow_guest=True)  # Allow public access for external access
def create_book(title, author, isbn, image):
    doc = frappe.get_doc({
        "doctype": "Book",
        "title": title,
        "author": author,
        "isbn": isbn,
        # "publish_date": publish_date,
        "image": image,
    })
    doc.insert()
    return {"message": "book created sucessfully"}


# Fetch book details
@frappe.whitelist(allow_guest=True)
def get_book(book_id):
    doc = frappe.get_doc("Book", book_id)
    return doc.as_dict()


# Update a book's status
@frappe.whitelist(allow_guest=True)
def update_book(book_id):
    doc = frappe.get_doc("Book", book_id)
    # Update the book with the provided data
    # doc.update(kwargs)
    doc.save()
    return {"message": "book updated sucessfully"}



# Delete a book
@frappe.whitelist(allow_guest=True)
def delete_book(book_id):
    frappe.delete_doc("Book", book_id)
    return {"message": "book deleted sucessfully"}
