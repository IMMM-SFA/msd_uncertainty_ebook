.. msd_uncertainty_ebook documentation master file, created by
   sphinx-quickstart on Wed May 26 22:27:12 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


=======================================================
Addressing Uncertainty in MultiSector Dynamics Research
=======================================================

Testing out mathjax
===================

The **first-order sensitivity index** indicates the percent of model output variance contributed by a factor individually (i.e., the effect of varying *x*\ :sub:`i`\ alone) and is obtained using the following (Saltelli, 2002a; Sobol, 2001):

.. math::

  S_i^1 = \frac{V_{x_i} [E_{x\sim_i} (x_i)]}{V(y)}

with *E* and *V* denoting the expected value and the variance, respectively.

Testing out a codeblock
=======================

.. code-block:: python
  :linenos:

   import ebook

   ebook.plot_experimental_design()

Testing out a note
==================

.. note::
  Keep track of the latest in programming solutions on the `Water Programming <https://waterprogramming.wordpress.com/>`_ blog!



Chapters
========

.. toctree::
  :maxdepth: 2

  1.0_Introduction



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
