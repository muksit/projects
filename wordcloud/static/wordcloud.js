$(function(){

var fill = d3.scale.category20c();


var phrases = "very, so, not"

request = $.get("/ask", {word: "josh"}, function(data){
    var sampletext = data;

    var splittext = sampletext.split(" ");

    d3.layout.cloud().size([2000, 2000])
        .words(splittext.map(function(d) {
        return {text: d, size: 15 * (getFrequency(sampletext)[d])+5 };
        }))
        .rotate(function() { return ~~(Math.random() * 2) * 90; })
        .font("Impact")
        .fontSize(function(d) { return d.size; })
        .on("end", draw)
        .start();

    var wordfrequency = getFrequency(sampletext);
    var keys = [];
    keys = Object.keys(wordfrequency);

    function draw(words) {
      d3.select("body").append("svg")
          .attr("width", 2000)
          .attr("height", 2000)
        .append("g")
          .attr("transform", "translate(850,650)")
        .selectAll("text")
          .data(words)
        .enter().append("text")
          .style("font-size", function(d) { return d.size + "px"; })
          .style("font-family", "Impact")
          .style("fill", function(d, i) { return fill(i); })
          .attr("text-anchor", "middle")
          .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
          })
          .text(function(d) { return d.text; });
    };


  
  });




/*var filteredlist = filter(keys)


function filter(list){
  var newlist = [];
  for (var x=0; x < list.length; x++) {
      if (containsObject(list[x], splitblacklist) == true) {
        newlist.pop(list[x])
      }
      else{
        newlist.push(list[x])
      }
    }
   return newlist }  */




/*function containsObject(obj, list) {    
    for ( var i = 0; i < list.length; i++) {
        if (list[i] === obj) {
            return true;
        }
    }
    return false;
}*/



  function getFrequency(text) {
    var freq = {};
    var arraytext = text.split(" ");
    for (var i=0; i < arraytext.length; i++) {
      var word = arraytext[i];      
        if (freq[word]) {
          freq[word]++;
        } 
        else {
           freq[word] = 1;
        }
    }

    return freq;
  };




  
  

});