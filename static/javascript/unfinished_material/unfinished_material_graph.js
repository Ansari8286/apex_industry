var ufm_quantity_graph = JSON.parse(document.getElementById("ufm_quantity_graph").textContent);
var sale_quantity_graph = JSON.parse(document.getElementById("sale_quantity_graph").textContent);

var dic_q = JSON.stringify(ufm_quantity_graph);
var dic_s = JSON.stringify(sale_quantity_graph);

// if (dic_q == '{}' && dic_s == "{}"){
//   document.getElementById("no_data_uf").innerHTML = "<br><div class='alert alert-light lead'><strong>Note:</strong> No Data Available</div>";
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
            label: "UFM Sale",
            backgroundColor: 'rgba(69, 123, 157)',
            borderColor: 'rgba(69, 123, 157, 1)',
            borderWidth: 1,
            data: [sale_quantity_graph['Round'], sale_quantity_graph['Square'],]
        },
        {
            label: "UFM Quantity",
            backgroundColor: 'rgba(29, 53, 87)',
            borderColor: 'rgba(29, 53, 87, 1)',
            borderWidth: 1,
            data: [ufm_quantity_graph['Round'],ufm_quantity_graph['Square'], ]
        },
    ],
  };
  
  var chartOptions = {
    responsive: true,
    legend: {
      display: false,
    },
    maintainAspectRatio: "false",
  }
  
  // window.onload = function() {
    var ctx = document.getElementById("ufmbar").getContext("2d");
    let myBar = new Chart(ctx, {
      type: "bar",
      data: barChartData,
      options: chartOptions
    });
  // };
// }
const updateUnFinishedMaterialGraph = (ufmSaleQuantityGraph, ufmQuantityGraph) => {
  myBar.data.datasets[0].data = [ufmSaleQuantityGraph['Round'], ufmSaleQuantityGraph['Square']];
  myBar.data.datasets[1].data = [ufmQuantityGraph['Round'], ufmQuantityGraph['Square']];
  myBar.update();
}
