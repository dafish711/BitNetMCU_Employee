from torchvision.datasets import ImageFolder
import os
 
# Mean and std computed from the training set (your supervisor's split).
# To recompute, run mean_std.py against the training_set folder.
OLIVETTI_MEAN = (0.5454,)
OLIVETTI_STD  = (0.1722,)
 
NUM_CLASSES = 40
 
 
class OlivettiFacesDataset(ImageFolder):
    # Dataset for the pre-split Olivetti faces dataset stored on Google Drive.
     def __init__(self, root, train=True, transform=None, download=None):
        split_folder = 'training_set' if train else 'validation_set'
        split_path = os.path.join(root, split_folder)
        super().__init__(root=split_path, transform=transform)