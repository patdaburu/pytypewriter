#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from pytypewriter import pycls


@pytest.mark.parametrize(
    'fqn',
    [
        'pytypewriter.errors.PyTypewriterException'
    ]
)
def test_pycls(fqn):
    """
    Arrange/Act:  Pass a fully-qualified type name (`fqn`) to the `pycls`
        function.
    Assert:  The function returns the expected type.

    :param fqn: the fully-qualified type name
    """
    _pycls = pycls(fqn)
    assert isinstance(_pycls, type), (
        "The function should return a `type`."
    )
    print(fqn.split('.')[-1])
    assert _pycls.__name__ == fqn.split('.')[-1], (
        'The type name should match the fully-qualified name (fqn).'
    )
