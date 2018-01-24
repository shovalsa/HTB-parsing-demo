function getTreeTypes(select) {
    var treeTypes = [];
    var options = select && select.options;
    var opt;

    for (var i=0; i<options.length; i++) {
      opt = options[i];

      if (opt.selected) {
        treeTypes.push(opt.value);
      }
    }
    return treeTypes;
  }

function appendTree(section){
  var node = document.createElement("IMG");
  var att = document.createAttribute("src");
  att.value = "/home/shoval/NLPProjects/openU/website/static/images/pos.png";
  node.setAttributeNode(att);
  section.appendChild(node)
}

function getSentence() {
    var treeTypeSelect = document.getElementById("annotators");
    var treeTypes = getTreeTypes(treeTypeSelect)
    var text = document.getElementById("text").value;
    console.log(text)

    for (var i=0; i<treeTypes.length; i++){
      document.getElementById("annotatorType").innerHTML = text;
    }
}


document.addEventListener("click", function () {
    getSentence()
});
