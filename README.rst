==================
pymt_heatpynetlogo
==================


.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. image:: https://img.shields.io/badge/recipe-pymt_heatpynetlogo-green.svg
        :target: https://anaconda.org/conda-forge/pymt_heatpynetlogo

.. image:: https://readthedocs.org/projects/pymt-pynetlogo/badge/?version=latest
        :target: https://pymt-pynetlogo.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://github.com/mdpiper/pymt_heatpynetlogo/actions/workflows/test.yml/badge.svg
        :target: https://github.com/mdpiper/pymt_heatpynetlogo/actions/workflows/test.yml

.. image:: https://github.com/mdpiper/pymt_heatpynetlogo/actions/workflows/lint.yml/badge.svg
        :target: https://github.com/mdpiper/pymt_heatpynetlogo/actions/workflows/lint.yml

.. image:: https://github.com/mdpiper/pymt_heatpynetlogo/actions/workflows/format.yml/badge.svg
        :target: https://github.com/mdpiper/pymt_heatpynetlogo/actions/workflows/format.yml


PyMT plugin for bmi-example-pynetlogo


* Free software: MIT License
* Documentation: https://pymt-heatpynetlogo.readthedocs.io.




============= =====================================
Component     PyMT
============= =====================================
HeatDiffusion from pymt.models import HeatDiffusion
============= =====================================

---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

-----------------------------
Installing pymt_heatpynetlogo
-----------------------------



To install `pymt_heatpynetlogo`,

.. code::

  conda install pymt_heatpynetlogo
