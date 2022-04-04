import os
import sys
from tqdm import tqdm
import pydicom as dcm
import matplotlib.pyplot as plt
import h5py
import numpy as np
from util.logging import tlog


def load_dicom_slice(dcm_file):
    return dcm.dcmread(dcm_file)


def view_dicom_slice(dcm_data):
    plt.imshow(dcm_data.pixel_array)
    plt.show()


def dict_dicom(dcm_data: dcm.Dataset):
    dcm_dict = {}
    for data_element in dcm_data:
        desc = data_element.name
        if desc != 'Pixel Data':
            dcm_dict[desc] = data_element.value
    return dcm_dict


def load_dicom_subject(dcm_subject_folder):
    content = os.listdir(dcm_subject_folder)
    first = True
    ct_slices = []
    subject_dict = {}
    for file in content:
        exts = file.rsplit('.', 1)
        if len(exts) > 1:
            ext = exts[1]
            if ext == 'dcm':
                dcm_data = dcm.dcmread(f"{dcm_subject_folder}/{file}")
                ct_slices.append(dcm_data.pixel_array)
                if first:
                    subject_dict = dict_dicom(dcm_data)
                    first = False
    subject_dict['ct_slices'] = ct_slices
    return subject_dict


def load_dicom_subjects(dcm_subjects_folder):
    folders = os.listdir(dcm_subjects_folder)
    dcm_subjects = {}
    for i in tqdm(range(0,len(folders)), desc='Loading Dicom Subjects'):
        folder = folders[i]
        subject_path = f"{dcm_subjects_folder}/{folder}"
        if os.path.isdir(subject_path):
            dcm_subjects[folder] = load_dicom_subject(subject_path)
    return dcm_subjects


def load_h5(data_folder):
    subjects_h5 = {}
    content = os.listdir(data_folder)
    for i in tqdm(range(0, len(content)), desc='Loading H5 Data'):
        file = content[i]
        exts = file.rsplit('.',1)
        if len(exts) > 1:
            ext = exts[1]
            if ext == 'h5':
                s_number = file.split('_', 1)[0]
                size = [512, 512]
                pixels = size[0]*size[1]
                with h5py.File(f"{data_folder}/{file}") as f:
                    n_slices = int(len(f['Source'])/pixels)
                    h5_data = {
                        'Source': array_to_slices(f['Source'], n_slices, size),
                        'Target': array_to_slices(f['Target'], n_slices, size),
                        'Tissue': array_to_slices(f['Tissue'], n_slices, size)
                    }
                subjects_h5[s_number] = h5_data
    return subjects_h5


def array_to_slices(arr, n_slices, size):
    slices = np.reshape(arr, (n_slices, size[0], size[1]))
    return slices


def load_data(data_type, data_folder):
    if data_type == 'dicom':
        return load_dicom_subjects(data_folder)
    elif data_type == 'h5':
        return load_h5(data_folder)
    else:
        tlog('Error', f'"{data_type}" is not a supported data type!')
        sys.exit()