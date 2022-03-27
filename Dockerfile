FROM python:3.9-slim

WORKDIR /tmp

# Install git
RUN apt update && apt install git -y

# App requirements
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Dev requirements
COPY requirements-dev.txt requirements-dev.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

# Dev user and workspace parameters
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG WORKSPACE=/project

# Create dev user
RUN addgroup --gid $USER_GID $USERNAME && \
    adduser --uid $USER_UID --gid $USER_GID --gecos '' --disabled-password --home /home/$USERNAME $USERNAME

# Workspace
RUN mkdir ${WORKSPACE} && chown -R ${USER_UID}:${USER_GID} ${WORKSPACE}
WORKDIR ${WORKSPACE}

EXPOSE 5000