import frappe

def get_context(context):
    # Get Room Types
    room_types = frappe.get_all("Hotel Room Type")
    

    # Get Room Prices || also add image urls
    room_prices = frappe.get_all('Item', filters={'item_group': 'Hotel Room'}, fields=['name', 'valuation_rate', 'item_name'])
    image_urls = [
        'assets/amends_hotel/hotel/image/room1.jpg',
        'assets/amends_hotel/hotel/image/room2.jpg',
        'assets/amends_hotel/hotel/image/room3.jpg'
    ]
    # add image url for each item in room prices
    room_prices = [{**d, **{'image_url': url}} for d, url in zip(room_prices, image_urls)]

    # print('\n\n PRICES\n', room_prices, '\n\n')

    # Make Context
    context.room_types = room_types
    context.room_prices = room_prices

    return context