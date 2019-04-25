// const d3 = require("d3.js");

let rect_color = {
  "0": "white",
  "2": "#87CEEB",
  "4": "yellow",
  "-1": "grey",
  "s":"red",
  "d":"red"
}

let select_vm = new Vue({
  el: '#inputdiv',
  data: {
    selected:'',
    graphList: [
      
    ]    
  },
  created: function (){
    this.getFileNames()
  },
  methods: {
    getFileNames: function(){
      var vm = this;
      axios.get('/graph?type=filenames')
        .then(function (response) {
          // vm.answer = _.capitalize(response.data.answer)
          // console.log(eval(response.data));

          // for (data of response.data){
          //   vm.graphList.push(data);
          // }
          vm.graphList = response.data;
        })
        .catch(function (error) {
          console.log('Error! Could not reach the API. ' + error)
        })
    },
    filechange: function(){
      clear();
      // console.log(this.selected);
      var vm = this;
      axios.get('/graph?type=getdata&file=' + this.selected)
        .then(function (response) {
          draw_topo(response.data);
        })
        .catch(function (error) {
          console.log('Error! Could not reach the API. ' + error)
        })
    },
    getResult: function(){
      var vm = this;
      axios.get('/graph?type=getresult&file=' + this.selected)
        .then(function (response) {
          draw_result(response.data);
        })
        .catch(function (error) {
          console.log('Error! Could not reach the API. ' + error)
        })
    },
    clear: function(){
      clear();
    }
  }
})
// select_vm.getFileNames();

const svg = d3.select("svg#topo");
function draw_topo(data){
  let graph_width = data.width;
  let graph_height = data.height; 
  
  const svg_width = svg.attr("width");
  const svg_height = svg.attr("height");

  let r = svg_width / graph_width > svg_height / graph_height ? svg_height / graph_height : svg_width / graph_width;

  for (i in data.graph){
    for (j in data.graph[i]){
      svg.append("rect")
        .attr("id", i + "a" + j)
        .attr("x", j * r)
        .attr("y", i * r)
        .attr("width", r)
        .attr("height", r)
        .attr("fill", rect_color[data.graph[i][j]])
        .attr("stroke", "#333")
        .attr("stroke-width", "1px")
    }
  }

  $("#" + data.src[0] + "a" + data.src[1]).attr("fill", "red");
  $("#" + data.dst[0] + "a" + data.dst[1]).attr("fill", "red");

}

function draw_result(data){
  for (p of data.path){
    $("#" + p[0] + "a" + p[1]).attr("fill", "red");
    $("#" + p[0] + "a" + p[1]).attr("fill", "red");
  }

  

}

function clear(){
  svg.selectAll("rect").remove();
}