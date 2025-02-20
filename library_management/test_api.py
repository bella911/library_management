import frappe
from frappe import _
from frappe.utils.response import build_response


@frappe.whitelist(allow_guest=True)  # Allow public access if needed
def greet():
    return "API test is working"


@frappe.whitelist(allow_guest=True)  # Allow guest access
def read_data(name):
    try:
        # Fetch document
        doc = frappe.get_doc("Member", name)
        return build_response("json", doc.as_dict(), 200)
    except frappe.DoesNotExistError:
        return build_response("json", {"error": "Data not found"}, 404)
    except Exception as e:
        return build_response("json", {"error": str(e)}, 500)