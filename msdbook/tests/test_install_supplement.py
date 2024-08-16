import os
import tempfile
import zipfile
import shutil
from unittest.mock import patch, MagicMock
import pytest
import requests
from install_supplement import InstallSupplement, install_package_data

# Helper function to create a mock zip file
def create_mock_zip_file(zip_name, file_contents):
    """Create a mock zip file with specified contents."""
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file_name, content in file_contents.items():
            zipf.writestr(file_name, content)

@pytest.fixture
def mock_version():
    """Fixture for mocking the version of msdbook."""
    with patch('importlib.metadata.version', return_value='0.1.3'):
        yield

@patch('install_supplement.requests.get')
@patch('install_supplement.pkg.get_data_directory')
@patch('install_supplement.shutil.copy')
@patch('install_supplement.zipfile.ZipFile')
@patch('install_supplement.tempfile.TemporaryDirectory')
def test_fetch_zenodo(mock_temp_dir, mock_zipfile, mock_shutil_copy, mock_get_data_directory, mock_requests_get, mock_version):
    """Test the fetch_zenodo method of InstallSupplement."""
    
    # Prepare mock responses
    mock_data_directory = tempfile.mkdtemp()
    mock_get_data_directory.return_value = mock_data_directory
    
    # Create a mock zip file
    mock_zip_content = {
        'file1.txt': 'content1',
        'subdir/file2.txt': 'content2'
    }
    mock_zip_name = 'mock_data.zip'
    create_mock_zip_file(mock_zip_name, mock_zip_content)

    # Mock requests.get to return our mock zip file
    with open(mock_zip_name, 'rb') as f:
        mock_requests_get.return_value = MagicMock(content=f.read())

    # Mock zipfile.ZipFile to use the mock zip file
    def mock_zipfile_init(*args, **kwargs):
        with zipfile.ZipFile(mock_zip_name, 'r') as mock_zip:
            yield mock_zip
    
    mock_zipfile.side_effect = mock_zipfile_init

    # Run the method under test
    installer = InstallSupplement()
    installer.fetch_zenodo()
    
    # Verify files were copied to the expected location
    for file_name in mock_zip_content.keys():
        expected_file_path = os.path.join(mock_data_directory, os.path.basename(file_name))
        assert os.path.exists(expected_file_path)
        with open(expected_file_path, 'r') as f:
            assert f.read() == mock_zip_content[file_name]
    
    # Clean up
    shutil.rmtree(mock_data_directory)
    os.remove(mock_zip_name)

@patch('install_supplement.InstallSupplement.fetch_zenodo')
def test_install_package_data(mock_fetch_zenodo):
    """Test the install_package_data function."""
    install_package_data()
    mock_fetch_zenodo.assert_called_once()

@patch('install_supplement.requests.get')
@patch('install_supplement.pkg.get_data_directory')
def test_fetch_zenodo_key_error(mock_get_data_directory, mock_requests_get, mock_version):
    """Test if KeyError is raised for an unsupported version."""
    mock_get_data_directory.return_value = tempfile.mkdtemp()
    
    # Patch version to an unsupported version
    with patch('importlib.metadata.version', return_value='0.2.0'):
        with pytest.raises(KeyError, match="Link to data missing for current version"):
            installer = InstallSupplement()
            installer.fetch_zenodo()
