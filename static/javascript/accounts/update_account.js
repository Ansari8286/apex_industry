// this ajax file for user account
    $("#btnsave-user").click("#user-form",function(){

        output_uf = "";
        let id = $(this).attr("data-sid");
        let f_name = $("#f_name").val();
        let l_name = $("#l_name").val();
        let email = $("#email").val();
        let p1 = $("#password1").val();
        let p2 = $("#password2").val();
        let csr = $("input[name=csrfmiddlewaretoken").val();
        
        upd_data = {
            u_id : id,
            first_name : f_name,
            last_name: l_name,
            email : email,
            password : p2,
            csrfmiddlewaretoken: csr,
        };
        if(p1 !== p2){
            $("#msg-user").html('<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong> Password is not matching<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
        }
        else if(f_name == ''){
            $("#msg-user").html('<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong> Please Enter First Name.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
        }else if(l_name == ''){
            $("#msg-user").html('<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong> Please enter Last Name.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
        }
        else if(email == ''){
            $("#msg-user").html('<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong> Please enter Email.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
        }
        else if(p1 == '') {
            $("#msg-user").html('<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong> Please enter Password.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
        }else if(p2 == ''){
            $("#msg-user").html('<div class="mt-2 text- alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong> Please enter Password.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
        }
        else{
            const UserAccountUpdate = (data) => {
                if (data.status == "Save") {
                    $("#msg-user").html('<div class="mt-2 text- alert alert-success alert-dismissible fade show" role="alert">Profile Updated<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
                }
                setInterval(() => {
                    window.location.reload();
                }, 1000);
            }
            common_ajax_call(url = '/user_save', data = upd_data, method_type="POST", UserAccountUpdate)
    }
    })
