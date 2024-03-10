# Person_Pose database

The database was built from a subset of the '__person__' class of the COCO 2017 database. One method for this is to download it via FiftyOne. 

### Relevant classes ('person') from COCO 2017 can be downloaded from [__FiftyOne__](https://docs.voxel51.com/user_guide/dataset_zoo/datasets.html)
  using [__this code__](https://github.com/4Ax-Technologies/pose_detector1/blob/unpickme-patch-1/FiftyOne_download.py) as three splits.
  
 * __train__
 * __val__
 * __test__

Please note that the test dataset has no annotations. 

If test annotations are required, please consider reserving a holdback subset of the "val" subset to use in the testing phase.

______

### Prototype phase

A bespoke database [0.1] was developed for a 'quick & dirty' prototype that achieved 100% performance, providing seamless transitions in the game
enviroment's physics engine. A 10000 image database was split into three:  __train__ : 7500   -   __val__ : 1500   -   __test__ : 1000. During
training, using Nvidia's TAO toolkit, selected standard augmentation procedures were used.
