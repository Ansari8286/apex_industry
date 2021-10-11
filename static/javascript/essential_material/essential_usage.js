// this ajax file for essential item usage per day.

const essential_usage = (data) => {
    const es_data = data.data
    es_data.map(item => {
        $('#upd_id').append(`<option value="${item.id}">${item.id}</option>`);
    })
}
common_ajax_call(url = 'Essential_Usage_Save', data="response",method_type = "GET", essential_usage)

//##############################################################################

var a = document.getElementById('upd_id');
const type = document.getElementById('upd_type');
a.addEventListener('change', function () {
    var selected_id = this.value;
    type.textContent = "Select"

    const essential_id = (data) => {
        var es_data = data.data
        es_data.map(item => {
            $('#upd_type').append(`<option value="${item.Type}">${item.Type}</option>`);
            $('#upd_size').val(item.ES_Size);
        })
    }
    common_ajax_call(url = `get_essential_type/${selected_id}/`,data="response", method_type = "GET", essential_id)
}, false);

//##############################################################################
//essential_usage_save
$("#btnsave-upd").click("#post-form-upd", function () {
    output_uf = "";
    let id = $("#upd_id").val();
    let date = $("#upd_date").val();
    let type = $("#upd_type").val();
    let quantity = $("#upd_quantity").val();
    let size = $("#upd_size").val();
    let csrf = $("input[name=csrfmiddlewaretoken").val();

    upd_data = {
        esu_date: date,
        esu_type: type,
        esu_quantity: quantity,
        esu_size: size,
        esu_id: id,
        csrfmiddlewaretoken: csrf,
    };
    if (date == '') {
        $("#toast5_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    } else if (id == '') {
        $("#toast5_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    }
    else if (type == '') {
        $("#toast5_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    }
    else if (quantity == '') {
        $("#toast5_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    } else if (size == '') {
        $("#toast5_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    }
    else {

        const essential_usage_save = (data) => {
            x = data.upd_data;
            if (data.status == 1) {
                $("#toast5_id").html(alert_msg('Error!', 'Not enough Quantity in stock', 'toast-div-danger'))
            };
            if (data.status == "Save") {
                for (i = 0; i < x.length; i++) {
                    output_uf +=`<tr>
                                    <td>${x[i].id}</td>
                                    <td>${x[i].register_id}</td>
                                    <td>${x[i].EPD_Date}</td>
                                    <td>${x[i].EPD_UID_id}</td>
                                    <td>${x[i].EPD_Type}</td>
                                    <td>${x[i].EPD_Quantity}</td>
                                    <td>${x[i].EPD_Size}</td>
                                    <td class='text-center d-flex justify-content-around'>
                                        <a class='btn three-btn btn-sm btn-del-upd' title='delet' data-sid="${x[i].id}"><i class='fa fa-trash'></i></a>
                                    </td>
                                </tr>`;
                $("#toast5_id").html(alert_msg('Success!', 'Entry Added', 'toast-div-success'))};
                $("#tbody-upd").html(output_uf);
                $("#post-form-upd")[0].reset();

            } else if (data.status == 0) {
                $("#toast5_id").html(alert_msg('Error!', 'Unable to save data', 'toast-div-danger'))
            }

        }
        common_ajax_call(url = 'Essential_Usage_Save', data = upd_data, method_type = "POST", essential_usage_save)
    }
})

// ###########################################################################

$('#tbody-upd').on("click", ".btn-del-upd", function () {
    // console.log('button selected')
    let id = $(this).attr("data-sid");
    let csrf = $("input[name=csrfmiddlewaretoken").val();
    console.log(id)
    mydata = { sid: id, csrfmiddlewaretoken: csrf };
    mythis = this;

    const essential_usage_delete = (data) => {
        if (data.status == 1) {
            $("#toast5_id").html(alert_msg('Success!', 'Entry Deleted', 'toast-div-danger'))
            $(mythis).closest("tr").fadeOut();
        }
    }
    common_ajax_call(url = 'Essential_Usage_Delete', data = mydata, method_type = "POST", essential_usage_delete)
})
