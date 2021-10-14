var fm_quantity_graph = JSON.parse(document.getElementById("fm_quantity_graph").textContent);
var sale_quantity_graph = JSON.parse(document.getElementById("sale_quantity_graph").textContent);
var dic_f_q = JSON.stringify(fm_quantity_graph);
var dic_f_s = JSON.stringify(sale_quantity_graph);

// if (dic_f_q == '{}' && dic_f_s == "{}"){
//   document.getElementById("no_data_fm").innerHTML = "<br><div class='alert alert-light lead'><strong>Note:</strong> No Data Available</div>";
// }
// else{
// FM Stock Chart

var barChartData = {
    labels: [
      "Round",
      "Square"
    ],
    datasets: [
        {
            label: "FM Sale",
            backgroundColor: 'rgba(69, 123, 157)',
            borderColor: 'rgba(69, 123, 157, 1)',
            borderWidth: 1,
            data: [sale_quantity_graph['Round'], sale_quantity_graph['Square'],]
        },
        {
            label: "FM Quantity",
            backgroundColor: 'rgba(29, 53, 87)',
            borderColor: 'rgba(29, 53, 87, 1)',
            borderWidth: 1,
            data: [fm_quantity_graph['Round'],fm_quantity_graph['Square']]
        },
        // {
        //     label: "FM Sale",
        //     backgroundColor: 'rgba(230, 57, 70)',
        //     borderColor: 'rgba(230, 57, 70, 1)',
        //     borderWidth: 1,
        //     data: [6, 9,]
        // }
    ],
  };
  
  var chartOptions = {
    responsive: true,
    legend: {
      position: "top",
      display: false
    },
    maintainAspectRatio: "false",
  }
  
  // window.onload = function() {
    var ctx = document.getElementById("fmbar").getContext("2d");
    let myBar = new Chart(ctx, {
      type: "bar",
      data: barChartData,
      options: chartOptions
    });
  // };

  const updateFinishedMaterialGraph = (saleQuantityGraph, fmQuantityGraph) => {
    myBar.data.datasets[0].data = [saleQuantityGraph['Round'], saleQuantityGraph['Square']];
    myBar.data.datasets[1].data = [fmQuantityGraph['Round'],fmQuantityGraph['Square']];
    myBar.update();
}

// }
