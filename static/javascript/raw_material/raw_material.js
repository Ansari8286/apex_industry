// this ajax file for raw material
const alert_msg = (head, msg, boot_class) => {
  return `        
        <div class="toast-div ${boot_class}" id="id-toast">
        <div class="toast-header border-bottom">
            <strong class="mr-auto text-dark">${head}</strong>
            <button class=" btn btn-lg pr-lg-2 m-0 py-0 float-right" onclick='this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode); return false;'>&times;</button>
        </div>
        <div class="toast-body border-top px-lg-5 text-center">
        ${msg}
        </div>
    </div>
    <script>
      $('#id-toast').delay(1600).fadeOut();
    </script>
    `;
};

//#######################################################################

var liveToastBtn = document.getElementById("liveToastBtn");

$("#btnsave").click("#post-form", function () {
  output = "";
  let raw_material_date = $("#raw_date").val();
  let raw_material_thickness = $("#raw_thickness").val();
  let raw_material_size = $("#raw_size").val();
  let raw_material_grade = $("#raw_grade").val();
  let raw_material_coilweight = $("#raw_weight").val();
  let raw_material_scrapweight = $("#S_Weight").val();
  let raw_material_vendor = $("#raw_vendor").val();
  let csrf = $("input[name=csrfmiddlewaretoken").val();

  raw_data = {
    raw_material_date: raw_material_date,
    raw_material_thickness: raw_material_thickness,
    raw_material_size: raw_material_size,
    raw_material_grade: raw_material_grade,
    raw_material_coilweight: raw_material_coilweight,
    raw_material_scrapweight: raw_material_scrapweight,
    raw_material_vendor: raw_material_vendor,
    csrfmiddlewaretoken: csrf,
  };
  
  if (raw_material_date == "") {
    $("#toast_id").html(
      alert_msg("Error!", "Please input field", "toast-div-danger")
    );
  } else if(raw_material_vendor == ""){
    $("#toast_id").html(
      alert_msg("Error!", "Please Enter Vendor", "toast-div-success")
    );  
  }else if (raw_material_thickness == "") {
    $("#toast_id").html(
      alert_msg("Error!", "Please input field", "toast-div-danger")
    );
  } else if (raw_material_size == "") {
    $("#toast_id").html(
      alert_msg("Error!", "Please input field", "toast-div-danger")
    );
  } else if (raw_material_grade == "") {
    $("#toast_id").html(
      alert_msg("Error!", "Please input field", "toast-div-danger")
    );
  } else if (raw_material_coilweight == "") {
    $("#toast_id").html(
      alert_msg("Error!", "Please input field", "toast-div-danger")
    );
  } else if (raw_material_scrapweight == "") {
    $("#toast_id").html(
      alert_msg("Error!", "Please input field", "toast-div-danger")
    );
  } else {
    const raw_material_save = (data) =>{
      x = data.raw_data1;
        if (data.status == "Save") {
          for (i = 0; i < x.length; i++) {
            output +=`<tr>
            <td scope="col">${x[i].id}</td>
            <td scope="col">${x[i].register_id}</td>
            <td scope="col">${x[i].Vendor}</td>
            <td scope="col">${x[i].RM_Date}</td>
            <td scope="col">${x[i].RM_Thickness}</td>
            <td scope="col">${x[i].RM_Size}</td>
            <td scope="col">${x[i].RM_Grade}</td>
            <td scope="col">${x[i].RM_currentCoilWeight}</td>
            <td scope="col">${x[i].RM_coilWeight}</td>
            <td>${x[i].RM_scrapWeight}</td>
            <td class='text-center d-flex justify-content-around'>
            <a class='btn three-btn btn-sm btn-del' title='delet' data-sid="${x[i].id}">
            <i class='fa fa-trash'></i>
            </a>
            </td>
            </tr>`
            $("#toast_id").html(
              alert_msg("Success!", "New Entry Added", "toast-div-success")
              );
            }
            $("#raw_thickness").val("");
            $("#raw_size").val("");
            $("#raw_weight").val("");
            $("#S_Weight").val("");
            $("#raw_vendor").val("");
            $("#tbody").html(output);
            // setInterval(() => {
            //   location.reload();
            // }, 2000);
            if (data.status == 0) {
              $("#toast_id").html(
              alert_msg("Alert!", "Unable to Add Data", "toast-div-danger")
            );
          }
        }
      }
      common_ajax_call(url = 'Raw_Material_Save', data = raw_data, method_type="POST", raw_material_save)

    //   const raw_material_graph = (data) => {
    //     // const raw_material_coilweight_graph = JSON.parse(document.getElementById("raw_material_coilweight_graph").textContent);
    //     raw_material_data = data.status
    //     graph_data = JSON.parse(JSON.stringify(raw_material_data))
    //     console.log(graph_data)
    //     rawMaterialGraph(data=graph_data)
    // }
    // common_ajax_call(url = '/raw_material_graph', data = "response", method_type="GET", raw_material_graph)
  }
});

//#######################################################################################

// $("#btnsave").on("click", function () {
// const raw_material_graph = (data) => {
//     console.log("success", data.status)
// }
// common_ajax_call(url = '/raw_material_graph', data = "response", method_type="GET", raw_material_graph)
// });

//#######################################################################

// For deleting raw materials
$("#tbody").on("click", ".btn-del", function () {
  id = $(this).attr("data-sid");
  csrf = $("input[name=csrfmiddlewaretoken").val();
  mydata = { sid: id, csrfmiddlewaretoken: csrf };
  mythis = this;

  const raw_material_delete = (data) => {
    if (data.status == 1) {
      $("#toast_id").html(
      alert_msg("Success!", "Entry Deleted", "toast-div-danger"));
      $(mythis).closest("tr").fadeOut();
    }
  }
  common_ajax_call(url = 'Raw_Material_Delete', data = mydata, method_type="POST", raw_material_delete)
});
