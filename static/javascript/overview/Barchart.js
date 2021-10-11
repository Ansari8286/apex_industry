$(".pagination").addClass("justify-content-center");
var raw_material_weight_graph = JSON.parse(document.getElementById("raw_material_weight_graph").textContent);
var raw_material_scrap_graph = JSON.parse(document.getElementById("raw_material_scrap_graph").textContent);
var finished_material_weight_graph = JSON.parse(document.getElementById("finished_material_weight_graph").textContent);
var finished_material_scrap_graph = JSON.parse(document.getElementById("finished_material_scrap_graph").textContent);

var empty_dic_month = JSON.stringify(raw_material_weight_graph)
var empty_dic_s_month = JSON.stringify(raw_material_scrap_graph)
var empty_dic_fm_w = JSON.stringify(finished_material_weight_graph)
var empty_dic_fm_s = JSON.stringify(finished_material_scrap_graph)

if ( empty_dic_month == "{}" && empty_dic_s_month == '{}' ){
    document.getElementById("no_data_rm_o").innerHTML = "<h5>Raw Material Monthly Data</h5><br><div class='alert alert-light lead'><strong>Note:</strong> No Data Available</div>";
}
else{
//First graph
var speedCanvas = document.getElementById("speedChart");

var dataFirst = {
    label: "Raw Material Weight",
    data: [raw_material_weight_graph['01'],raw_material_weight_graph['05'], raw_material_weight_graph['10'], raw_material_weight_graph['15'], raw_material_weight_graph['20'], raw_material_weight_graph['25'], raw_material_weight_graph['30']],
    lineTension: 0,
    fill: false,
    borderColor: "rgba(29, 53, 87)"
};

var dataSecond = {
    label: "Raw Material ScrapWeight",
    data: [raw_material_scrap_graph['01'], raw_material_scrap_graph['05'], raw_material_scrap_graph['10'], raw_material_scrap_graph['15'], raw_material_scrap_graph['20'], raw_material_scrap_graph['25'], raw_material_scrap_graph['30']],
    lineTension: 0,
    fill: false,
    borderColor: "rgba(230, 57, 70)"
};

var speedData = {
labels: ["1", "5", "10", "15", "20", "25", "30"],
datasets: [dataFirst, dataSecond]
};

var chartOptions = {
legend: {
    display: true,
    position: 'top',
    labels: {
    boxWidth: 80,
    fontColor: 'black'
    }
}
};

var lineChart = new Chart(speedCanvas, {
type: 'line',
data: speedData,
options: chartOptions
});
}

if (empty_dic_fm_w == '{}' && empty_dic_fm_s == '{}'){
    document.getElementById("no_data_fm_o").innerHTML = "<h5>Finish Material Monthly Data</h5><br><div class='alert alert-light lead'><strong>Note:</strong> No Data Available</div>";
}
else{
    let currentDate = new Date();
    let cDay = currentDate.getDate()

    if (finished_material_weight_graph['01']== undefined){
        finished_material_weight_graph['01'] = 0
        finished_material_scrap_graph['01']=0
    }
// second graph
var speedCanvas = document.getElementById("speedChart1");

var dataFirst = {
    label: "Finish Material Weight",
    data: [finished_material_weight_graph['01'], finished_material_weight_graph['05'], finished_material_weight_graph['10'], finished_material_weight_graph['15'], finished_material_weight_graph['20'], finished_material_weight_graph['25'], finished_material_weight_graph['30']],
    lineTension: 0,
    fill: false,
    borderColor: "rgba(29, 53, 87)"
};

var dataSecond = {
    label: "Finish Material ScrapWeight",
    data: [finished_material_scrap_graph['01'], finished_material_scrap_graph['05'], finished_material_scrap_graph['10'], finished_material_scrap_graph['15'], finished_material_scrap_graph['20'], finished_material_scrap_graph['25'], finished_material_scrap_graph['30']],
    lineTension: 0,
    fill: false,
    borderColor: "rgba(230, 57, 70)"
};

var speedData = {
labels: ["1", "5", "10", "15", "20", "25", "30"],
datasets: [dataFirst, dataSecond]
};

var chartOptions = {
legend: {
    display: true,
    position: 'top',
    labels: {
    boxWidth: 80,
    fontColor: 'black'
    }
}
};

var lineChart = new Chart(speedCanvas, {
type: 'line',
data: speedData,
options: chartOptions
});
}