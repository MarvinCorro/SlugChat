$(function()
{
    var slideqty = $('#featured .item').length;
    var wheight = $(window).height(); //get the height of the window


    $('.fullheight').css('height', wheight); //set to window tallness  


    //replace IMG inside carousels with a background image
    $('#featured .item img').each(function()
    {
        var imgSrc = $(this).attr('src');
        $(this).parent().css(
        {
            'background-image': 'url(' + imgSrc + ')'
        });
        $(this).remove();
    });

    //adjust height of .fullheight elements on window resize
    $(window).resize(function()
    {
        wheight = $(window).height(); //get the height of the window
        $('.fullheight').css('height', wheight); //set to window tallness  
    });

    for (var i = 0; i < slideqty; i++)
    {
        var insertText = '<li data-target="#featured" data-slide-to="' + i + '"';
        insertText += '></li>';
        $('#featured ol').append(insertText);
    }

    $('#featured').carousel(
    {
        interval: 7000,
        pause: "false"
    });

    $(window).resize(function()
    {
        $(".home-page-content").height(($(window).height()) - ($(".main-header").height()) - ($(".main-footer").height()));
    });

    $(window).ready(function()
    {
        $(".home-page-content").height(($(window).height()) - ($(".main-header").height()) - ($(".main-footer").height()));
    });
});