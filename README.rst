Advent of Code 2020 Solutions in Python
=======================================
Advent of Code 2020 Solutions

If not python3 on linux:

.. code-block::

    module avail python
    module add python/3.8.0


Regardless of OS:

.. code-block::

    python3 -m venv --prompt="aoc" venv
    source venv/bin/activate
    pip install --upgrade pip setuptools
    pip install -r requirements.txt


.. code-block::

    aoc 2 data/day2.txt


.. code-block::

    pytest
