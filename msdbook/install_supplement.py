import os
import tempfile
import zipfile
import shutil

import requests

from importlib.metadata import version
from io import BytesIO as BytesIO

import msdbook.package_data as pkg


class InstallSupplement:
    """Download and unpack example data supplement from Zenodo that matches the current installed
    msdbook distribution.

    """

    # URL for DOI minted example data hosted on Zenodo
    DATA_VERSION_URLS = {
        "*": "https://zenodo.org/record/5294124/files/msdbook_package_data.zip?download=1",
    }

    def fetch_zenodo(self):
        """Download and unpack the Zenodo example data supplement for the
        current msdbook distribution."""

        # full path to the msdbook root directory where the example dir will be stored
        data_directory = pkg.get_data_directory()

        # get the current version of msdbook that is installed
        current_version = version("msdbook")

        try:
            data_link = InstallSupplement.DATA_VERSION_URLS[current_version]

        except KeyError:
            data_link = InstallSupplement.DATA_VERSION_URLS["*"]

        # retrieve content from URL
        print("Downloading example data for msdbook version {}...".format(current_version))
        r = requests.get(data_link)

        with zipfile.ZipFile(BytesIO(r.content)) as zipped:

            # extract each file in the zipped dir to the project
            for f in zipped.namelist():

                extension = os.path.splitext(f)[-1]

                if len(extension) > 0:

                    basename = os.path.basename(f)
                    out_file = os.path.join(data_directory, basename)

                    # extract to a temporary directory to be able to only keep the file out of the dir structure
                    with tempfile.TemporaryDirectory() as tdir:

                        # extract file to temporary directory
                        zipped.extract(f, tdir)

                        # construct temporary file full path with name
                        tfile = os.path.join(tdir, f)

                        print(f"Unzipped: {out_file}")
                        # transfer only the file sans the parent directory to the data package
                        shutil.copy(tfile, out_file)


def install_package_data():
    """Download and unpack example data supplement from Zenodo that matches the current installed
    msdbook distribution.

    """

    zen = InstallSupplement()

    zen.fetch_zenodo()
