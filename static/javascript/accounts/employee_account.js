// this ajax file for updating user role, status, delete access

    $('#edit-employee').on("click",".btn-user-update",function (){
        let id = $(this).attr("data-sid");
        let h = '#status_'
        let r = '#role_'
        let rr = "role_"
        let d = '#del_'
        sid = id.toString(id)
        let status = $(h.concat(sid)).val(); 
        let role = $(r.concat(sid)).val();
        let delet = $(d.concat(sid)).val();
        let csr = $("input[name=csrfmiddlewaretoken").val();
        if (role == 'In-Active'){
            $(d.concat(sid)).val('No');
        }
        p_data = { 
            sid: id,
            st : status,
            rl : role,
            del_access: delet,
            csrfmiddlewaretoken: csr };

            const employeeAccountUpdate = (data) => {
                if (data.status == "Save") {
                    $("#toast6_id").html(
                        alert_msg("Success!", "User Updated", "toast-div-success")
                    );                     
                }
                else{
                    $("#toast6_id").html(
                        alert_msg("Error!", "Unable to update", "toast-div-danger")
                    );                         
                }
            }
            common_ajax_call(url = '/Employee_Access', data = p_data, method_type="POST", employeeAccountUpdate)
    })

//######################################################################################

    $('#edit-employee').on("click",".btn-user-delete",function (){
        let id = $(this).attr("data-sid");
        let csr = $("input[name=csrfmiddlewaretoken").val();
        mydata = { sid: id, csrfmiddlewaretoken: csr };
        mythis = this;

        const employeeAccountDelete = (data) => {
            if (data.status==1){
                $("#toast6_id").html(alert_msg("Success!", "User Deleted", "toast-div-danger")
                );                    
                $(mythis).closest("tr").fadeOut();
            }
        }
        common_ajax_call(url = '/user_delete', data = mydata, method_type="POST", employeeAccountDelete)
    })
