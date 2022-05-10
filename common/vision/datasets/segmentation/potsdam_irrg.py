"""
@author: Junguang Jiang
@contact: JiangJunguang1123@outlook.com
"""
import os
from .segmentation_list import SegmentationList


class PotsdamIRRG(SegmentationList):

    CLASSES = ['Clutter background', 'Impervious surfaces', 'Car', 'Tree', 'Low vegetation', 'Building']


    TRAIN_ID_TO_COLOR = [(255, 255, 0), (255, 255, 255), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), [0, 0, 0]]

    EVALUATE_CLASSES = CLASSES

    def __init__(self, root, split='train', data_folder='images', label_folder='labels', **kwargs):
        assert split in ['all', 'train', 'test']

        data_list_file = os.path.join(root, "image_list", "{}.txt".format(split))
        self.split = split
        super(PotsdamIRRG, self).__init__(root, PotsdamIRRG.CLASSES, data_list_file, data_list_file,
                                         data_folder, label_folder,
                                         train_id_to_color=PotsdamIRRG.TRAIN_ID_TO_COLOR, **kwargs)


