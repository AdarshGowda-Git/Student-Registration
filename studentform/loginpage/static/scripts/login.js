//$(document).ready(function(){
//$("#registration_form_button").Click(function(e)
// {
//     e.preventDefault();
//    var first_name = $('#first_name').val();
//    var last_name = $('#last_name').val();
//    var registration_num = $('#registration_num').val();
//    var email_id = $('#email_id').val();
//    var phone_num = $('#phone_num').val();
//    var address_id = $('#address_id').val();
//    var country = $('#country').val();
//
//    console.log(first_name)
//
//    $.ajax
//    ({
//        url : save_registration_url, // the endpoint
//        type : 'POST', // http method
//        data :
//         {
//           first_name: first_name,
//           last_name: last_name,
//           registration_num: registration_num,
//           email_id: email_id,
//           phone_num: phone_num,
//           address_id: address_id,
//           country: country
//        }, // data sent with the post request
//
//        // handle a successful response
//        success : function(response) {
//
//            console.log(json); // log the returned json to the console
//            console.log("success"); // another sanity check
//        },
//
//        // handle a non-successful response
//        error : function(xhr,errmsg,err) {
//            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//        }
//
//
//    });
//});
//return false;
//});
//
