//// Get Data

//get input
//run model on input
//get prediction
//display prediction


//Bar chart or Pie Chart with character amounts m v f

//Buble Chart with number of lines m v f -- genders diff colors

// Bubble Chart - words with animation on male vs female

//?Maybe male vs female characters with where they are on the credits?

var trace1 = {
    x: ['Male', 'Female', 'Non-gendered'],
    y: [4355, 2261, 2418],
    type: 'bar',
    text: ['Male Characters', 'Female Characters', 'Non-gendered Characters'],
    marker: {
        color: '#208C81'
        // color: 'rgb(185, 160, 185)'
    }
  };
  
  var data = [trace1];
  
  var layout = {
    title: 'Characters per Gender',
    font:{
      family: 'Raleway, sans-serif'
    },
    showlegend: false,
    xaxis: {
      tickangle: -45
    },
    yaxis: {
      zeroline: false,
      gridwidth: 2
    },
    bargap :0.05
  };
  
  Plotly.newPlot('charbar', data, layout);

  var trace2 = {
    x: ['Male', 'Female', 'Non-gendered'],
    y: [187727, 82221, 22995],
    type: 'bar',
    text: ['Male Lines', 'Female Lines', 'Non-gendered Lines'],
    marker: {
        color: '#30698C'
        // color: 'rgb(185, 160, 185)'
    }
  };
  
  var data = [trace2];
  
  var layout = {
    title: 'Lines per Gender',
    font:{
      family: 'Raleway, sans-serif'
    },
    showlegend: false,
    xaxis: {
      tickangle: -45
    },
    yaxis: {
      zeroline: false,
      gridwidth: 2
    },
    bargap :0.05
  };
  
  Plotly.newPlot('linesbar', data, layout);