.. msd_uncertainty_ebook documentation master file, created by
   sphinx-quickstart on Wed May 26 22:27:12 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


=======================================================
Addressing Uncertainty in MultiSector Dynamics Research
=======================================================

.. only:: html

    .. epigraph::

        Patrick M. Reed, Antonia Hadjimichael, Keyvan Malek,
        Tina Karimi, Chris R. Vernon, Vivek Srikrishnan, Rohini S. Gupta,
        David F. Gold, Ben Lee, Klaus Keller, Travis B. Thurber, Jennie S. Rice

    A practical guide to sensitivity analysis and diagnostic model evaluation techniques for confronting the computational and conceptual challenges of multi-model, transdisciplinary workflows.

    **Topics in the Book**

    * `Preface <preface.html>`_
    * `Introduction <1_introduction.html>`_
    * `An overview of diagnostic modeling and perspectives on model evaluation <2_diagnostic_modeling_overview_and_perspectives.html>`_
    * `A framework for the basic methods and concepts used in sensitivity analysis <3_sensitivity_analysis_the_basics.html>`_
    * `Technical applications supporting diagnostic model evaluation and exploration <4_sensitivity_analysis_diagnostic_and_exploratory_modeling.html>`_

    **Interactive Tutorials**

    * `Factor Discovery <nb_fishery_dynamics_>`_
    * `Model Calibration <nb_hymod_>`_
    * `Sobol Sensitivity Analysis <nb_saltelli_sobol_>`_
    * `Factor Mapping using Logistic Regression <nb_logistic_regression_>`_
    * `Time-evolving scenario discovery for infrastructure pathways <nb_discovery_>`_
    * `A Hidden-Markov Modeling Approach to Creating Synthetic Streamflow Scenarios <nb_hmm_>`_

    .. tip::

        .. raw:: html

            <p>
                Use the sidebar on the left to quickly navigate the eBook!
                <br/>
                Click or tap the <i style="padding: 0 0.25rem;" class="fas fa-bars"></i> icon to show and hide the sidebar.
            </p>

    .. admonition:: Info

        .. raw:: html

            <p>
                Report a typo or just pass along something you like about the book by <a target="_blank" href="https://github.com/IMMM-SFA/msd_uncertainty_ebook/issues/new?assignees=thurber%2C+crvernon&labels=documentation%2C+triage&template=custom.md&title=Publication+Feedback">opening an issue</a> on GitHub!
                <br/>
                Click or tap the <i style="padding: 0 0.25rem;" class="fab fa-github"></i> icon to find this link again.
            </p>

.. raw:: latex

    \frontmatter
    \sphinxmaketitle

.. toctree::
    :hidden:
    :glob:

    preface
    citation
    acknowledgements
    code_of_conduct
    contributing

.. raw:: latex

    \sphinxtableofcontents

.. raw:: latex

    \mainmatter

.. toctree::
    :hidden:
    :includehidden:
    :numbered: 4
    :maxdepth: 4
    :caption: Contents
    :name: mastertoc
    :glob:

    1_introduction
    2_diagnostic_modeling_overview_and_perspectives
    3_sensitivity_analysis_the_basics
    4_sensitivity_analysis_diagnostic_and_exploratory_modeling
    5_conclusion

.. raw:: latex

    \appendix

.. appendix::
    :hidden:
    :numbered: 4
    :maxdepth: 4
    :caption: Appendices
    :glob:

    A1_Uncertainty_Quantification
    A2_Jupyter_Notebooks
    A3_plotting_code

.. raw:: latex

    \backmatter

.. toctree::
    :hidden:
    :maxdepth: 1
    :caption: Glossary
    :glob:

    6_glossary


.. raw:: latex

    \backmatter

.. toctree::
    :hidden:
    :maxdepth: 1
    :caption: References
    :glob:

    R.Bibliography
