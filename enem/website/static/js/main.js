$(function(){

  function ageChart() {
    var data = [];

    $("#chart-fields").find("input").each(function(index) {
      data.push({
        "age": $(this).attr("name"),
        "count": $(this).attr("count")
      });    
    });

    AmCharts.makeChart("chart-area", {
      "type": "pie",
      "theme": "light",
      "dataProvider": data,
      "valueField": "count",
      "titleField": "age",
      "balloon":{
      "fixedPosition":true
      },
      "legend":{
        "position":"right",
      "marginRight":100,
      "autoMargins":false
    },
      "export": {
        "enabled": true
      }
    });
  }

  ageChart();
});

