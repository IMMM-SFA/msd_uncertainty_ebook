FROM jupyter/minimal-notebook:2022-05-03

USER root

RUN git clone https://github.com/IMMM-SFA/msd_uncertainty_ebook.git msd_uncertainty_ebook
RUN cd msd_uncertainty_ebook && pip install .

# Now create a symlinked data folder inside the msdbook package that links to /bucket/data folder
RUN mkdir -p /bucket/data
RUN rm -rf /opt/conda/lib/python3.9/site-packages/msdbook/data
RUN ln -s /bucket/data /opt/conda/lib/python3.9/site-packages/msdbook/data
