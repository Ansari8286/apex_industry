const rawMaterialGraph = (data=JSON.parse(document.getElementById("raw_material_coilweight_graph").textContent)) => { 
const raw_material_coilweight_graph = data
// raw_id = document.getElementById('raw_material_coilweight_graph')
console.log(raw_material_coilweight_graph)
var raw_dic = JSON.stringify(raw_material_coilweight_graph);
// console.log(raw_dic);
// RM Stock chart
if(raw_dic == "{}" ){
    document.getElementById("no_data_raw").innerHTML = "<br><div class='alert alert-light lead'><strong>Note:</strong> No Data Available</div>";
}
else{
var percent = "%";
var donut = document.getElementById("rmdonut");

var mychart = new Chart(donut, {
    type: 'doughnut',
    data: {
        labels: ['202Q', '304Q', '316Q'],
        datasets: [{
            label: 'Rm Stock',
            data: [raw_material_coilweight_graph['202Q'], raw_material_coilweight_graph['304Q'], raw_material_coilweight_graph['316Q']],
            backgroundColor: [
                'rgba(69, 123, 157)',
                'rgba(29, 53, 87)',
                'rgba(230, 57, 70)',
            ],
            borderColor: [
                'rgba(69, 123, 157, 0.7)',
                'rgba(29, 53, 87, 0.7)',
                'rgba(230, 57, 70, 0.7)',
            ],
            borderWidth: 0.3,
            hoverOffset: 10,
        }],
    },
    options: {
        plugins: {
            legend: {
                position: 'bottom',
            },
        }
    }
});
}
}
rawMaterialGraph(data=JSON.parse(document.getElementById("raw_material_coilweight_graph").textContent))