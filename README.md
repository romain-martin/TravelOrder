# TravelOrder
T-AIA-901

------------------------------------
Prérequis:
------------------------------------

pip3 install scikit-build

sudo apt install libportaudio

sudo apt install libffi-dev

pip install setuptools==60

pip install Cython

------------------------------------
Virtualenv
------------------------------------

# Install:

$  pip3 install virtualenv

# Create:

$  python3 -m venv <venv-name>

# Activate:

$  source <venv-name>/bin/activate

# Quit:

$  deactivate

# Requirements

$ pip3 install -r requirements.txt

------------------------------------
Installation SpeechToText:
------------------------------------

$ pip3 install SpeechRecognition pydub

------------------------------------
Insallation pyAudio (Microphone)
------------------------------------

Windows
------------------------------------
You can just pip install it:

$ pip3 install pyaudio

Linux
------------------------------------
You need to first install the dependencies:

$ sudo apt-get install python-pyaudio python3-pyaudio
sudo apt install portaudio19-dev

$ pip3 install portaudio pyAudio

MacOS
------------------------------------
You need to first install portaudio, then you can just pip install it:

$ brew install portaudio
$ pip3 install pyaudio

------------------------------------
PocketSphinx (model fr)
------------------------------------

pip install pocketsphinx

https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst