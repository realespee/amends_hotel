frappe.pages['hotel-reservation'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Hotel Reservation',
		single_column: true
	});
}