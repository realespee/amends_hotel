
$('#largeModal').on('show.bs.modal', function (event) {
    var fullName = $('#fullName').val();
    var checkin = $('#checkin').val();
    var checkout = $('#checkout').val();
    var room = $('#room').val();
    var adults = $('#adults').val();
    var children = $('#children').val();
    
    $('#fullNameModal').val(fullName);
    $('#checkinModal').val(checkin);
    $('#checkoutModal').val(checkout);
    $('#roomModal').val(room);
    $('#adultsModal').val(adults);
    $('#childrenModal').val(children);

    var payload = {
        'fullName': $('#fullName').val(),
        'checkin': $('#checkin').val(),
        'checkout': $('#checkout').val(),
        'room': $('#room').val(),
        'adults': $('#adults').val(),
        'children': $('#children').val(),
    }

    $('#submit-form').on('click', function(e){

        frappe.call({
            method: 'amends_hotel.api.room_reservation',
            args: {
                'payload': payload
            },
            // async: false, // This was a charm after 18 hours
            callback: function(r){
                if(r.message){
                    alert("Success! Congratulations")
                }
    
            }
        })

    })
         
});

