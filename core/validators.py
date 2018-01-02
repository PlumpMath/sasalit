# -*- encoding: utf8 -*-

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_semester(value):
    if value < 1 or value > 2:
        raise ValidationError(
            _('%(value)s는 올바른 학기가 아닙니다.'),
            params={'value': value},
        )


def validate_year(value):
    if value < 2016 or value > 2100:
        raise ValidationError(
            _('%(value)s는 올바른 연도가 아닙니다.'),
            params={'value': value},
        )
