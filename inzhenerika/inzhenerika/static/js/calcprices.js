document.addEventListener('DOMContentLoaded', function() {
    var typeSelect = document.getElementById('type');
    var priceInputs = document.querySelectorAll('.calc-table-td:nth-child(4) input');

    typeSelect.addEventListener('change', function() {
        var selectedOption = typeSelect.options[typeSelect.selectedIndex];
        var priceValue = selectedOption.getAttribute('data-price');

        priceInputs.forEach(function(input) {
            input.value = priceValue;
        });
    });

    var calculateTotal = function() {
        var totals = 0;
        priceInputs.forEach(function(input) {
            var count = Number(input.parentNode.querySelector('.number-text').value);
            var price = Number(input.value);
            var total = count * price;

            input.parentNode.querySelector('.calc-table-td:nth-child(5)').textContent = total;
            totals += total;
        });

        document.getElementById('total').textContent = totals;
    };

    priceInputs.forEach(function(input) {
        input.parentNode.querySelector('.number-text').addEventListener('input', calculateTotal);
    });

    calculateTotal();
});