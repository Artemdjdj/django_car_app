



$(document).ready(function () {
    $('.thumbnail').click(function () {
        var src = $(this).attr('src');
        $('.carousel-item').removeClass('active');
        $('.carousel-item img[src="' + src + '"]').parent().addClass('active');
        $('#carouselExampleInterval').carousel($('.carousel-item.active').index());
    });
});