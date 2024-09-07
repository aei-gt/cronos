frappe.listview_settings['Cronos Hik Vision Attendance'] = {
    onload: function (listview) {
        listview.page.add_button(__('Fetch Hik Vision Records'), function () {
            frappe.call({
                method: 'cronos.hikvision_api.hikvision.fetch_hik_vision_records',
                callback: function (response) {
                    if (response) {
                        frappe.show_alert(__('Records have been fetched and processed.'));
                        listview.refresh();
                    }
                }
            });
        });

        listview.page.add_button(__('Delete Records'), function () {
            frappe.call({
                method: 'cronos.hikvision_api.hikvision.delete_records',
                callback: function (response) {
                    if (response) {
                        frappe.show_alert(__('Records have been Deleted.'));
                        listview.refresh();
                    }
                }
            });
        });
        
        
    
    }
};
