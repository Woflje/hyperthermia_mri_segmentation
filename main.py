from util.load_data import *
import numpy as np
import h5py
import os


if __name__ == '__main__':

    # dcm_subjects_path = "..\\data\\HyperthermiaPatData\\HyperCollar\\dicoms"
    # dcm_segmentation_path = "..\\data\\HyperthermiaPatData\\HyperCollar\\segmentation"
    dcm_segmentation_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                         '..', 'data/HyperthermiaPatData/HyperCollar/segmentation'))
    # dcm_dataset = load_data('dicom', dcm_subjects_path)
    dcm_segmentation = load_data('h5', dcm_segmentation_path)

    tissues = [
        'Air_internal',
        'Lung',
        'Muscle',
        'Fat',
        'Bone',
        'Surrounding',
        'Cerebrum',
        'Cerebellum',
        'Brainstem',
        'Myelum',
        'ScleraRight',
        'LensRight',
        'VitreousHumorRight',
        'OpticalNerveRight',
        'ScleraLeft',
        'LensLeft',
        'VitreousHumorLeft',
        'OpticalNerveLeft',
        'OpticalNerveLeft',
        'CartilageThyroid',
        'CartilageCricoid',
        'Thyroid',
        'MetalImplants',
        'GTV'
    ]

    plt.imshow(dcm_segmentation['0376']['Source'][58])
    plt.show()
    plt.imshow(dcm_segmentation['0376']['Tissue'][58])
    plt.show()
    plt.imshow(dcm_segmentation['0376']['Target'][58])
    plt.show()