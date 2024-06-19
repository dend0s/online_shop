from django.core.exceptions import ValidationError


def phone_number_validator(number):
    if len(number) == 11 and (number[0] == '7' or number[0] == '8'):
        return number
    raise ValidationError('Некорректный номер телефона')
