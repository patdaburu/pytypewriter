#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from pytypewriter import pyfqn, PyTypewriterException


@pytest.mark.parametrize(
    'pytype,fqn',
    [
        (PyTypewriterException, 'pytypewriter.errors.PyTypewriterException'),
        (
            PyTypewriterException('object test'),
            'pytypewriter.errors.PyTypewriterException'
        ),
    ]
)
def test_pyfqn(pytype, fqn):
    """
    Arrange/Act:  Get the fully-qualified name (`fqn`) for a python type by
        calling the `pyfqn` method.
    Assert:  The function's return value matches the expectation.

    :param pytype: a python type
    :param fqn: the fully-qualified name of the python type
    """
    assert pyfqn(pytype) == fqn, (
        "The fully-qualified name ('fqn') should match the expectation."
    )
