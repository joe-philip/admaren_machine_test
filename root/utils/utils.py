from datetime import datetime
from typing import Any

from django.utils.text import slugify
from pytz import timezone


def success(data: Any = None) -> dict:
    return {'status': True, 'message': 'success', 'data': data}


def fail(error) -> dict:
    return {'status': False, 'message': 'fail', 'error': error}


def slug_generate(key: str = 'slug') -> str:
    return slugify(f'{key}-{datetime.now(tz=timezone("Asia/Calcutta"))}')
