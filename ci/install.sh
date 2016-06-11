#!/bin/bash
set -e -x
if [[ "$TRAVIS_OS_NAME" == "linux" ]]; then
    sudo pip install pip --upgrade
    sudo pip install --install-option="--no-cython-compile" cython
    sudo pip install numpy
    sudo pip install python-coveralls
    sudo pip install nosexcover
    sudo pip install -e $HOME/build/urschrei/convertbng -v
fi

if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
    source $HOME/build/urschrei/convertbng/venv/bin/activate
    pip install pip --upgrade
    pip install --install-option="--no-cython-compile" cython
    pip install numpy
    pip install python-coveralls
    pip install nosexcover
    pip install -e $HOME/build/urschrei/convertbng -v
fi
