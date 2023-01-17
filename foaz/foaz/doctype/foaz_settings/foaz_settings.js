// Copyright (c) 2022, Mai Ismail and contributors
// For license information, please see license.txt

frappe.ui.form.on('Foaz Settings', {
	fetch_employees: function (frm) {
		frappe.call({
			method: "foaz.api.fetch_employees",
			callback: function (r) {
				if (!r.exc) {
					console.log("Done !!!!!!!!!!!!!!!!!!!!!");
				}
			},
		});
	},
	fetch_transactions: function (frm) {
		frappe.call({
			method: "enqueue_long_job_fetch_transactions",
			doc: frm.doc,
			callback: function (r) {
				if (!r.exc) {
					console.log("Done !!!!!!!!!!!!!!!!!!!!!");
				}
			},
		});
	}
});
