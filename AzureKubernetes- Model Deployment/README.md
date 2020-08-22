In this notebook I illustrated how to deploy a trained model that can be used a webservice hosted on Azure Kubernetes Cluster. This enables to to use a trained model for real-time inferencing.


Creating a Workspace that acts as the root object to organize all artifacts and resources used by Azure Machine Learning.
Creating Experiments in your Workspace that capture versions of the trained model along with any desired model performance telemetry. Each time you train a model and evaluate its results, you can capture that run (model and telemetry) within an Experiment.
Creating Compute resources that can be used to scale out model training, so that while your notebook may be running in a lightweight container in Azure Notebooks, your model training can actually occur on a powerful cluster that can provide large amounts of memory, CPU or GPU.
Using Automated Machine Learning (AutoML) to automatically train multiple versions of a model using a mix of different ways to prepare the data and different algorithms and hyperparameters (algorithm settings) in search of the model that performs best according to a performance metric that you specify.
Packaging a Docker Image that contains everything your trained model needs for scoring (prediction) in order to run as a web service.
Deploying your Image to either Azure Kubernetes or Azure Container Instances, effectively hosting the Web Service.
