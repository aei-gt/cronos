import frappe

def execute():
    frappe.db.delete('Workspace', {'name': 'Cronos'})
    frappe.db.commit()