$(".pagination").addClass("justify-content-center");
var finished_material_quantity_graph = JSON.parse(document.getElementById("finished_material_quantity_graph").textContent);
var sale_graph = JSON.parse(document.getElementById("sale_graph").textContent);
var essential_items_graph = JSON.parse(document.getElementById("essential_items_graph").textContent);
var essential_use_graph = JSON.parse(document.getElementById("essential_use_graph").textContent);

var empty_f_q = JSON.stringify(finished_material_quantity_graph)
var empty_f_s = JSON.stringify(sale_graph)
var empty_es_s = JSON.stringify(essential_items_graph)
var empty_es_u = JSON.stringify(essential_use_graph)

if( empty_es_s == '{}' && empty_es_u == '{}'){
	document.getElementById("no_data_es_o").innerHTML = "<br><div class='alert alert-light lead'><strong>Note:</strong> No Data Available</div>";
}
else{
// Essential Stock Flow chart
var stkflow = document.getElementById("myBar");
var myChart = new Chart(stkflow, {
	type: 'bar',
	data: {
		labels: ["Cylinder", "Belt", "Fevil", "Cutting Oil", "Cutter", "Polish Wheel", "Matt Wheel", "Buff", "Plastic Roll", "Conjunction Rod", "Powder Box", "Big Carton", "Small Plastic"],
		datasets: [{
			label: 'Stock',
			backgroundColor: "rgba(29, 53, 87)",
			data: [essential_items_graph['Cylinder'],essential_items_graph['Belt'],essential_items_graph['Fevil'],essential_items_graph['Cutting Oil'],
					essential_items_graph['Cutter'],essential_items_graph['Polish Wheel'],essential_items_graph['Matt Wheel'],essential_items_graph['Buff'],
					essential_items_graph['Plastic Roll'],essential_items_graph['Conjunction Rod'],essential_items_graph['Powder Box'],
					essential_items_graph['Big Carton'], essential_items_graph['Small Plastic']],
		}, {
			label: 'Usage',
			backgroundColor: "rgba(230, 57, 70)",
			data: [-essential_use_graph['Cylinder'],-essential_use_graph['Belt'],-essential_use_graph['Fevil'],-essential_use_graph['Cutting Oil'],
					-essential_use_graph['Cutter'],-essential_use_graph['Polish Wheel'],-essential_use_graph['Matt Wheel'],-essential_use_graph['Buff'],
					-essential_use_graph['Plastic Roll'],-essential_use_graph['Conjunction Rod'],-essential_use_graph['Powder Box'],
					-essential_use_graph['Big Carton'], -essential_use_graph['Small Plastic']],
		}],
	},
	options: {
		indexAxis: 'y',
		plugins: {
			title: {
				display: false,
				text: 'Chart'
			},
		},
		responsive: true,
		scales: {
			x: {
				stacked: true,
			},
			y: {
				stacked: true,
			}
		}
	},
});
}

// FM Made and Sell chart
if( empty_f_s == '{}' && empty_f_q == '{}'){
	document.getElementById("no_data_fmf_o").innerHTML = "<br><div class='alert alert-light lead'><strong>Note:</strong> No Data Available</div>";
}
var speedCanvas = document.getElementById("myMixChart");

var dataFirst = {
    label: "Quantity Produced",
	data: [finished_material_quantity_graph['01'],finished_material_quantity_graph['02'],finished_material_quantity_graph['03'],finished_material_quantity_graph['04'],finished_material_quantity_graph['05'],finished_material_quantity_graph['06'],finished_material_quantity_graph['07'],finished_material_quantity_graph['08'],finished_material_quantity_graph['09'],finished_material_quantity_graph['10'],finished_material_quantity_graph['11'],finished_material_quantity_graph['12']],
    fill: true,
    backgroundColor: "rgba(230, 57, 70)",
    borderColor: 'red',
    order: 1,
    type: 'bar'
};

var dataSecond = {
    label: "Quantity Sale",
	data: [sale_graph['01'],sale_graph['02'],sale_graph['03'],sale_graph['04'],sale_graph['05'],sale_graph['06'],sale_graph['07'],sale_graph['08'],sale_graph['09'],sale_graph['10'],sale_graph['11'],sale_graph['12']],
    lineTension: 0,
    fill: false,
    borderColor: "rgba(29, 53, 87)",
    order: 0,
    type: 'line'
};

var speedData = {
labels: ["Jan", "Feb", "March", "April", "May", "June", "July","Aug","Sep","Oct","Nov","Dec"],
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
data: speedData,
options: chartOptions
});

// FM Made and Sell chart
