var currentPage = 0;

function start(){
if(PDFObject.supportsPDFs){
   console.log("Yay, this browser supports inline PDFs.");
} else {
   console.log("Boo, inline PDFs are not supported by this browser");
}
changePage(0);
setFrameOnAdjust();

}

function changePage(number){
var numval = String(number);
PDFObject.embed("../static/Planning.pdf", "#presentationFrame",{page: numval, height:"450px",width:"100%" });
}

function prevSlide(){
currentPage = currentPage - 1;
changePage(currentPage);
}

function nextSlide(){
currentPage = currentPage + 1;
changePage(currentPage);
}

function togglePanelBar(){
  console.log("toggleCalled");
  var windowHeight = $(window).height();
  var panelHeight = $("#bottomControlPanel").height();
  var newHeight = windowHeight - panelHeight;
  console.log($(window).height());
  console.log($("#bottomControlPanel").height());

  if (panelHeight < 50){
      setFrameHeight(windowHeight - 389 - 160);
  } else {
      setFrameHeight(windowHeight - 40 - 160);
  }
}

function setFrameOnAdjust(){
  console.log("toggleCalled");
  var windowHeight = $(window).height();
  var panelHeight = $("#bottomControlPanel").height();
  var newHeight = windowHeight - panelHeight;
  console.log($(window).height());
  console.log($("#bottomControlPanel").height());
  setFrameHeight(windowHeight - panelHeight - 160);
}

function setFrameHeight(number){
    console.log('setFrame: ',number);
  $("#presentationFrame > .pdfobject").height(number);
//  console.log($("#presentationFrame > .pdfobject").height());
}
