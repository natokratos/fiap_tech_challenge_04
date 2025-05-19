FROM python:3.13.0

RUN mkdir /app && \
        chmod 777 /app && \
        apt-get update && \
        apt-get -y upgrade

#RUN apt-get install sudo 
RUN install -d -m 0755 /etc/apt/keyrings
RUN apt-get -y install wget sudo which
RUN wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
RUN gpg -n -q --import --import-options import-show /etc/apt/keyrings/packages.mozilla.org.asc | awk '/pub/{getline; gsub(/^ +| +$/,""); if($0 == "35BAA0B33E9EB396F59CA838C0BA5CE6DC6315A3") print "\nThe key fingerprint matches ("$0").\n"; else print "\nVerification failed: the fingerprint ("$0") does not match the expected one.\n"}'
RUN echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] \
            https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
RUN echo 'Package: * \
            Pin: origin packages.mozilla.org \
            Pin-Priority: 1000 \
            ' | tee /etc/apt/preferences.d/mozilla
#RUN apt-get -y install firefox \
RUN apt-get -y install gnome-browser-connector \
        libffi-dev \
        software-properties-common

# RUN add-apt-repository ppa:deadsnakes/ppa && \
#     apt-get update && \
#     apt-get -y install python3.13 && \
#     wget -q https://bootstrap.pypa.io/get-pip.py && \
#     python3.13 get-pip.py


# Configure Poetry
ENV POETRY_VERSION=2.1.3
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

#RUN apt-get install ldconfig
# RUN curl -fsSL https://pyenv.run | bash && \
#         echo 'export PYENV_ROOT="\$HOME/.pyenv"' >> ~/.bashrc && \
#         echo '[[ -d \$PYENV_ROOT/bin ]] && export PATH="\$PYENV_ROOT/bin:\$PATH"' >> ~/.bashrc && \
#         echo 'eval "\$(pyenv init - bash)"' >> ~/.bashrc && \
#         echo 'export PYENV_ROOT="\$HOME/.pyenv"' >> ~/.profile && \
#         echo '[[ -d \$PYENV_ROOT/bin ]] && export PATH="\$PYENV_ROOT/bin:\$PATH"' >> ~/.profile && \
#         echo 'eval "\$(pyenv init - bash)"' >> ~/.profile

# RUN echo "$PYENV_ROOT/bin"
# RUN cd /app && \
#         pyenv install 3.13.0 && \
#         pyenv virtualenv 3.13.0 venv_3.13.0 && \
#         pyenv global 3.13.0 && \
#RUN pip install --upgrade pip && \
# RUN python3.13 -m pip install selenium \
#         bs4 \
#         requests \
#         lxml \
#         boto3 \
#         awscli \
#         fastparquet \
#     chmod -Rf 777 /app

WORKDIR /app

# Install dependencies
# COPY poetry.lock pyproject.toml ./
#RUN cd /app && poetry install

# Run your app
#COPY . /app
#CMD [ "poetry", "run", "python", "-c", "print('Hello, World!')" ]

        # pip3 install bs4 && \
        # pip3 install requests && \
        # pip3 install lxml && \
        # pip3 install boto3 && \
        # pip3 install awscli && \
        # pip3 install fastparquet
CMD [ "/bin/bash" ]