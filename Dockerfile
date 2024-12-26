FROM ghcr.io/msd-live/jupyter/python-notebook:latest

USER root

RUN git clone --depth=1 --branch=main https://github.com/IMMM-SFA/msd_uncertainty_ebook.git msd_uncertainty_ebook
RUN cd msd_uncertainty_ebook && pip install .

# Install msdbook data
RUN mkdir -p /opt/conda/lib/python3.11/site-packages/msdbook/data
RUN python -c 'from msdbook.install_supplement import install_package_data; install_package_data()'
