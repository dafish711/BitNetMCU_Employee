from torchvision.datasets import ImageFolder
import os
 
# Mean and std computed from the training set (your supervisor's split).
# To recompute, run mean_std.py against the training_set folder.
EMPLOYEE_MEAN = (0.4360,)
EMPLOYEE_STD  = (0.1487,)
 
NUM_CLASSES = 10
 
 
class EmployeeFacesDataset(ImageFolder):
    # Dataset for the pre-split Employee faces dataset stored on Google Drive.
     def __init__(self, root, train=True, transform=None, download=None):
        split_folder = 'training_set' if train else 'validation_set'
        split_path = os.path.join(root, split_folder)
        super().__init__(root=split_path, transform=transform)