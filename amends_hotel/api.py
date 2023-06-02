import frappe
import json
from datetime import datetime

@frappe.whitelist()
def room_reservation(payload):
    print('\n\n\n Payload', payload, '\n\n')
    print('\n\n\n Payload', type(payload), '\n\n')

    booking = json.loads(payload)

    # Trigger create new document for Room Reservation
    doc = frappe.get_doc({
        'doctype': 'Hotel Room Reservation',
        'guest_name': booking['fullName'],
        'from_date': datetime.strptime(booking['checkin'], "%Y-%m-%d %H:%M").date(),
        'to_date': datetime.strptime(booking['checkout'], "%Y-%m-%d %H:%M").date(),
        'late_checkin': 0,
        'status': 'Booked',
        'items': [
            {
                'item': 'NormalRoom',
                'qty': 1
            }
        ]
    })
    doc.insert()

    return doc