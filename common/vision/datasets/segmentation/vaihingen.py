"""
@author: Junguang Jiang
@contact: JiangJunguang1123@outlook.com
"""
import os
from .segmentation_list import SegmentationList
from .potsdam_irrg import PotsdamIRRG


class Vaihingen(SegmentationList):

    def __init__(self, root, split='train', data_folder='images', label_folder='labels', **kwargs):
        assert split in ['all', 'train', 'test']

        data_list_file = os.path.join(root, "image_list", "{}.txt".format(split))
        self.split = split
        super(Vaihingen, self).__init__(root, PotsdamIRRG.CLASSES, data_list_file, data_list_file,
                                         data_folder, label_folder,
                                         train_id_to_color=PotsdamIRRG.TRAIN_ID_TO_COLOR, **kwargs)


