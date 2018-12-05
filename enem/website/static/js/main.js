function showLoading(text) {
  $('.chart-title').html(text);
  $('.chart-title').show("slow");
  $('#chart-area').hide();
  $('#loading-area').show();
  $('#chart-content').show("slow");
}

function showChart() {
  $('#loading-area').hide();
  $('#chart-area').show();
}

$('#confButton').click(function() {
  $('#chart-content').show("slow");
  showChart();
  var map = AmCharts.makeChart( "chart-area", {
    "type": "map",
    "theme": "light",
    "panEventsEnabled": true,
    "dataProvider": {
      "map": "brazilLow",
      "getAreasFromMap": true
    },
    "areasSettings": {
      "autoZoom": false,
      "color": "#CDCDCD",
      "colorSolid": "#5EB7DE",
      "selectedColor": "#5EB7DE",
      "outlineColor": "#666666",
      "rollOverColor": "#88CAE7",
      "rollOverOutlineColor": "#FFFFFF",
      "selectable": true
    },
    "listeners": [ {
      "event": "clickMapObject",
      "method": function( event ) {
        Cookies.set('place', event.mapObject.id.substring(3, 6));
        $("#place").html(Cookies.get('place'));
      }
    }]
  } );
});

$('#numberByGenreChart').click(function() {    
  showLoading($(this).html());
  $.ajax({
    type: "POST",
    url: 'numberbygenre',
    dataType: 'json',
    data: { place: Cookies.get('place') },
    success: function (data) {
      showChart();
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
});

$('#numberByAgeChart').click(function() {
  showLoading($(this).html());
  $.ajax({
    type: "POST",
    url: 'numberbyage',
    dataType: 'json',
    data: { 'place': Cookies.get('place') },
    success: function (data) {
      showChart();
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
});

$('#numberByLanguageChart').click(function() {
  showLoading($(this).html());
  $.ajax({
    type: "POST",
    url: 'numberbylanguage',
    dataType: 'json',
    data: { 'place': Cookies.get('place') },
    success: function (data) {
      showChart();
      dataProvider = [];
      $.each(data.content.result, function(index, value) {        
        switch(value.TP_LINGUA) {
          case "0":
            dataProvider.push({
              "title": "Inglês",
              "value": value.COUNT
            });
            break;
          case "1":
            dataProvider.push({
              "title": "Espanhol",
              "value": value.COUNT
            });
            break;
        }
      });
      AmCharts.makeChart("chart-area", {
        "type": "pie",
        "theme": "light",
        "dataProvider": dataProvider,
        "titleField": "title",
        "valueField": "value",
        "labelRadius": 5,
        "radius": "42%",
        "innerRadius": "60%",
        "labelText": "[[title]]",
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
});

$('#numberByInternetChart').click(function() {
  showLoading($(this).html());
  $.ajax({
    type: "POST",
    url: 'numberbyinternet',
    dataType: 'json',
    data: { 'place': Cookies.get('place') },
    
    success: function (data) {
      showChart();
      dataProvider = [];
      $.each(data.content.result, function(index, value) {        
        switch(value.Q025) {
          case "A":
            dataProvider.push({
              "title": "Não",
              "value": value.COUNT
            });
            break;
          case "B":
            dataProvider.push({
              "title": "Sim",
              "value": value.COUNT
            });
            break;
        }
      });
      AmCharts.makeChart("chart-area", {
        "type": "pie",
        "theme": "light",
        "dataProvider": dataProvider,
        "titleField": "title",
        "valueField": "value",
        "labelRadius": 5,
        "radius": "42%",
        "innerRadius": "60%",
        "labelText": "[[title]]",
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
});

$('#numberByPresenceChart').click(function() {
  showLoading($(this).html());
  $.ajax({
    url: 'numberbypresence',
    dataType: 'json',
    success: function (data) {
      console.log(data.content.result);
      showChart();
      AmCharts.makeChart("chart-area", {
        "theme": "light",
        "type": "serial",
        "dataProvider": data.content.result,
        "startDuration": 1,
        "graphs": [{
            "balloonText": "Presentes: [[value]]",
            "fillAlphas": 0.9,
            "lineAlpha": 0.2,
            "title": "Presentes",
            "type": "column",
            "clustered":false,
            "columnWidth":0.3,
            "valueField": "Presentes"
        }, {
            "balloonText": "Ausentes: [[value]]",
            "fillAlphas": 0.9,
            "lineAlpha": 0.2,
            "title": "Ausentes",
            "type": "column",
            "clustered":false,
            "columnWidth":0.4,
            "valueField": "Ausentes"
        }, {
          "balloonText": "Eliminados: [[value]]",
          "fillAlphas": 0.9,
          "lineAlpha": 0.2,
          "title": "Eliminados",
          "type": "column",
          "clustered":false,
          "columnWidth":0.5,
          "valueField": "Eliminados"
        }],
        "plotAreaFillAlphas": 0.1,
        "categoryField": "Dia",
        "categoryAxis": {
            "gridPosition": "start"
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
});

$('#performanceByGenreChart').click(function() {
  showLoading($(this).html());
  $.ajax({
    type:"POST",
    url: 'performancebygenre',
    dataType: 'json',
    data: { 'place': Cookies.get('place') },
    
    success: function (data) {
      console.log(data);
      showChart();
      dataProvider = [];
      values = {};
      values["Tipo"] = "Ciências Humanas"
      $.each(data.content.result, function(index, value) {
        if (value.genre == "F") {
          values["Feminino"] = value.media_NOTA_CH;
        } else {
          values["Masculino"] = value.media_NOTA_CH;
        }
      });
      dataProvider.push(values);
      values = {};
      values["Tipo"] = "Ciências da Natureza"
      $.each(data.content.result, function(index, value) {
        if (value.genre == "F") {
          values["Feminino"] = value.media_NOTA_CN;
        } else {
          values["Masculino"] = value.media_NOTA_CN;
        }
      });
      dataProvider.push(values);
      values = {};
      values["Tipo"] = "Linguagens e Códigos"
      $.each(data.content.result, function(index, value) {
        if (value.genre == "F") {
          values["Feminino"] = value.media_NOTA_LC;
        } else {
          values["Masculino"] = value.media_NOTA_LC;
        }
      });
      dataProvider.push(values);
      values = {};
      values["Tipo"] = "Matemática"
      $.each(data.content.result, function(index, value) {
        if (value.genre == "F") {
          values["Feminino"] = value.media_NOTA_MT;
        } else {
          values["Masculino"] = value.media_NOTA_MT;
        }
      });
      dataProvider.push(values);
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
});

$('#performanceByEstadosChart').click(function() {
  showLoading($(this).html());
  $.ajax({
    url: 'performancebyestados',
    dataType: 'json',
    success: function(data){
      showChart();
      var chart = AmCharts.makeChart("chart-area", {
        "theme": "none",
        "type": "serial",
        "startDuration": 2,
        "dataProvider":data.content.result,
        "valueAxes": [{
            "position": "left",
            "title": "Nota"
        }],
        "graphs": [{
            "balloonText": "[[category]]: <b>[[value]]</b>",
            "fillColorsField": "color",
            "fillAlphas": 1,
            "lineAlpha": 0.1,
            "type": "column",
            "valueField": "media"
        }],
        "depth3D": 10,
      "angle": 30,
        "chartCursor": {
            "categoryBalloonEnabled": true,
            "cursorAlpha": 0,
            "zoomable": false
        },
        "categoryField": "estado",
        "categoryAxis": {
            "gridPosition": "start",
            "labelRotation": 90
        },
        "export": {
          "enabled": true
         }
    
    });
    
    }
  });
});

$('#situacaoEnsinoMedio').click(function() {
  showLoading($(this).html());
  console.log("Antes da chamada do ajax");
  $.ajax({
    type:"POST",
    url: 'situacaoensinomedio',
    dataType: 'json',
    data: { 'place': Cookies.get('place') },

    success: function(data){
      showChart();
      console.log("Definindo o gráfico :D");
      console.log(data["content"]);
      AmCharts.makeChart( "chart-area", {
        "type": "pie",
        "theme": "none",
        "dataProvider": data.content,
        "titleField": "title",
        "valueField": "value",
        "labelRadius": 5,
      
        "radius": "42%",
        "innerRadius": "60%",
        "labelText": "[[title]]",
        "legend":{
          "position":"right",
          "marginRight":100,
          "autoMargins":false
        },
        "export": {
          "enabled": true
        }
      } );
    },
    error: function(){
      console.log("Deu ruim man");
    },
    complete: function(){
      console.log("Completou man");
    }
  })
});

$(document).ready(function () {  
  if (Cookies.get('place') == undefined) {
    Cookies.set('place', 'BR');
  }
  $("#place").html(Cookies.get('place'));
  $('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
  });
});