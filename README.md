#Анализ численности населения по картам

#Запуск

Для сбора данных используется скрипт scrupper.py
Запускается без параметров. 
Сохраняется в папку в текущем каталоге с номером зума карты

Для обучения используется скрипт train.py
Train.py --dataset path_to_dataset --weights path_to_weight --logs path_to_log

Для распознавания объектов запускаем скрипт detection.py
Формат команды:
Detection.py --weights path_to_weight --logs path_to_logs --image path_to_image_dir --output path_to_output_dir

Для проведения анализа с помощью jupyter notebook запускаем processor.ipynb 

#Необходимые зависимости:
* h5py==2.10.0
* httplib2==0.9.2
* ipython==7.8.0
* ipython-genutils==0.2.0
* ipywidgets==7.5.1
* jupyter-client==5.3.4
* jupyter-core==4.6.0
* Keras==2.1.0
* Keras-Applications==1.0.8
* Keras-Preprocessing==1.1.0
* mask-rcnn==2.1
* matplotlib==3.1.1
* numpy==1.17.3
* opencv-python==4.1.1.26
* opencv-python-headless==4.1.1.26
* Pillow==6.2.0
* scikit-image==0.16.1
* scipy==1.3.1
* tensorboard==1.14.0
* tensorflow==1.14.0
* tensorflow-estimator==1.14.0
