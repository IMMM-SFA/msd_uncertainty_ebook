========
Examples
========


Using mathjax
===================

The **first-order sensitivity index** indicates the percent of model output variance contributed by a factor individually (i.e., the effect of varying *x*\ :sub:`i`\ alone) and is obtained using the following (Saltelli, 2002a; Sobol, 2001):

.. math::

  S_i^1 = \frac{V_{x_i} [E_{x\sim_i} (x_i)]}{V(y)}

with *E* and *V* denoting the expected value and the variance, respectively.

Building a codeblock
=======================

.. code-block:: python
  :linenos:

   import ebook

   ebook.plot_experimental_design()

Testing out a note
==================

.. note::
  Keep track of the latest in programming solutions on the `Water Programming <https://waterprogramming.wordpress.com/>`_ blog!


Insert a figure with a caption
==============================

Be sure to add your figure into 'msd_uncertainty_ebook/docs/source/_static'

  .. figure:: _static/im3.png
      :alt: IM3 logo
      :width: 100px
      :align: center

      This is my caption.
