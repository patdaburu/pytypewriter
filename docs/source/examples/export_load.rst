.. _export_load:

Using `export` and `load`
-------------------------

Python provides lots of mechanisms for serializing and de-serializing
classes, like `pickle <https://docs.python.org/3/library/pickle.html>`_
and the
`__getstate__() <https://docs.python.org/2/library/pickle.html#object.__getstate__>`_
and `__setstate__() <https://docs.python.org/2/library/pickle.html#object.__setstate__>`_
magic methods.  You could use
`dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ or
`named tuples <https://docs.python.org/3/library/collections.html#collections.namedtuple>`_
or even the `__repr__() <https://realpython.com/courses/pythonic-oop-string-conversion-__repr__-vs-__str__/>`_
magic method... and the list goes on!

The main goal of the :py:func:`export() <pytypewriter.exchange.export>` and
:py:func:`load() <pytypewriter.exchange.export>` methods is to provide a regular
way to create simple mappings that represent the state of an object in such a
way that you can easily re-create an instance with the same state.  Once you have
your mapping, you can serialize it to
`JSON <https://docs.python.org/3/library/json.html>`_ or
`TOML <https://pypi.org/project/toml/>`_, or you can use it in whatever way suits
your needs.

The main differences between using this method and others are:

    * type information is included in the mapping; and
    * you can use standard object initialization methods to recreate your instances, so
    * you can take pretty fine-grained control over just exactly how serialization and
      de-serialization of your types works.

So, maybe this is for you and maybe it isn't, but let's discuss how it works.


The ``Exportable`` Mixin
^^^^^^^^^^^^^^^^^^^^^^^^

The first step toward taking advantage of this export/load process is to have your
class extended the :py:class:`Exportable <pytypewriter.exchange.Exportable>` mixin
which requires that you implement the
:py:func:`export <pytypewriter.exchange.Exportable.export>` instance method and
the :py:func:`load <pytypewriter.exchange.Exportable.export>` class method.

.. code-block::

    from typing import Any, Mapping
    from pytypewriter import Exportable

    class SampleClass(Exportable):
        """
        This class was written just for this demonstration article.
        """
        def __init__(self, arg1: int, arg2: str = None):
            """

            :param arg1: an integer
            :param arg2: a string
            """
            self.arg1 = arg1
            self.arg2 = arg2

        def export(self) -> Mapping[str, Any]:
            """
            Export the instance as a mapping of simple types.

            :return: the mapping
            """
            return {
                'arg1': self.arg1,
                'arg2': self.arg2
            }

        @classmethod
        def load(cls, data: Mapping[str, Any]) -> Any:
            """
            Create an instance from a mapping.

            :param data: the data
            :return: the instance
            """
            return cls(**data)

The ``export`` Function
^^^^^^^^^^^^^^^^^^^^^^^

Now that your class extends ``Exportable``, we can call the ``export`` function on it directly,
or we can get a little more meta information for free by using the
:py:func:`export() <pytypewriter.exchange.export>` function.

.. code-block:: python

    import json
    from pytypewriter import export

    sample_class = SampleClass(arg1=100, arg2='hello')

    exported = export(sample_class)

    # Just to make things a little easier to read, let's
    # convert the exported data to JSON before we have a look.
    print(json.dumps(exported, indent=4))

Notice that the ``export`` function included the fully-qualified type name.

.. code-block:: coq
    :linenos:
    :emphasize-lines: 4

    {
        "arg1": 100,
        "arg2": "hello",
        "__type__": "my_module.SampleClass"
    }

The ``load`` Function
^^^^^^^^^^^^^^^^^^^^^

If we extend the sample above, we can take the exported data and re-create an instance of
the with the original state.

.. code-block:: python

    from pytypewriter import load

    loaded = load(exported)

    print(f'The loaded type is: {type(loaded)}.')
    print(f'arg1 = {repr(loaded.arg1)}')
    print(f'arg2 = {repr(loaded.arg2)}')

.. code-block:: coq

    The loaded type is: <class 'my_module.SampleClass'>.
    arg1 = 100
    arg2 = 'hello'