import os
from roboflow import Roboflow

rf = Roboflow(api_key=os.environ['ROBOFLOW_API_KEY'])
project = rf.workspace('processing-workspace').project('football-l9zew')
dataset = project.version(6).download('yolov8', location='data/football')
print('Saved to:', dataset.location)