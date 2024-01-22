from typing import Any


def success(data: Any = None) -> dict:
    return {'status': True, 'message': 'success', 'data': data}


def fail(error) -> dict:
    return {'status': False, 'message': 'fail', 'error': error}
