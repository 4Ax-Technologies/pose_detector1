# Person_Pose database

The dataset was built from a subset of the '__person__' class of the COCO 2017 database. One way to download a single class is to download it via the 
FiftyOne website where you can specify any class(es) that you require. This method requires that the data is then unwrapped from the FiftyOne API.

### Relevant classes ('person') from COCO 2017 can be downloaded from [__FiftyOne__](https://docs.voxel51.com/user_guide/dataset_zoo/datasets.html)
  using [__this code__](https://github.com/4Ax-Technologies/pose_detector1/blob/unpickme-patch-1/FiftyOne_download.py) , as three splits.
  
 * __train__
 * __val__
 * __test__

Please note that the test dataset has no annotations. 

If test annotations are required, please consider reserving a holdback subset of the "val" subset to use in the testing phase.

______

### Prototype phase

A bespoke database [0.1] was developed for a quick & dirty prototype. The 11595 image prototype database was downloaded from the [COCO 2017 website](https://cocodataset.org/#home) using 4Ax's [coco_person_data.py](https:github.com/4Ax-Technologies/pose_detector1/coco_person_data.py), unzipped using [7-zip](https://www.7-zip.org/download.html) and was split into three subsets:  __train__ : 8000   -   __val__ : 2595   -   __test__ : 1000. 
During training, using Nvidia's [TAO toolkit](https://developer.nvidia.com/tao-toolkit), selected standard augmentation procedures were used. The prototype achieved beter than 95% accuracy performance, providing seamless transitions 
in the game environment's physics engine. Despite this level of performance the project continued into the development phase with the intention of further refining and improving the model.


______

### Development phase

In this phase the entire COCO trainval dataset was downloaded and all irrelevant classes were then discarded. The 64115 images present in the 'person' class
were split as follows: __train__ : 40000   -   __val__ : 20000   -   __test__ : 4115.


