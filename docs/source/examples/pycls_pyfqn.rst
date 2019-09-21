.. _pycls_pyfqn:

Using `pycls` and `pyfqn`
-------------------------

You can use :py:func:`pytypewriter.types.pyfqn` to get a fully-qualified
type name for an object, or you can go the other direction and get the python
`type` from a fully-qualified name.

.. code-block::

    from pytypewriter import pyfqn, pycls

    # Create an object, any object.
    s = "I am a string."
    # Get its fully-qualified type name (fqn).
    fqn = pyfqn(s)
    # Let's see what we have.
    print(f"The fully-qualified type name is: {fqn}")

    # Now let's take the fully-qualified name (fqn) and get the type.
    cls = pycls(fqn)
    # What's that type?
    print(f"The type is: {cls}")

.. code-block:: coq

    The fully-qualified type name is: builtins.str
    The type is: <class 'str'>
