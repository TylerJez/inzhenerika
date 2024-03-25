$('.open-popup').click(function(e) {
    e.preventDefault();
    $('.popup-bg').fadeIn(10);
});

$('.close-popup').click(function() {
    $('.popup-bg').fadeOut(10);
});