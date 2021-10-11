// this ajax file for finished material
$(".pagination").addClass("justify-content-center");
let Raw_Material = $("#fm_form").attr("url")

const finished_material = (data) => {
  const es_data = data.data;
  es_data.map((item) => {
    $("#rm_id").append(`<option value="${item.id}">${item.id}</option>`);
  });
}
common_ajax_call(url = Raw_Material, data="response", method_type = "GET", finished_material)

//#########################################################################

var a = document.getElementById("rm_id");
const grad = document.getElementById("rm_grade");
a.addEventListener("change", function () {

  var selected_id = this.value;
  grad.textContent = "Select";

  const finished_material_id = (data) => {
    var rw_data = data.data;
    rw_data.map((item) => {

      $("#rm_grade").append(`<option value="${item.RM_Grade}">${item.RM_Grade}</option>`);
      $("#rm_size").val(item.RM_Size);
      $("#rm_weight").attr('placeholder', `Enter RM weights:current coil weight: ${item.RM_coilWeight}`);
    });
  }
  common_ajax_call(url = `get_raw_material_grade/${selected_id}/`, data = "response", method_type = "GET", finished_material_id)
});

//####################################################################s

$("#btnsave_fm").click("#fm_form", function () {
  output = "";
  value = "";
  let fm_date = $("#fm_date").val();
  let rm_id = $("#rm_id").val();
  let rm_size = $("#rm_size").val();
  let rm_grade = $("#rm_grade").val();
  let rm_weight = $("#rm_weight").val();

  let fm_type = $("#fm_type").val();
  let fm_thickness = $("#fm_thickness").val();
  let fm_size = $("#fm_size").val();
  let fm_weight = $("#fm_weight").val();
  let fm_quantity = $("#fm_quantity").val();
  let fm_scrapeweight = $("#fm_scrapeweight").val();

  let ufm_thickness = $("#ufm_thickness").val();
  let ufm_size = $("#ufm_size").val();
  let ufm_weight = $("#ufm_weight").val();
  let ufm_quantity = $("#ufm_quantity").val();

  let csr = $("input[name=csrfmiddlewaretoken").val();

  fm_data = {
    fmat_date: fm_date,
    raw_id: rm_id,
    raw_size: rm_size,
    raw_grade: rm_grade,
    raw_weight: rm_weight,
    fmat_type: fm_type,
    fmat_thickness: fm_thickness,
    fmat_size: fm_size,
    fmat_weight: fm_weight,
    fmat_quantity: fm_quantity,
    fmat_scrape: fm_scrapeweight,
    uf_thickness: ufm_thickness,
    uf_size: ufm_size,
    uf_weight: ufm_weight,
    uf_quantity: ufm_quantity,
    csrfmiddlewaretoken: csr,
  };
  if (fm_date == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (rm_id == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (rm_size == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (rm_grade == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (rm_weight == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (fm_type == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (fm_thickness == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (fm_size == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (fm_weight == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (fm_quantity == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (fm_scrapeweight == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (ufm_thickness == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (ufm_size == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (ufm_weight == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else if (ufm_quantity == "") {
    $("#msg").html(
      '<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong>Please Input all Fields.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    );
  } else {
    
    const finished_material_save = (data) => {
      x = data.fm_data;
      
      if (data.status == 1) {
        $("#msg").html(
          '<div class="mt-2 text- alert alert-warning alert-dismissible fade show" role="alert">Not Enough Weight in Raw Material<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
        );
      }
      if (data.status == "Save") {
        fmId = x.slice(-1)[0]
        
        $('#sfm_id').append(`<option value="${fmId.id}">${fmId.id}</option>`);
      
        for (i = 0; i < x.length; i++) {
          output +=`<tr>
                      <td scope="col">${x[i].id}</td>
                      <td scope="col">${x[i].FM_Date}</td>
                      <td scope="col">${x[i].register_id}</td>
                      <td scope="col">${x[i].coilUID_id}</td>
                      <td scope="col">${x[i].Size}</td>
                      <td scope="col">${x[i].Grade}</td>
                      <td scope="col">${x[i].coilWeight}</td>
                      <td scope="col">${x[i].materialType}</td>
                      <td scope="col">${x[i].FM_Thickness}</td>
                      <td scope="col">${x[i].FM_Size}</td>
                      <td scope="col">${x[i].FM_Weight}</td>
                      <td scope="col">${x[i].FM_Quantity}</td>
                      <td scope="col">${x[i].FM_scrapWeight}</td>
                      <td scope="col">${x[i].UF_Thickness}</td>
                      <td scope="col">${x[i].UF_Size}</td>
                      <td scope="col">${x[i].UF_Weight}</td>
                      <td scope="col">${x[i].UF_Quantity}</td>
                      <td class="text-center d-flex justify-content-around">
                        <a class="btn three-btn btn-sm btn-del-fm" title="delet" data-sid="${x[i].id}" id="del"><i class="fa fa-trash"></i></a>
                      </td>
                    </tr>`
        $("#msg").html('<div class="mt-2 text- alert alert-success alert-dismissible fade show" role="alert">Successfully Submitted<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
        }
        $("#tbody_fm").html(output);
        $("#fm_form")[0].reset();
        if (data.status == 0) {
          $("#msg").html(
            '<div class="mt-2 text- alert alert-warning alert-dismissible fade show" role="alert">Unable to save data.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
          );
          // $("#msg").show();
          $("#fm_form")[0].reset();
        }
      }
    }
    common_ajax_call(url = '/Finished_Material_Save', data = fm_data, method_type = "POST", finished_material_save)
  }
});

//#################################################################################

$("#tbody_fm").on("click", ".btn-del-fm", function () {
  let id = $(this).attr("data-sid");
  let csr = $("input[name=csrfmiddlewaretoken").val();
  mydata = { sid: id, csrfmiddlewaretoken: csr };
  mythis = this;

  const finished_material_delete = (data) => {
  if (data.status == 1) {
    $("#toast_id").html(
      alert_msg("Success!", "Entry Deleted", "toast-div-danger")
    );
    $(mythis).closest("tr").fadeOut();
  }
}
common_ajax_call(url = '/Finished_Material_Delete', data = mydata, method_type = "POST", finished_material_delete)
});
