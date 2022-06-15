FROM jupyter/minimal-notebook:2022-05-03

USER root

RUN git clone https://github.com/IMMM-SFA/msd_uncertainty_ebook.git msd_uncertainty_ebook
RUN cd msd_uncertainty_ebook && pip install .

