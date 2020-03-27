from random import randint

import pytest


def test_data_model_proper_do_some_stuff(data_model_with_a):
    assert not data_model_with_a.do_some_stuff(1)
    assert data_model_with_a.do_some_stuff(2)


def test_data_model_do_some_stuff_without_a(data_model_with_two_b_items):
    assert not data_model_with_two_b_items.do_some_stuff(1)
    assert not data_model_with_two_b_items.do_some_stuff(randint(1, 10000))
    assert data_model_with_two_b_items.a is None


def test_data_model_do_any_other_stuff(full_data_model):
    assert full_data_model.c is not None

    assert not full_data_model.do_any_other_stuff(4)
    assert full_data_model.do_any_other_stuff(2)

    full_data_model.c = None

    assert not full_data_model.do_any_other_stuff(4)
    assert not full_data_model.do_any_other_stuff(2)


def test_data_model_do_some_extra_stuff(make_any_data_model):
    data_model = make_any_data_model(b=['a', 'b'])

    with pytest.raises(ValueError):
        data_model.do_some_extra_stuff()

    data_model.a = 5

    assert data_model.do_some_extra_stuff() == 'a_0_5,b_1_5'
