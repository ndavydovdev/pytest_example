import string
from datetime import datetime
from random import choice, randint

import pytest

from .internal import AnyDataModelName

MAX_STR_LENGTH = 10
MAX_LIST_LENGTH = 5


def gen_string(max_length: int) -> str:
    return str(''.join(choice(string.ascii_letters) for _ in range(max_length)))


@pytest.fixture
def make_any_data_model():
    def make(**kwargs):
        return AnyDataModelName(
            a=kwargs.get('a'),
            b=kwargs.get('b') or [gen_string(randint(1, MAX_STR_LENGTH)) for i in range(randint(1, MAX_LIST_LENGTH))],
            c=kwargs.get('c')
        )
    return make


@pytest.fixture
def data_model_with_two_b_items(make_any_data_model):
    return make_any_data_model(b=['foo', 'bar'])


@pytest.fixture
def data_model_with_a(make_any_data_model):
    return make_any_data_model(a=2)


@pytest.fixture
def full_data_model(data_model_with_a):
    data_model_with_a.c = datetime(2019, 12, 29)
    return data_model_with_a


