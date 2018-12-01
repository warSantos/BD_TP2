function showLoading() {
  $("#chart-area").hide("slow", function() {
    $('#chart-area').html("<img src='/static/img/loading.gif' class='loading-img' alt=''></img>");
    $('#chart-area').show("slow");
  });
}

function numberByAgeChart() {
  showLoading();
  $.ajax({
    url: 'numberbyage',
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

function numberByGenreChart() {
  showLoading();
  $.ajax({
    url: 'numberbygenre',
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

function performanceByGenreChart() {
  showLoading();
  $.ajax({
    url: 'performancebygenre',
    dataType: 'json',
    success: function (data) {
      console.log(data);
      $('#chart-area').html("");
      dataProvider = [];
      values = {};
      values["Tipo"] = "Nota CH"
      $.each(data.content.result, function(index, value) {
        if (value.genre == "F") {
          values["Feminino"] = value.media_NOTA_CH;
        } else {
          values["Masculino"] = value.media_NOTA_CH;
        }
      });
      dataProvider.push(values);
      values["Tipo"] = "Nota CN"
      $.each(data.content.result, function(index, value) {
        if (value.genre == "F") {
          values["Feminino"] = value.media_NOTA_CN;
        } else {
          values["Masculino"] = value.media_NOTA_CN;
        }
      });
      dataProvider.push(values);
      values["Tipo"] = "Nota LC"
      $.each(data.content.result, function(index, value) {
        if (value.genre == "F") {
          values["Feminino"] = value.media_NOTA_LC;
        } else {
          values["Masculino"] = value.media_NOTA_LC;
        }
      });
      dataProvider.push(values);
      values["Tipo"] = "Nota MT"
      $.each(data.content.result, function(index, value) {
        if (value.genre == "F") {
          values["Feminino"] = value.media_NOTA_MT;
        } else {
          values["Masculino"] = value.media_NOTA_MT;
        }
      });
      dataProvider.push(values);
      console.log(dataProvider);
      AmCharts.makeChart("chart-area", {
        "type": "radar",
        "theme": "light",
        "dataProvider": dataProvider,
        "startDuration": 1,
        "valueAxes": [{
          "maximum": 1000,
          "minimum": 0
        }],
        "graphs": [ {
          "balloonText": "Feminino: [[value]]",
          "bullet": "round",
          "lineThickness": 2,
          "valueField": "Feminino"
        },
        {
          "balloonText": "Masculino: [[value]]",
          "bullet": "round",
          "lineThickness": 2,
          "valueField": "Masculino"
        }],
        "categoryField": "Tipo",
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