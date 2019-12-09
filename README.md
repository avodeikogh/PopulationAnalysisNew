Анализ численности населения по картам

Запуск

Для сбора данных используется скрипт scrupper.py
Запускается без параметров. 
Сохраняется в папку в текущем каталоге с номером зума карты

Для обучения используется скрипт train.py
Train.py --dataset path_to_dataset --weights path_to_weight --logs path_to_log

Для распознавания объектов запускаем скрипт detection.py
Формат команды:
Detection.py --weights path_to_weight --logs path_to_logs --image path_to_image_dir --output path_to_output_dir

Для проведения анализа с помощью jupyter notebook запускаем processor.ipynb 

Необходимые зависимости:
absl-py==0.8.1
alabaster==0.7.12
asn1crypto==0.24.0
astor==0.8.0
attrs==19.3.0
Automat==0.6.0
Babel==2.7.0
backcall==0.1.0
bleach==3.1.0
blinker==1.4
certifi==2019.9.11
chardet==3.0.4
click==6.7
cloud-init==18.5
colorama==0.3.7
command-not-found==0.3
configobj==5.0.6
constantly==15.1.0
cryptography==2.1.4
cycler==0.10.0
Cython==0.29.13
decorator==4.4.0
defusedxml==0.6.0
distro-info===0.18ubuntu0.18.04.1
docutils==0.15.2
entrypoints==0.3
gast==0.3.2
google-pasta==0.1.7
grpcio==1.24.1
h5py==2.10.0
html5lib==0.999999999
httplib2==0.9.2
hyperlink==17.3.1
idna==2.8
imageio==2.6.1
imagesize==1.1.0
imgaug==0.3.0
importlib-metadata==0.23
incremental==16.10.1
ipykernel==5.1.2
ipyparallel==6.2.4
ipython==7.8.0
ipython-genutils==0.2.0
ipywidgets==7.5.1
jedi==0.15.1
Jinja2==2.10.3
jsonpatch==1.16
jsonpointer==1.10
jsonschema==3.1.1
jupyter-client==5.3.4
jupyter-core==4.6.0
Keras==2.1.0
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.0
keyring==10.6.0
keyrings.alt==3.0
kiwisolver==1.1.0
language-selector==0.1
Markdown==3.1.1
MarkupSafe==1.1.1
mask-rcnn==2.1
matplotlib==3.1.1
mistune==0.8.4
more-itertools==7.2.0
nbconvert==5.6.0
nbformat==4.4.0
netifaces==0.10.4
networkx==2.4
nose==1.3.7
notebook==6.0.1
numpy==1.17.3
oauthlib==2.0.6
opencv-python==4.1.1.26
opencv-python-headless==4.1.1.26
packaging==19.2
PAM==0.4.2
pandocfilters==1.4.2
parso==0.5.1
pexpect==4.7.0
pickleshare==0.7.5
Pillow==6.2.0
prometheus-client==0.7.1
prompt-toolkit==2.0.10
protobuf==3.10.0
ptyprocess==0.6.0
pyasn1==0.4.2
pyasn1-modules==0.2.1
pycrypto==2.6.1
pyGeoTile==1.0.6
Pygments==2.4.2
pygobject==3.26.1
PyJWT==1.5.3
pyOpenSSL==17.5.0
pyparsing==2.4.2
pyrsistent==0.15.4
pyserial==3.4
python-apt==1.6.4
python-dateutil==2.8.0
python-debian==0.1.32
pytz==2019.3
PyWavelets==1.1.1
pyxdg==0.25
PyYAML==5.1.2
pyzmq==18.1.0
qtconsole==4.5.5
requests==2.22.0
requests-unixsocket==0.1.5
scikit-image==0.16.1
scipy==1.3.1
SecretStorage==2.3.1
Send2Trash==1.5.0
service-identity==16.0.0
Shapely==1.6.4.post2
simplegeneric==0.8.1
six==1.12.0
snowballstemmer==2.0.0
Sphinx==2.2.0
sphinxcontrib-applehelp==1.0.1
sphinxcontrib-devhelp==1.0.1
sphinxcontrib-htmlhelp==1.0.2
sphinxcontrib-jsmath==1.0.1
sphinxcontrib-qthelp==1.0.2
sphinxcontrib-serializinghtml==1.1.3
ssh-import-id==5.7
systemd-python==234
tensorboard==1.14.0
tensorflow==1.14.0
tensorflow-estimator==1.14.0
termcolor==1.1.0
terminado==0.8.2
testpath==0.4.2
tornado==6.0.3
traitlets==4.3.3
Twisted==17.9.0
ufw==0.36
unattended-upgrades==0.1
urllib3==1.25.6
wcwidth==0.1.7
webencodings==0.5.1
Werkzeug==0.16.0
widgetsnbextension==3.5.1
wrapt==1.11.2
zipp==0.6.0
zope.interface==4.3.2
