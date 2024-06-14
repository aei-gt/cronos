import frappe
import mysql.connector
from mysql.connector import Error
def dummy_api(self,method):
    # Get database connection parameters from site_config.json
    site_config = frappe.get_site_config()
    db_name = site_config.get("db_name")
    db_password = site_config.get("db_password")
    db_host = site_config.get("db_host", "localhost")
    db_user = site_config.get("db_user", "root")
    # Define the connection parameters
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    if conn.is_connected():
        cursor = conn.cursor()
        query = "SELECT * FROM `tabUser`"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:      
            frappe.msgprint(f"{rows[-1]}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        doc = frappe.new_doc("Ahmed")
        doc.name1 = "title"
        doc.save(ignore_permissions = True)
        frappe.db.commit()
    else:
        print("Connection failed")


