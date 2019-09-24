#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Any, Mapping
import pytest
from pytypewriter import export, load, Exportable


class TestClass1(Exportable):
    __test__ = False  # pytest ignore

    def __init__(self, arg1: int, arg2: str = None):
        self.arg1 = arg1
        self.arg2 = arg2

    def export(self) -> Mapping[str, Any]:
        return {
            'arg1': self.arg1,
            'arg2': self.arg2
        }

    @classmethod
    def load(cls, data: Mapping[str, Any]) -> Any:
        return cls(**data)


@pytest.mark.parametrize(
    'obj,typename,attrs', [
        (
            TestClass1(arg1=1, arg2='test'),
            'tests.exchange.test_exportable.TestClass1',
            {
                'arg1': 1,
                'arg2': 'test'
            }
        ),
    ]
)
def test_export_load(obj, typename, attrs):
    """
    Arrange/Act: Export the object (`obj`) using the `export` function, then
        create a new object from the exported data using the `load` function.
    Assert: The object the `load` function returns meets the expectations.

    :param obj: the object
    :param typename: the object's type name
    :param attrs: a mapping of attribute values to check against the object
    """
    # Export the object.
    exported = export(obj)
    # Verify the `__typename__` value in the exported data.
    assert exported['__type__'] == typename

    # Load a new instance from the exported data.
    loaded = load(exported)
    # Check the attributes of the loaded object.
    for k, v in attrs.items():
        assert getattr(loaded, k) == v
