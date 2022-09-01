from datetime import datetime
import requests
import locale


def time_request(request):
    """Время для футера"""
    try:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')  # Выставляем форматирование дат для России
    except Exception as err:
        print(err)
    timestamp = str(requests.post('https://api.taxideli.ru/test/gettime').json()['dataAns'])  # Получаем значение даты
    timestamp_checked = timestamp[:10] if len(timestamp) > 10 else timestamp  # Приводим к десяти знакам
    return {
        'time_footer': datetime.fromtimestamp(int(timestamp_checked)).strftime('%a %d.%m.%Y %H:%M')
    }
