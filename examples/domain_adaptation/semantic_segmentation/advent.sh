# GTA5 to Cityscapes
CUDA_VISIBLE_DEVICES=0 python advent.py /home/duraklefkan/Desktop/Academic/MasterThesis/DomainAdaptation/Datasets2/MUCSS_dataset/PotsdamIRRG \
     /home/duraklefkan/Desktop/Academic/MasterThesis/DomainAdaptation/Datasets2/MUCSS_dataset/Vaihingen -s PotsdamIRRG -t Vaihingen \
    --log logs/advent/gtav2cityscapes

# # Synthia to Cityscapes
# CUDA_VISIBLE_DEVICES=0 python advent.py data/synthia data/Cityscapes -s Synthia -t Cityscapes \
#     --log logs/advent/synthia2cityscapes

# # Cityscapes to Foggy
# CUDA_VISIBLE_DEVICES=0 python advent.py data/Cityscapes data/Cityscapes -s Cityscapes -t FoggyCityscapes \
#     --log logs/advent/cityscapes2foggy