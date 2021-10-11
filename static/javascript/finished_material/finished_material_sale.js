// this ajax file for finished material sale
let Sale_Save = $("#sale-form").attr("url")
const finished_material_id = (data) => {
    console.log(data.data)
    const finished_material_id = data.data
    finished_material_id.map(item => {
        $('#sfm_id').append(`<option value="${item.id}">${item.id}</option>`);
    })
}
common_ajax_call(url = Sale_Save, data="response", method_type = "GET", finished_material_id)

//#######################################################################

var a_s_t = document.getElementById('sfm_id');
const s_m_grad = document.getElementById('s_m_type');
if(a_s_t){
    a_s_t.addEventListener('change', function () {
        var selected_id = this.value;
    s_m_grad.textContent = "Select"
    
    const finished_material_type = (data) => {
        var s_m_data = data.data
        s_m_data.map(item => {
            $('#s_m_type').val(item.materialType);
        })
    }
    common_ajax_call(url = `get_finished_material_type/${selected_id}/`, data="response", method_type = "GET", finished_material_type)
});
}

//####################################################################

$("#btnsave-sale").click("#sale-form", function () {
    // $("#btnsave").click(function(){
    output_uf = "";
    let fmsale_id = $("#sfm_id").val();
    let sale_date = $("#sale_date").val();
    let sale_type = $("#s_m_type").val();
    let sale_quantity = $("#sale_quantity").val();
    let sale_weight = $("#sale_weight").val();
    let sold_to = $("#sale_sold").val();
    let csr = $("input[name=csrfmiddlewaretoken").val();
    sale_data = {
        fmsales_id: fmsale_id,
        sold_to: sold_to,
        sale_type: sale_type,
        sales_date: sale_date,
        sales_quantity: sale_quantity,
        sales_weight: sale_weight,
        csrfmiddlewaretoken: csr,
    };
    if (fmsale_id == '') {
        // console.log('input')
        $("#toast2_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    } else if (sale_sold == '') {
        // $("#sale-form")[0].reset();
        $("#toast2_id").html(alert_msg('Error!', 'Please input Sold To', 'toast-div-danger'))
    }
    else if (sale_date == '') {
        // $("#sale-form")[0].reset();
        $("#toast2_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    } else if (sale_quantity == '') {
        $("#toast2_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    } else if (sale_weight == '') {
        $("#toast2_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    }
    else {
        const finished_material_sale_save = (data) => {
            x = data.sale_data;
                if (data.status == 1) {
                    $("#toast2_id").html(alert_msg('Error!', 'Not enough Weight in Stock', 'toast-div-danger'))
                };
                if (data.status == 2) {
                    $("#toast2_id").html(alert_msg('Error!', 'Not enough Quantity in Stock', 'toast-div-danger'))
                }
                if (data.status == "Save") {
                    for (i = 0; i < x.length; i++) {
                        output_uf +=`<tr>
                                        <td>${x[i].id}</td>
                                        <td>${x[i].register_id}</td>
                                        <td>${x[i].To}</td>
                                        <td>${x[i].FMcoilUID_id}</td>
                                        <td>${x[i].Sale_date}</td>
                                        <td>${x[i].Sale_Type}</td>
                                        <td>${x[i].Sale_Quantity}</td>
                                        <td>${x[i].Sale_Weight}</td>
                                        <td class='text-center d-flex justify-content-around'>
                                            <a class='btn three-btn btn-sm btn-del-salefm' title='delet' data-sid="${x[i].id}"><i class='fa fa-trash'></i></a>
                                        </td>
                                    </tr>`;
                    $("#toast2_id").html(alert_msg('Success!', 'Entry Added Successfully', 'toast-div-success'))
                    };
                    $("#s_m_type").val("");
                    $("#sale_quantity").val("");
                    $("#sale_weight").val("");
                    $("#sale_sold").val("");
                    $("#tbody-sale").html(output_uf);
                } if (data.status == 0) {
                    $("#toast2_id").html(alert_msg('Error!', 'Unable to save data', 'toast-div-danger'))
                }
        }
        common_ajax_call(url = 'Finished_Material_Sale_Save', data=sale_data, method_type = "POST", finished_material_sale_save)
    }
})
//###################################################################

$('#tbody-sale').on("click", ".btn-del-salefm", function () {
    let id = $(this).attr("data-sid");
    let csr = $("input[name=csrfmiddlewaretoken").val();
    console.log(id)
    mydata = { sid: id, csrfmiddlewaretoken: csr };
    mythis = this;

    const finished_material_sale_delete = (data) => {
        if (data.status == 1) {
            $("#toast2_id").html(alert_msg('Success!', 'Entry Deleted', 'toast-div-danger'))
            $(mythis).closest("tr").fadeOut();
        }
    }
    common_ajax_call(url = 'Finished_Material_Sale_Delete', data=mydata, method_type = "POST", finished_material_sale_delete)
})

