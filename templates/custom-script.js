$(window).resize(function(){
  $(".home-page-content").height( ($( window ).height()) - ($(".main-header").height()) - ($(".main-footer").height()));
});
$(window).ready(function(){
  $(".home-page-content").height( ($( window ).height()) - ($(".main-header").height()) - ($(".main-footer").height()));
});
