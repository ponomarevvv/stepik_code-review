# Задача
Реализовать проверку наличия кнопки добавления в корзину

# Реализация
Проверка реализована для браузеров Mozilla Firefox и Google Chrome и для каждой локализации страницы

# Использование
Шаблон:
pytest -{опции/флаги запуска} --{агрумент1}={значение1} --{агрумент2}={значение2}... test_items.py

Доступные аргументы:<br>
  --browser={имя_браузера}<br>
      значения: chrome (выбран по-умолчанию),
                firefox<br>
  --language={язык}<br>
      значения : en-gb (выбран по-умолчанию), fr, es, ar, ca, cs, da, de, el, fi, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk

Пример использования:<br>
$ pytest test_items.py - запуск теста страницы на английском языке в Google Chrome<br>
$ pytest --language=fr --browser=firefox test_items.py - запуск теста страницы на французском языке в Mozilla Firefox

