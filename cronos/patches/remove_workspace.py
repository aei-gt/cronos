import frappe

def execute():
    frappe.db.delete('Workspace', {'name': 'CRONOS'})
    frappe.db.commit()