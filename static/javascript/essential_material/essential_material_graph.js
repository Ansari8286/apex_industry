var essential_data_graph = JSON.parse(document.getElementById("essential_data_graph").textContent);

// console.log(essential_data_graph,'asdnkjasdksadkjas')
var dic_c = JSON.stringify(essential_data_graph);
if (dic_c == '{}') {
    document.getElementById("no_data_em").innerHTML = "<br><div class='alert alert-light lead'><strong>Note:</strong> No Data Available</div>";
}

else {

    // EM Stock Chart
    var ctx = document.getElementById("embar");
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Cylinder", "Belt", "Fevil", "Cutting Oil", "Cutter", "Polish Wheel", "Matt Wheel", "Buff", "Plastic Roll", "Conjunction Rod", "Powder Box", "Big Carton", "Small Plastic"],
            datasets: [{
                label: 'EM Stocks',
                data: [essential_data_graph['Cylinder'], essential_data_graph['Belt'], essential_data_graph['Fevil'], essential_data_graph['Cutting Oil'],
                essential_data_graph['Cutter'], essential_data_graph['Polish Wheel'], essential_data_graph['Matt Wheel'], essential_data_graph['Buff'],
                essential_data_graph['Plastic Roll'], essential_data_graph['Conjunction Rod'], essential_data_graph['Powder Box'],
                essential_data_graph['Big Carton'], essential_data_graph['Small Plastic']],
                backgroundColor: 'rgba(29, 53, 87, 0.9)',
                borderWidth: 0.3
            }]
        },
        options: {
            // indexAxis: 'y',
            responsive: true,
            legend: {
                display: false,
            }
        }
    });
}