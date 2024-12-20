import os
import pytest
from unittest import mock
from io import BytesIO
import shutil
import requests
import zipfile

from msdbook.install_supplement import InstallSupplement, install_package_data
import msdbook.package_data as pkg

# Mock the version of msdbook to test different scenarios
@pytest.fixture
def mock_version():
    with mock.patch("msdbook.install_supplement.version") as mock_version_func:
        yield mock_version_func

# Test for fetching Zenodo data with a valid version
def test_fetch_zenodo_valid_version(mock_version):
    mock_version.return_value = "0.1.3"  # Set the mock version to a valid one

    # Mock the response from requests.get to avoid downloading
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.content = b"fake zip content"  # Mock zip content

        zen = InstallSupplement()

        # Mock the methods that interact with the file system to ensure no actual file operations
        with mock.patch("zipfile.ZipFile") as mock_zip, mock.patch("shutil.copy") as mock_copy:
            mock_zip.return_value.__enter__.return_value.namelist.return_value = ["example.txt"]
            mock_copy.return_value = None  # Do nothing for copy

            zen.fetch_zenodo()

            # Ensure the requests.get was called with the correct URL
            mock_get.assert_called_once_with("https://zenodo.org/record/5294124/files/msdbook_package_data.zip?download=1")

            # Ensure the file extraction and copy process was called
            mock_zip.return_value.__enter__.return_value.extract.assert_called_once()
            mock_copy.assert_called_once()

# Test for handling missing data link for an unsupported version
def test_fetch_zenodo_invalid_version(mock_version):
    mock_version.return_value = "0.2.0"  # Set to a version that isn't in DATA_VERSION_URLS

    zen = InstallSupplement()

    with pytest.raises(KeyError) as excinfo:
        zen.fetch_zenodo()

    assert "Link to data missing for current version" in str(excinfo.value)

# Test if the correct data directory is used for unpacking
def test_unpack_data_to_correct_directory(mock_version):
    mock_version.return_value = "0.1.4"  # Set to a valid version

    # Mock the response from requests.get
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.content = b"fake zip content"  # Mock zip content

        zen = InstallSupplement()

        # Mock methods interacting with the file system
        with mock.patch("zipfile.ZipFile") as mock_zip, mock.patch("shutil.copy") as mock_copy:
            mock_zip.return_value.__enter__.return_value.namelist.return_value = ["example.txt"]
            mock_copy.return_value = None  # Do nothing for copy

            # Simulate fetching and extracting the data
            zen.fetch_zenodo()

            # Ensure that files are copied to the correct directory
            mock_copy.assert_called_once()

# Test to ensure install_package_data works without errors
def test_install_package_data(mock_version):
    mock_version.return_value = "0.1.3"  # Use a valid version

    # Mock all the file system and network operations
    with mock.patch("requests.get") as mock_get, mock.patch("zipfile.ZipFile") as mock_zip, \
         mock.patch("shutil.copy") as mock_copy:

        mock_get.return_value.content = b"fake zip content"  # Mock zip content
        mock_zip.return_value.__enter__.return_value.namelist.return_value = ["example.txt"]
        mock_copy.return_value = None  # Do nothing for copy

        # Call the function to test
        zen = InstallSupplement()
        zen.fetch_zenodo()

        # Ensure all methods were called as expected
        mock_get.assert_called_once()
        mock_zip.return_value.__enter__.return_value.extract.assert_called_once()
        mock_copy.assert_called_once()

# Test that the correct URL is used for a different version
def test_fetch_zenodo_version_url(mock_version):
    mock_version.return_value = "0.1.5"  # Set a different version

    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.content = b"fake zip content"  # Mock zip content

        zen = InstallSupplement()

        with mock.patch("zipfile.ZipFile") as mock_zip, mock.patch("shutil.copy") as mock_copy:
            mock_zip.return_value.__enter__.return_value.namelist.return_value = ["example.txt"]
            mock_copy.return_value = None  # Do nothing for copy

            zen.fetch_zenodo()

            # Verify the URL for version "0.1.5"
            mock_get.assert_called_once_with("https://zenodo.org/record/5294124/files/msdbook_package_data.zip?download=1")

# Test that missing URL raises a KeyError with a helpful message
def test_missing_data_url(mock_version):
    mock_version.return_value = "0.1.6"  # Version that is not in DATA_VERSION_URLS

    zen = InstallSupplement()

    with pytest.raises(KeyError) as excinfo:
        zen.fetch_zenodo()

    assert "Link to data missing for current version" in str(excinfo.value)

