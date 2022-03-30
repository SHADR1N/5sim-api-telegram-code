# Быстрая инструкция

API настроен на получение номеров для телеграм аккаунтов</br>
Используются любые доступные операторы</br>
Страны используемые 'russia', 'ukraine', 'belarus', 'kazakhstan'</br>

```{python}{
# Создаем подключение
api = FiveSms('YOUR API KEY')
# Получаем баланс
api.balance()

# Получаем номер телефон
phone = api.get_phone()
if phone:
    # Получаем код
    code = api.get_code()
else:
    # Если номеров нет, то видим сообщение
    print('No free phone.')

