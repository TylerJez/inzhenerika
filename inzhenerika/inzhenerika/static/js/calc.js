/*Обрабатываем нажатия на кнопки + и - */
$('.minpl').click(function () {
    /*Находим input*/
    $input = $(this).parent().find('.quant');
    var qty = Number($input.val());
    /*На случай, если количество не удалось определить (например, пользователь мог оставить поле пустым)*/
    if (isNaN(qty)) qty = 0;
    if ($(this).hasClass('plus')) {
        if (qty == 0) {
            qty = $input.data('min');
        } else {
            qty += $input.data('step');
        }
    } else {
        qty -= $input.data('step');
    }
    var min = $input.data('min');
    if (qty >= min) {
        $input.val(qty).trigger('input');
    } else {
        $input.val(0).trigger('input');
    }
    /*Передаем функции подсчета, обновления*/
    updateCalc($input);
});
/*Обрабатываем ввод с клавиатуры */
$('.quant').change(function () {
    var qty = $(this).val();
    if (isNaN(qty)) qty = 0;
    var min = $(this).data('min');
    var step = $(this).data('step');
    if (qty > 0) {
        /*Если вдруг число не кратно шагу, увеличиваем (только увеличение) до кратного*/
        qty = Math.ceil(qty / step) * step;
        if (qty < min) {
            qty = min;
        }
        $(this).val(qty).trigger('input');
    } else {
        $(this).val(0).trigger('input');
    }
    updateCalc($(this));
});
/*Считаем, обновляем значения*/
function updateCalc($input) {
    var qty = Number($input.val());
    if (isNaN(qty)) qty = 0;
    $input.parents('.t-row').find('.price').text(qty * $input.data('price') / $input.data('step'));
    var itog = 0;
    $input.parents('.calc-table').find('.price').each(function () {
        itog += parseInt($(this).text());
    });
    $input.parents('.calc-table').next().find('.val').text(itog);
}


$('form').keypress(function (event) {
    return event.keyCode != 13;
});
