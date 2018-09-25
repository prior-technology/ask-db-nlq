FROM nvidia/cuda:9.2-runtime-centos7

#inspired by https://github.com/conda/conda-docker/blob/master/miniconda3/centos7/Dockerfile
RUN yum -y update \
    && yum -y install curl bzip2 \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local/ \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3 \
    && conda update conda \
    && conda clean --all --yes \
    && rpm -e --nodeps curl bzip2 \
    && yum clean all

ENV LANG en_IE.utf8

COPY environment.yml ./
RUN conda env create -f environment.yml

