document.getElementById('send-btn').addEventListener('click', function(e) {
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
});