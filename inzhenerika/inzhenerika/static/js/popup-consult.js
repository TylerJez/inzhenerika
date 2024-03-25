$('.open-popup-consult').click(function(e) {
    e.preventDefault();
    $('.popup-bg-consult').fadeIn(10);
});

$('.close-popup-consult').click(function() {
    $('.popup-bg-consult').fadeOut(10);
});