const alert3_msg = (head, msg, boot_class) => {
    return `
    <div class="toast-div" data-delay="1000">
        <div class="toast-header ${boot_class}">
        <strong class="mr-auto text-dark">${head}</strong>
        <button class=" btn btn-lg pr-lg-2 m-0 py-0 float-right" onclick='this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode); return false;'>&times;</button>
        </div>
        <div class="toast-body ${boot_class} px-lg-5 text-center">${msg}</div>
    </div>
    `
}

//#########################################################################

$("#btnsave-es").click("#post-form-es", function () {
    output_uf = "";
    let date = $("#es_date").val();
    let type = $("#es_type").val();
    let quantity = $("#es_quantity").val();
    let size = $("#es_size").val();
    let csrf = $("input[name=csrfmiddlewaretoken").val();    

    es_data = {
        es_date: date,
        es_type: type,
        es_quantity: quantity,
        es_size: size,
        csrfmiddlewaretoken: csrf,
    };
    
    if (date == '') {
        $("#toast3_id").html(alert3_msg('Error!', 'Please input field', 'toast-div-danger'))
    } else if (type == '') {
        $("#toast3_id").html(alert3_msg('Error!', 'Please input field', 'toast-div-danger'))
    } else if (quantity == '') {
        $("#toast3_id").html(alert3_msg('Error!', 'Please input field', 'toast-div-danger'))
    } else if (size == '') {
        $("#toast3_id").html(alert3_msg('Error!', 'Please input field', 'toast-div-danger'))
    }
    else {
        const essential_save = (data) => {
        let x = data.es_data;
        esId = x.slice(-1)[0]
        $('#upd_id').append(`<option value="${esId.id}">${esId.id}</option>`);
        
            if (data.status == "Save") {
                for (i = 0; i < x.length; i++) {
                    output_uf +=`<tr>
                                    <td scope="col">${x[i].id}</td>
                                    <td scope="col">${x[i].register_id}</td>
                                    <td scope="col">${x[i].ES_Date}</td>
                                    <td scope="col">${x[i].Type}</td>
                                    <td scope="col">${x[i].ES_Quantity}</td>
                                    <td scope="col">${x[i].ES_Size}</td>
                                    <td class='text-center d-flex justify-content-around'>
                                        <a class='btn three-btn btn-sm btn-del-es' title='delet' data-sid="${x[i].id}"><i class='fa fa-trash'></i></a>
                                    </td>
                                </tr>`
                $("#toast3_id").html(alert3_msg('Success!', 'Entry Added', 'toast-div-success'))};
                $("#es_date").val("");
                $("#es_type").val("");
                $("#es_quantity").val("");
                $("#es_size").val("");
                $("#tbody-es").html(output_uf);
            } else if (data.status == 0) {
                $("#toast3_id").html(alert3_msg('Error!', 'Unable to save data', 'toast-div-danger'))
            }
        }
        common_ajax_call(url = 'Essential_Item_Save', data = es_data, method_type = "POST", essential_save)
        const essential_material_graph = (data) => {
            essential_data = data.essential_data_graph
            essentialDataGraph = JSON.parse(JSON.stringify(essential_data))
            updateEssentialMaterialGraph(essentialDataGraph) 
        }
        common_ajax_call(url = '/essential_material_graph', data = "response", method_type="GET", essential_material_graph)
    }
})

//###################################################################################

$('#tbody-es').on("click", ".btn-del-es", function () {
    // console.log('button selected')
    let id = $(this).attr("data-sid");
    let csrf = $("input[name=csrfmiddlewaretoken").val();
    mydata = { sid: id, csrfmiddlewaretoken: csrf };
    mythis = this;
    const essentialDelete = (data) => {
        if (data.status == 1) {
            $("#toast3_id").html(alert3_msg('Success!', 'Entry Deleted', 'toast-div-danger'))
            $(mythis).closest("tr").fadeOut();
        }
    }
    common_ajax_call(url = 'Essential_Item_Delete', data = mydata, method_type = "POST", essentialDelete)
    const essential_material_graph = (data) => {
        essential_data = data.essential_data_graph
        essentialDataGraph = JSON.parse(JSON.stringify(essential_data))
        updateEssentialMaterialGraph(essentialDataGraph) 
    }
    common_ajax_call(url = '/essential_material_graph', data = "response", method_type="GET", essential_material_graph)
})
