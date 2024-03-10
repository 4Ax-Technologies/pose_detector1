# Architecture/language overview: 

## Pose Estimation Model to Unreal Engine physics


### 1. Pose Estimation Model:  
* Existing deep learning frameworks such as TensorFlow or PyTorch can be used to train and deploy a pose estimation model. These frameworks offer 
  extensive support for neural network architectures and are widely used in the research community.  
* Alternatively, use a pre-trained model from a library such as [__OpenPose__](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md) , which offers an efficient pose estimation solution.
* OpenPose is very good, but it's functionality greatly exceeds what is required and brings with it an undesirable drain on computational overhead
  for this use case.  
* OpenPose was trained on the COCO 2017 dataset. Pose_detector1 uses a resnet18 backbone detectnet_v2 model trained on a relevant subset of COCO 2017.
* pose_detector1 uses a Resnet 18 backbone, which was trained on a sample of the "person" class contained within the 80 class COCO 2017 database
* In evaluation it achieved 95%+ accuracy. 
  
###    2. Interfacing Layer:  
* Python serves as a robust choice for the interfacing layer due to its flexibility, ease of integration with machine learning libraries, 
  and its support within Unreal Engine.  
* Python scripts will be used to process the output from the pose estimation model and extract relevant information such as joint positions, 
  angles, and gestures.
  
###    3. Communication Bridge:  
* Establish a communication bridge between the Python scripts and Unreal Engine, using methods such as inter-process communication (IPC), 
  sockets, or dedicated plugins.  
* Leverage plugins like UnrealCV or Python.NET, which enable communication between Python and Unreal Engine.
  
###    4. Physics Control in Unreal Engine:  
* Unreal Engine's Blueprint visual scripting system or its native C++ API could be used to set up and control physics interactions based 
  on the data received from the pose estimation model.  
* Blueprint scripting offers a high-level visual interface for defining logic and behaviors within Unreal Engine, but for performance-critical 
  tasks or complex logic, it is better to implement custom physics behaviour using C++ to ensure optimal performance and flexibility.
  
###    5. Feedback Loop:  
* A feedback loop should be implemented to continuously update the physics parameters based on the real-time output of the pose estimation model.
* Synchronization between the pose estimation model's output, the physics simulation in Unreal Engine, and the rendering pipeline is necessary 
  to maintain seamless and responsive simulation experiences.  
        
This architecture and language mix should ensure the development of a robust system that seamlessly integrates pose estimation with game engine physics in Unreal Engine, leveraging the strengths of each component to deliver the most immersive and interactive experiences.
