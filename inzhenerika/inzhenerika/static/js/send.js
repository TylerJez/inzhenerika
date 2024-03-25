/*document.getElementById('send-btn').addEventListener('click', function(e) {
  e.preventDefault();
  var fields = document.getElementsByTagName('input');
  var isValid = true;

  for (var i = 0; i < fields.length; i++) {
      if (fields[i].value === '') {
          isValid = false;
          break;
      }
  }
  if (isValid) {
      alert('Заявка успешно отправлена! Ожидайте звонок с 10:00 до 16:30 по Новосибирскому времени на следующий рабочий день.');
      for (var i = 0; i < fields.length; i++) {
        fields[i].value = '';
    }

  } else {
      alert('Пожалуйста, заполните все поля формы.');
  }
});*/
document.getElementById('form-feedback').addEventListener('submit', function(event) {
  var inputs = this.querySelectorAll('input, textarea');
  var hasEmptyFields = Array.from(inputs).some(function(input) {
    return !input.value.trim();
  });

  if (hasEmptyFields) {
    event.preventDefault();
    alert('Пожалуйста, заполните все поля формы.');
  } else {
    event.preventDefault();
    alert('Спасибо за оставленный отзыв!');
    for (var i = 0; i < inputs.length; i++){
        inputs[i].value = '';
    }
  }
});

document.getElementById('form-consult').addEventListener('submit', function(event) {
  var inputs = this.querySelectorAll('input, textarea');
  var hasEmptyFields = Array.from(inputs).some(function(input) {
    return !input.value.trim();
  });

  if (hasEmptyFields) {
    event.preventDefault();
    alert('Пожалуйста, заполните все поля формы.');
  } else {
    event.preventDefault();
    alert('Вы оформили заявку на консультацию! Ожидайте звонок с 10:00 до 16:30 (+4 от МСК) следующего рабочего дня!');
    for (var i = 0; i < inputs.length; i++){
        inputs[i].value = '';
    }
  }
});