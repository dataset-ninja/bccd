# Path to the original dataset

import os

import gdown
import numpy as np
import supervisely as sly
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)

import src.settings as s

dataset_path = "./APP_DATA/BCCD"
# items_folder = "data"
batch_size = 30
images_ext = ".jpg"
anns_ext = ".txt"


def create_ann(image_path, ds_name, cls_to_obj_classes):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_width = image_np.shape[1]

    bbox_path = os.path.join(dataset_path, "anns", get_file_name(image_path) + anns_ext)

    if file_exists(bbox_path):
        with open(bbox_path) as f:
            content = f.read().split("\n")

            for curr_data in content:
                if len(curr_data) != 0:
                    line = curr_data.split(" ")
                    if len(line) != 5:
                        line[0] = line[0] + " " + line.pop(1)
                        if len(line) != 5:
                            line[0] = line[0] + " " + line.pop(1)
                    obj_class = cls_to_obj_classes[line.pop(0)]

                    curr_data = list(map(float, line))

                    top = curr_data[2]
                    left = curr_data[0]
                    right = curr_data[1]
                    bottom = curr_data[3]

                    rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                    label = sly.Label(rectangle, obj_class)
                    labels.append(label)

    return sly.Annotation(img_size=(img_height, img_width), labels=labels)


def get_img_basenames(folder_path):
    img_basenames = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(images_ext):
                img_basenames.append(os.path.basename(file).split(".")[0])
    return img_basenames


class_names = ["RBC", "WBC", "Platelets"]


obj_classes = []
cls_to_obj_classes = {}
for cls in class_names:
    obj_classes.append(sly.ObjClass(cls, sly.Rectangle))
    cls_to_obj_classes[cls] = sly.ObjClass(cls, sly.Rectangle)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_classes)
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in ["train", "val", "test"]:
        with open(os.path.join(dataset_path, f"ImageSets/Main/{ds_name}.txt"), "r") as file:
            lines = [line.rstrip() for line in file]

        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        # curr_path = os.path.join(dataset_path, ds_name)
        images_paths = [
            f
            for f in sly.fs.list_files(os.path.join(dataset_path, "img"))
            if sly.fs.get_file_name(f) in lines
        ]

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_paths))

        for img_pathes_batch in sly.batched(images_paths, batch_size=batch_size):
            img_names_batch = [get_file_name(f) for f in img_pathes_batch]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [
                create_ann(image_path, ds_name, cls_to_obj_classes)
                for image_path in img_pathes_batch
            ]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_pathes_batch))

    return project
