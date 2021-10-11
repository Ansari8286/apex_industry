// Common Ajax Code
const common_ajax_call = (url, data, method_type, success_function_name) => {
    $.ajax({
        type: method_type,
        // headers: {
        //     "X-CSRFToken": csrftoken,
        // },
        dataType: "json",
        url: url,
        data: data,
        success: function (datas) {
            success_function_name(datas);
        },
    });
};
// Common Ajax code

// ######################################################################

// This function is display pop ups in alert button
var Notification_Alert = $("#noti_alert_button").attr("url")
const noti_alert_fun = (data) => {
    if (data.status == "Save") {
    }
}
$("#noti_alert_button").click(function () {
    var b = 'clicked'

    let count_html = document.querySelector(".badge")
    count_html.classList.remove('bg-danger')
    count_html.innerHTML = ""
    b_data = {
        button: b,
    }
    common_ajax_call(url = Notification_Alert, data = b_data, method_type="GET", noti_alert_fun)
})

//###################################################################

// this is for date validation 

$(".serach").on("click", function (e) {

    if ($("#id_start_date")[0].value && $("#id_end_date")[0].value) {
    } else {
        e.preventDefault();
        alert("Please select Dates!");
    }
});

//#########################################################################

// this ajax function for sending notification to admin

$("#btn-noti").click("#notification-form", function () {

    let table_name = $("#p_name").val()
    let subject = $("#p_size").val();
    let reason = $("#q_order").val();
    let operation = $("#p_thickness").val();
    let csr = $("input[name=csrfmiddlewaretoken").val();

    n_data = {
        table_name: table_name,
        subject: subject,
        operation: operation,
        reason: reason,
        csrfmiddlewaretoken: csr,
    };
    if (subject == '') {
        $("#toast8_id").html(
            alert_msg("Success!", "Please Enter Subject", "toast-div-danger")
        );
    } else if (operation == '') {
        $("#toast8_id").html(
            alert_msg("Success!", "Please Enter Operation Request", "toast-div-danger")
        );
    } else if (reason == '') {
        $("#toast8_id").html(
            alert_msg("Success!", "Please Enter Reason", "toast-div-danger")
        );
    }
    else {
        const send_notification = (data) => {
            x = data.n_data1;
            if (data.status == "Save") {
                $("#toast8_id").html(
                    alert_msg("Success!", "Sent Successfully", "toast-div-success")
                );
                $("#notification-form")[0].reset();
            };
            if (data.status == 0) {
                $("#toast8_id").html(
                    alert_msg("Error!", "Unable To Send Message", "toast-div-danger")
                );
                $("#notification-form")[0].reset();
            }
        }
        common_ajax_call(url = '/Notifcation_Send', data = n_data, method_type = "POST", send_notification)
    }
})

//#######################################################################

// this ajax function for set active and inactive time by admin

$("#btnsave-timer").click("#post-form-timmer",function(){
        
        let a_time = $("#a_time").val();
        let d_time = $("#d_time").val();
        let csr = $("input[name=csrfmiddlewaretoken").val();
        timmer_data = {
            ac_time : a_time,
            dc_time : d_time,
            csrfmiddlewaretoken: csr,
        };
        if(a_time == ''){
            $("#msg-emp").html('<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong> Please Enter Active Time.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
        }else if(d_time == ''){
            $("#msg-emp").html('<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong> Please enter In-Active Time.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
        }
        else{
            const setTimer = (data) => {
                x = data.timmer_data;
                if (data.status == "Save") {
                    $("#msg-emp").html('<div class="mt-2 text- alert alert-warning alert-dismissible fade show" role="alert">Timmer Set.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
                }else if(data.status==0) {
                    $("#msg-emp").html('<div class="mt-2 text- alert alert-warning alert-dismissible fade show" role="alert">Unable to set Time.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
                }
            }
            common_ajax_call(url = '/Set_Timer', data = timmer_data, method_type = "POST", setTimer)
    }
    })
