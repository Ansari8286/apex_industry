

   //raw material stock search 
   $(document).ready( function () {
       var dataTable = $('#raw_table').DataTable({
           "pageLength":10,
           'aoColumnDefs':[{
               'bSortable':false,
               'aTargets':['nosort'],
            }],
            columnDefs:[
                {type:'date-dd-mm-yyyy',aTargets:[2]}
            ],
            // 'aoColumns':[
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                // ],
                "order":false,
                "bLengthChange":false,
                "dom":'<"top">ct<"top"p><"clear">'
                // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                // "iDisplayLength": 3
            });
            $("#filterbox").keyup(function(){
                dataTable.search(this.value).draw();
            });
        } );
        
        
        //finish material stock search
        $(document).ready( function () {
            var dataTable = $('#finished_table').DataTable({
                "pageLength":10,
                'aoColumnDefs':[{
                    'bSortable':false,
                    'aTargets':['nosort'],
                }],
                // columnDefs:[
                    //     {type:'date-dd-mm-yyyy',aTargets:[2]}
                    // ],
                    // 'aoColumns':[
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        // ],
                        "order":false,
                        "bLengthChange":false,
                        "dom":'<"top">ct<"top"p><"clear">'
                        // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                        // "iDisplayLength": 3
                    });
                    $("#filterbox-fm").keyup(function(){
                        dataTable.search(this.value).draw();
                    });
                } );
                
                // FM sales
                
                $(document).ready( function () {
                    var dataTable = $('#finished_table_sales').DataTable({
                        "pageLength":10,
                        'aoColumnDefs':[{
                            'bSortable':false,
                            'aTargets':['nosort'],
                        }],
                        // columnDefs:[
                            //     {type:'date-dd-mm-yyyy',aTargets:[2]}
                            // ],
                            // 'aoColumns':[
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                // ],
                                "order":false,
                                "bLengthChange":false,
                                "dom":'<"top">ct<"top"p><"clear">'
                                // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                                // "iDisplayLength": 3
                            });
                            $("#filterbox-fm-sales").keyup(function(){
                                
                                dataTable.search(this.value).draw();
                            });
                        } );
                        
                        // unifinished material stock
                        $(document).ready( function () {
                            var dataTable = $('#unfinished_table').DataTable({
                                "pageLength":10,
                                'aoColumnDefs':[{
                                    'bSortable':false,
                                    'aTargets':['nosort'],
                                }],
                                // columnDefs:[
                                    //     {type:'date-dd-mm-yyyy',aTargets:[2]}
                                    // ],
                                    // 'aoColumns':[
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        // ],
                                        "order":false,
                                        "bLengthChange":false,
                                        "dom":'<"top">ct<"top"p><"clear">'
                                        // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                                        // "iDisplayLength": 3
                                    });
                                    $("#filterbox-ufm").keyup(function(){
        dataTable.search(this.value).draw();
    });
} );
// ufm sales
$(document).ready( function () {
    var dataTable = $('#unfinished_table_sales').DataTable({
        "pageLength":10,
        'aoColumnDefs':[{
            'bSortable':false,
            'aTargets':['nosort'],
        }],
        // columnDefs:[
            //     {type:'date-dd-mm-yyyy',aTargets:[2]}
            // ],
            // 'aoColumns':[
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                // ],
                "order":false,
                "bLengthChange":false,
                "dom":'<"top">ct<"top"p><"clear">'
                // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                // "iDisplayLength": 3
            });
            $("#filterbox-ufm-sales").keyup(function(){
                dataTable.search(this.value).draw();
            });
        } );
        
        //essential material stock
        
        $(document).ready( function () {
            var dataTable = $('#es_table').DataTable({
                "pageLength":10,
                'aoColumnDefs':[{
                    'bSortable':false,
                    'aTargets':['nosort'],
                }],
                // columnDefs:[
                    //     {type:'date-dd-mm-yyyy',aTargets:[2]}
                    // ],
                    // 'aoColumns':[
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        // ],
                        "order":false,
                        "bLengthChange":false,
                        "dom":'<"top">ct<"top"p><"clear">'
                        // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                        // "iDisplayLength": 3
                    });
                    $("#filterbox-es").keyup(function(){
                        dataTable.search(this.value).draw();
                    });
                } );
                // es usage table
                $(document).ready( function () {
                    var dataTable = $('#es_table_usage').DataTable({
                        "pageLength":10,
                        'aoColumnDefs':[{
                            'bSortable':false,
                            'aTargets':['nosort'],
                        }],
                        // columnDefs:[
                            //     {type:'date-dd-mm-yyyy',aTargets:[2]}
                            // ],
                            // 'aoColumns':[
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                // ],
                                "order":false,
                                "bLengthChange":false,
                                "dom":'<"top">ct<"top"p><"clear">'
                                // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                                // "iDisplayLength": 3
                            });
                            $("#filterbox-es-usage").keyup(function(){
                                dataTable.search(this.value).draw();
                            });
                        } );
                        
                        //account page employe account
                        $(document).ready( function () {
                            var dataTable = $('#emp_account').DataTable({
                                "pageLength":10,
                                'aoColumnDefs':[{
                                    'bSortable':false,
                                    'aTargets':['nosort'],
                                }],
                                // columnDefs:[
                                    //     {type:'date-dd-mm-yyyy',aTargets:[2]}
                                    // ],
                                    // 'aoColumns':[
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        // ],
                                        "order":false,
                                        "bLengthChange":false,
                                        "dom":'<"top">ct<"top"p><"clear">'
                                        // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                                        // "iDisplayLength": 3
                                    });
                                    $("#filterbox-emp-account").keyup(function(){
                                        dataTable.search(this.value).draw();
                                    });
                                } );
                                
                                //deleted tables
$(document).ready( function () {
    var dataTable = $('#deleted_tables').DataTable({
        "pageLength":10,
        'aoColumnDefs':[{
            'bSortable':false,
            'aTargets':['nosort'],
        }],
        // columnDefs:[
            //     {type:'date-dd-mm-yyyy',aTargets:[2]}
            // ],
            // 'aoColumns':[
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                // ],
                "order":false,
                "bLengthChange":false,
                "dom":'<"top">ct<"top"p><"clear">'
                // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                // "iDisplayLength": 3
            });
            $("#filterbox-del-tables").keyup(function(){
                dataTable.search(this.value).draw();
            });
        } );
        
        //raw log table
        $(document).ready( function () {
            var dataTable = $('#log_raw').DataTable({
                "pageLength":10,
                'aoColumnDefs':[{
                    'bSortable':false,
                    'aTargets':['nosort'],
                }],
                // columnDefs:[
                    //     {type:'date-dd-mm-yyyy',aTargets:[2]}
                    // ],
                    // 'aoColumns':[
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        // ],
                        "order":false,
                        "bLengthChange":false,
                        "dom":'<"top">ct<"top"p><"clear">'
                        // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                        // "iDisplayLength": 3
                    });
                    $("#filterbox-log").keyup(function(){
                        dataTable.search(this.value).draw();
                    });
                } );
                
                //finish table log
                $(document).ready( function () {
                    var dataTable = $('#fm_log').DataTable({
                        "pageLength":10,
                        'aoColumnDefs':[{
                            'bSortable':false,
                            'aTargets':['nosort'],
                        }],
                        // columnDefs:[
                            //     {type:'date-dd-mm-yyyy',aTargets:[2]}
                            // ],
                            // 'aoColumns':[
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                //     null,
                                // ],
                                "order":false,
                                "bLengthChange":false,
                                "dom":'<"top">ct<"top"p><"clear">'
                                // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                                // "iDisplayLength": 3
                            });
                            $("#filterbox-fm-log").keyup(function(){
                                dataTable.search(this.value).draw();
                            });
                        } );
                        
                        //unfinished log table
                        $(document).ready( function () {
                            var dataTable = $('#ufm_log').DataTable({
                                "pageLength":10,
                                'aoColumnDefs':[{
                                    'bSortable':false,
                                    'aTargets':['nosort'],
                                }],
                                // columnDefs:[
                                    //     {type:'date-dd-mm-yyyy',aTargets:[2]}
                                    // ],
                                    // 'aoColumns':[
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        //     null,
                                        // ],
                                        "order":false,
                                        "bLengthChange":false,
                                        "dom":'<"top">ct<"top"p><"clear">'
                                        // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                                        // "iDisplayLength": 3
                                    });
                                    $("#filterbox-ufm-log").keyup(function(){
                                        dataTable.search(this.value).draw();
                                    });
                                } );
                                
                                //es log table
                                $(document).ready( function () {
                                    var dataTable = $('#es_log').DataTable({
                                        "pageLength":10,
                                        'aoColumnDefs':[{
                                            'bSortable':false,
                                            'aTargets':['nosort'],
        }],
        // columnDefs:[
            //     {type:'date-dd-mm-yyyy',aTargets:[2]}
            // ],
            // 'aoColumns':[
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                //     null,
                // ],
                "order":false,
                "bLengthChange":false,
                "dom":'<"top">ct<"top"p><"clear">'
                // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                // "iDisplayLength": 3
            });
            $("#filterbox-es-log").keyup(function(){
                dataTable.search(this.value).draw();
            });
        } );
        
        //scrap table filter
        $(document).ready( function () {
            var dataTable = $('#scrap_filter').DataTable({
                "pageLength":10,
                'aoColumnDefs':[{
                    'bSortable':false,
                    'aTargets':['nosort'],
                }],
                // columnDefs:[
                    //     {type:'date-dd-mm-yyyy',aTargets:[2]}
                    // ],
                    // 'aoColumns':[
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        //     null,
                        // ],
                        "order":false,
                        "bLengthChange":false,
                        "dom":'<"top">ct<"top"p><"clear">'
                        // "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                        // "iDisplayLength": 3
                    });
                    $("#filterbox-scrap").keyup(function(){
                        dataTable.search(this.value).draw();
                    });
                } );
                // $(".pagination").addClass("justify-content-center");
                $("ul.pagination").addClass("justify-content-center");
                a = $(".pagination")
                a.addClass("justify-content-center");
          
                
                