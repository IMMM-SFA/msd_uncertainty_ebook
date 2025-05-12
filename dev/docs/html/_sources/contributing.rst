******************
Contribution Guide
******************

Our eBook is a living product that we hope continues to grow over time to stay relevant with methodological and technological advancements in the field of uncertainty quantification and MultiSector Dynamics at large. We extend an invitation to you, the reader, to contribute to our interactive Jupyter notebook tutorials. If you feel you have a contribution that would be relevant and generalizable to the MSD community, please submit a proposal idea `here <https://github.com/IMMM-SFA/msd_uncertainty_ebook/issues/new?assignees=thurber%2C+crvernon&labels=triage&projects=&template=contribution_proposal.yml&title=Contribution+Proposal>`_. Your proposal will be reviewed by our team, and feedback and/or a decision will be provided shortly. Any accepted contribution will receive it's own DOI and citation so that you may provide an independent reference to your work as you see fit.

Please consider the following requirements for contribution:

- All elements of your contribution MUST be fully open-source and can be distributed with an `Open Source Initiative approved license <https://opensource.org/licenses/>`_ with an understanding that they may be used in community demonstrations and other activities. Author citations will be present in the notebook for any contributed work to ensure the author(s) receive full credit for their contribution.
- Any data or code reused in your submission must be correctly cited giving credit to the original authors.
- The notebook provided must be written in English and able to be a stand-alone product that needs no further explanation past what is written in the notebook to make use of it.
- The provided work is not merely a regurgitation of an existing tutorial or demonstration but represents a novel contribution.
- All contributions and communication thereof must abide by our `code of conduct <https://uc-ebook.org/docs/html/code_of_conduct.html>`_.


If you feel your work meets the criteria above, please submit a proposal issue `here <https://github.com/IMMM-SFA/msd_uncertainty_ebook/issues/new?assignees=thurber%2C+crvernon%2C+erexer&labels=triage&projects=&template=contribution_proposal.yml&title=Contribution+Proposal>`_. If your proposal is approved, please create a pull request with the submission `template <https://github.com/IMMM-SFA/msd_uncertainty_ebook/blob/main/.github/PULL_REQUEST_TEMPLATE/contribution_checklist.md>`_ copied into the pull request description and filled out. We will then review your pull request and provide feedback. Once your contribution has been deemed ready to deploy, we will generate a DOI for your work, launch it to our MSD-LIVE set of interactive notebooks, and feature the contribution in the index of our eBook.

Please feel free to reach out with any further questions.


Development workflow
____________________

The following is the recommended workflow for contributing:

1. `Fork the msd_uncertainty_ebook repository <https://github.com/IMMM-SFA/msd_uncertainty_ebook/fork>`_ and then clone it locally:

  .. code-block:: bash

    git clone https://github.com/<your-user-name>/msd_uncertainty_ebook


2. Set up the repository for development:

  Make sure that you are using an **msd_uncertainty_ebook** `compatible python version <https://github.com/IMMM-SFA/msd_uncertainty_ebook/blob/dev/pyproject.toml#L10>`_. It is important to install the package in development mode. This will give you the flexibility to make changes in the code without having to rebuild the package:

  .. code-block:: bash

      cd msd_uncertainty_ebook

      pip install -e ".[dev]"


  `Install \`pre-commit\` <https://pre-commit.com/>`_, a code format checker, in the repo:

  .. code-block:: bash

      pre-commit install


3. Add your changes and commit them:

  .. code-block:: bash

    git add <my-file-name>

    git commit -m "<my short message>"


4. Ensure all tests pass:

  Ensure your tests pass locally before pushing to your remote branch where GitHub actions will launch CI services to build the package, run the test suite, and evaluate code coverage. To do this, ensure that ``pytest`` is installed then navigate to the root of your cloned directory (e.g., <my-path>/msd_uncertainty_ebook) and run ``pytest`` in the terminal.

  .. code-block:: bash

      pip install -e ".[dev]"

      pytest


5. Update the Documentation:

  Changes to the documentation can be made in the ``msd_uncertainty_ebook/docs/source`` directory containing the RST files. To view your changes, ensure you have the documentation dependencies of **msd_uncertainty_ebook** installed and run the following from the ``msd_uncertainty_ebook/docs/source`` directory:

  .. code-block:: bash

      pip install -e ".[docs]"

      make html


  This will generate your new documentation in a directory named ``msd_uncertainty_ebook/docs/build/html``. You can open the ``index.html`` in your browser to view the documentation site locally. If your changes are merged into the main branch of **msd_uncertainty_ebook**, changes in your documentation will go live on the `uc-ebook.org documentation <https://uc-ebook.org/docs/html/index.html>`_. If your changes are merged into the dev branch of **msd_uncertainty_ebook**, changes in your documentation will go live on the `dev site <https://uc-ebook.org/dev/docs/html/index.html>`_.

6. Push your changes to the remote

  .. code-block:: bash

    git push origin <my-branch-name>


7. Submit a pull request with the submission `template <https://github.com/IMMM-SFA/msd_uncertainty_ebook/blob/main/.github/PULL_REQUEST_TEMPLATE/contribution_checklist.md>`_ copied into the pull request description and filled out.

8. If approved, your pull request will be merged first into the dev, and then into the main branch by a **msd_uncertainty_ebook** admin and a release will be conducted subsequently. **msd_uncertainty_ebook** uses `semantic naming <https://semver.org/>`_ for versioned releases. Each release receives a DOI via a linked Zenodo service automatically.


Miscellaneous Developer Notes
_____________________________

- `Dockerfile for the uc-ebook site <https://github.com/MSD-LIVE/jupyter-notebook-uc-ebook>`_.
-  `Dockerfile for the uc-ebook dev site <https://github.com/MSD-LIVE/jupyter-notebook-uc-ebook-dev>`_.
