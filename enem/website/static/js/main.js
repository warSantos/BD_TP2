function ageChart() {
  $("#chart-area").hide("slow", function() {
    $('#chart-area').html("<img src='/static/img/loading.gif' class='loading-img' alt=''></img>");
    $('#chart-area').show("slow");
  });
  $.ajax({
    url: 'age',
    dataType: 'json',
    success: function (data) {
      $('#chart-area').html("");
      AmCharts.makeChart("chart-area", {
        "type": "pie",
        "theme": "light",
        "dataProvider": data.content.result,
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
  });
}

function genreChart() {
  $("#chart-area").hide("slow", function() {
    $('#chart-area').html("<img src='/static/img/loading.gif' class='loading-img' alt=''></img>");
    $('#chart-area').show("slow");
  });
  $.ajax({
    url: 'genre',
    dataType: 'json',
    success: function (data) {
      $('#chart-area').html("");
      dataProvider = [];
      max = 0;
      $.each(data.content.result, function(index, value) {        
        switch(value.TP_SEXO) {
          case "F":
            dataProvider.push({
                "name": "Feminino",
                "points": value.COUNT,
                "color": "#ff7979",
                "bullet": "/static/img/female_avatar.png"
            });
            break;
          case "M":
            dataProvider.push({
                "name": "Masculino",
                "points": value.COUNT,
                "color": "#22a6b3",
                "bullet": "/static/img/male_avatar.png"
            });
            break;
        }
        max += value.COUNT;
      });
      AmCharts.makeChart("chart-area", {
          "type": "serial",
          "theme": "light",
          "dataProvider": dataProvider,
          "valueAxes": [{
              "maximum": max,
              "minimum": 0,
              "axisAlpha": 0,
              "dashLength": 4,
              "position": "left"
          }],
          "startDuration": 1,
          "graphs": [{
              "balloonText": "<span style='font-size:13px;'>[[category]]: <b>[[value]]</b></span>",
              "bulletOffset": 10,
              "bulletSize": 52,
              "colorField": "color",
              "cornerRadiusTop": 8,
              "customBulletField": "bullet",
              "fillAlphas": 0.8,
              "lineAlpha": 0,
              "type": "column",
              "valueField": "points"
          }],
          "marginTop": 0,
          "marginRight": 0,
          "marginLeft": 0,
          "marginBottom": 0,
          "autoMargins": false,
          "categoryField": "name",
          "categoryAxis": {
              "axisAlpha": 0,
              "gridAlpha": 0,
              "inside": true,
              "tickLength": 0
          },
          "export": {
            "enabled": true
          }
      });
    }
  });
}

$(document).ready(function () {  
  $('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
  });
});