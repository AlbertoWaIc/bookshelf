from datetime import datetime

MAX_LENGTH = 255

# 日付がString型のものdate型にする処理
def string_to_date_type(date):
    date_format = "%Y-%m-%d"

    try:
        date_object = datetime.strptime(date, date_format).date()
    except ValueError:
        date_object = date
    return date_object


def truncate_text_for_char(text):
    if len(text) > MAX_LENGTH:
        truncated_text = text[:MAX_LENGTH-3] + "..."
        return truncated_text
    else:
        return text
