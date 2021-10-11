// this ajax file for unfinished material sale
var UnFinished_Material_Sale_Save = $("#usale-form").attr("url")
const unfinished_material_Id = (data) => {
    const us_m_t = data.data
        us_m_t.map(item =>{
            $('#usfm_id').append(`<option value="${item.id}">${item.id}</option>`);
        })
}
common_ajax_call(url = UnFinished_Material_Sale_Save, data = "response", method_type="GET", unfinished_material_Id)

//###################################################################################

var ua_s_t = document.getElementById('usfm_id');
const us_m_grad = document.getElementById('us_m_type');
if (ua_s_t){
    ua_s_t.addEventListener('change', function() {
        var selected_id = this.value;
        us_m_grad.textContent = "Select"
        
        const unfinished_material_type = (data) => {
            var us_m_data = data.data
            us_m_data.map(item =>{
                $('#us_m_type').val(item.UFM_type);
            })
        }
        common_ajax_call(url = `get_unfinished_material_type/${selected_id}/`, data = "response", method_type="GET", unfinished_material_type)
    }, false);
}
    
//############################################################################################

$("#btnsave-usale").click("#usale-form",function(){
    output_uf = "";
    let ufmsale_id= $("#usfm_id").val();
    let sale_date = $("#usale_date").val();
    let usale_sold = $("#usale_sold").val()
    let usale_type = $("#us_m_type").val();
    let sale_quantity = $("#usale_quantity").val();
    let sale_weight = $("#usale_weight").val();
    let csr = $("input[name=csrfmiddlewaretoken").val();

    sale_data = {
        us_m_type : usale_type,
        ufmsales_id : ufmsale_id,
        sales_date : sale_date,
        sales_quantity: sale_quantity,
        sales_weight: sale_weight,
        usale_sold: usale_sold,
        csrfmiddlewaretoken: csr,
    };
    if(ufmsale_id == ''){
        $("#toast4_id").html(alert_msg('Error!','Please input field', 'toast-div-danger'))
    }else if(usale_sold == ''){
        $("#toast4_id").html(alert_msg('Error!','Please input Sold To', 'toast-div-danger'))
    }
    else if(sale_date == ''){
        $("#toast4_id").html(alert_msg('Error!','Please input field', 'toast-div-danger'))
    }else if(sale_quantity == '') {
        $("#toast4_id").html(alert_msg('Error!','Please input field', 'toast-div-danger'))
    }else if(sale_weight == '') {
        $("#toast4_id").html(alert_msg('Error!','Please input field', 'toast-div-danger'))
    }    
    else{
        const unfinished_material_Sale = (data) => {
            x = data.sale_data;
            if (data.status == 1) {
        $("#toast4_id").html(alert_msg('Error!','Not enough Weight in stock', 'toast-div-danger'))
            };
            if (data.status == 2) {
        $("#toast4_id").html(alert_msg('Error!','Not enough Quantity in stock', 'toast-div-danger'))
            }
            if (data.status == "Save") {
                for (i = 0; i < x.length; i++) {
                    output_uf +=`<tr>
                                    <td>${x[i].id}</td>
                                    <td>${x[i].register_id}</td>
                                    <td>${x[i].To}</td>
                                    <td>${x[i].UFcoilID_id}</td>
                                    <td>${x[i].Sale_date}</td>
                                    <td>${x[i].Sale_Type}</td>
                                    <td>${x[i].Sale_Quantity}</td>
                                    <td>${x[i].Sale_Weight}</td>
                                    <td class='text-center d-flex justify-content-around'>
                                        <a class='btn three-btn btn-sm btn-del-usale' title='delet' data-sid="${x[i].id}"><i class='fa fa-trash'></i></a>
                                    </td>
                                </tr>`;
                $("#toast4_id").html(alert_msg('Success!','Entry Added', 'toast-div-success'))
                };
                $("#usale_sold").val("");
                $("#us_m_type").val("");
                $("#usale_quantity").val("");
                $("#usale_weight").val("");
                $("#tbody-usale").html(output_uf);
            }if(data.status==0) {
                $("#toast4_id").html(alert_msg('Error!','Unable to save data', 'toast-div-danger'))
            }
        }
        common_ajax_call(url = 'UnFinished_Material_Sale_Save', data = sale_data, method_type="POST", unfinished_material_Sale)
}
})

//############################################################################################

$('#tbody-usale').on("click",".btn-del-usale",function (){
    let id = $(this).attr("data-sid");
    let csr = $("input[name=csrfmiddlewaretoken").val();
    console.log(id)
    mydata = { sid: id, csrfmiddlewaretoken: csr };
    mythis = this;

    const unfinished_material_Sale_Delete = (data) => {
        if (data.status==1){
            $("#toast4_id").html(alert_msg('Success!','Entry deleted', 'toast-div-danger'))
            $(mythis).closest("tr").fadeOut();
        }
    }
    common_ajax_call(url = 'UnFinished_Material_Sale_Delete', data = mydata, method_type="POST", unfinished_material_Sale_Delete)
})
