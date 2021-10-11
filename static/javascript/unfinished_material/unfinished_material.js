// this ajax file for unfinished material 

$("#btnsaveuf").click("#uf-form", function () {
    output_uf = "";
    let uf_date = $("#uf_date").val();
    let uf_weight = $("#uf_weight").val();
    let uf_quantity = $("#uf_quantity").val();
    let fm_id = $("#fm_id").val();
    let csr = $("input[name=csrfmiddlewaretoken").val();

    uf_data = {
        uf_date: uf_date,
        uf_weight: uf_weight,
        uf_quantity: uf_quantity,
        f_id: fm_id,
        csrfmiddlewaretoken: csr,
    };
    if (uf_date == '') {
        $("#toast1_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    } else if (uf_weight == '') {
        $("#toast1_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    } else if (uf_quantity == '') {
        $("#toast1_id").html(alert_msg('Error!', 'Please input field', 'toast-div-danger'))
    }
    else {
        const unfinished_material_save = (data) => {
            x = data.uf_data;
                if (data.status == "Save") {
                    for (i = 0; i < x.length; i++) {
                        output_uf +=`<tr>
                                        <td scope="col">${x[i].id}</td>
                                        <td scope="col">${x[i].register_id}</td>
                                        <td scope="col">${x[i].UFM_date}</td>
                                        <td scope="col">${x[i].FMid}</td>
                                        <td scope="col">${x[i].UFM_type}</td>
                                        <td scope="col">${x[i].UFM_Quantity}</td>
                                        <td scope="col">${x[i].UFM_Weight}</td>
                                        <td class="text-center d-flex justify-content-around">
                                            <a class="btn three-btn btn-sm btn-del-ufm" title='delet' data-sid="${x[i].id}"id="del"><i class="fa fa-trash"></i></a>
                                        </td>
                                    </tr>`
                    $("#toast1_id").html(alert_msg('Success!', 'Entry Added Successfully', 'toast'))
                    };
                    $("#tbodyufm").html(output_uf);
                    if (data.status == 0) {
                        $("#toast1_id").html(alert_msg('Error!', 'Unable to Save Data', 'toast-div-danger'))
                    }
                }
        }
        common_ajax_call(url = 'Unfinished_Material_Save', data = uf_data, method_type="POST", unfinished_material_save)
    }
})

//################################################################################################

$('#tbodyufm').on("click", '.btn-del-ufm', function () {
    let id = $(this).attr("data-sid");
    let csr = $("input[name=csrfmiddlewaretoken").val();
    mydata = { sid: id, csrfmiddlewaretoken: csr };
    mythis = this;
    const unfinished_material_Delete = (data) => {
        if (data.status == 1) {
            $("#toast1_id").html(alert_msg('Success!', 'Entry Deleted', 'toast-div-danger'))
            $(mythis).closest("tr").fadeOut();
        }
    }
    common_ajax_call(url = 'Unfinished_Material_Delete', data = mydata, method_type="POST", unfinished_material_Delete)
})
