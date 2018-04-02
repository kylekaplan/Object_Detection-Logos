# Object_Detection-Logos

## Setup Environment
* <a href='https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md'>Installation</a><br>
*  \*Working with tensorflow 1.7

	```
	pip install tensorflow --upgrade
	pip install tensorflow-gpu --upgrade
	```

* For cocoapi on windows, edit setup.py as shown <a href='https://github.com/cocodataset/cocoapi/compare/master...willyd:windows?expand=1'>here</a> and run make file manually if you need to.

## Create train.record and eval.record files
* Connor Dowload from <a href='https://drive.google.com/drive/u/1/folders/11HkDmKfCwm-H8lBktsSFNaZXsEc5cNqt'>here</a> and place in ```models\research\object_detection\Logos\data\```<br>

## Download the checkpoint model
* Connor you can also downlaod the checkpoint model folder from the drive. Place in ```models\research\object_detection\Logos\models\model```
The file structure should look like this:
	```
	+models
	  +model
	    -pipeline config file
	    +train
	    +eval
	```
	You will also have some other model files in there.

* (Connor ignore, you did in step above) Dowload your pre-trained checkpoint <a href='https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md'>here</a> we selected faster\_rcnn\_inception\_resnet\_v2\_atrous\_oid and place in models\research\object_etection\Logos\models\model\<br>

## Configure pipeline.config
* Open ```pipeline.config``` edit to put in your path (full path is required).
* Connor wherever you see ```C:\\Users\\Kyle\\Desktop\\college\\Senior_Project\\object_detection-logos\\``` replace with your path

## Run Training and Evaluation
* It seems train and eval are supposed to run at the same time alough I think you can aget way with running one at a time.

* From <a href='https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_locally.md'>tensorflow/models/research/object_detection/g3doc/running_locally.md</a><br>

	### Running the Training Job
	* 
	```
	# From the tensorflow/models/research/ directory
	python object_detection/train.py \
	    --logtostderr \
	    --pipeline_config_path=${PATH_TO_YOUR_PIPELINE_CONFIG} \
	    --train_dir=${PATH_TO_TRAIN_DIR}
	```
		where `${PATH_TO_YOUR_PIPELINE_CONFIG}` points to the pipeline config and `${PATH_TO_TRAIN_DIR}` points to the directory in which training checkpoints and events will be written to. By default, the training job will run indefinitely until the user kills it.

	* Connor your command would be ```$ python object_detection\train.py --logtostderr --pipeline_config_path=object_detection\Logos\models\model\pipeline.config --train_dir=object_detection\Logos\models\model\train\```

	### Running the Evaluation Job

	* Evaluation is run as a separate job. The eval job will periodically poll the train directory for new checkpoints and evaluate them on a test dataset. The job can be run using the following command:

		```
		# From the tensorflow/models/research/ directory
		python object_detection/eval.py \
		    --logtostderr \
		    --pipeline_config_path=${PATH_TO_YOUR_PIPELINE_CONFIG} \
		    --checkpoint_dir=${PATH_TO_TRAIN_DIR} \
		    --eval_dir=${PATH_TO_EVAL_DIR}
		```

		where `${PATH_TO_YOUR_PIPELINE_CONFIG}` points to the pipeline config, `${PATH_TO_TRAIN_DIR}` points to the directory in which training checkpoints were saved (same as the training job) and `${PATH_TO_EVAL_DIR}` points to the directory in which evaluation events will be saved. As with the training job, the eval job run until terminated by default.

	* Connor your command is: ```$ python object_detection\eval.py --logtostderr --pipeline_config_path=object_detection\Logos\models\model\pipeline.config --checkpoint_dir=object_detection\Logos\models\model\train\ --eval_dir=object_detection\Logos\models\model\eval\```

## Running Tensorboard

Progress for training and eval jobs can be inspected using Tensorboard. If
using the recommended directory structure, Tensorboard can be run using the
following command:

```bash
tensorboard --logdir=${PATH_TO_MODEL_DIRECTORY}
```

where `${PATH_TO_MODEL_DIRECTORY}` points to the directory that contains the
train and eval directories. Please note it may take Tensorboard a couple minutes
to populate with data.
