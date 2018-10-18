import os
import sys
import yaml
import torch
import visdom
import argparse
import timeit
import numpy as np
import scipy.misc as misc
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models

from torch.backends import cudnn
from torch.utils import data

from tqdm import tqdm

from ptsemseg.models import get_model
from ptsemseg.loader import get_loader, get_data_path
from ptsemseg.metrics import runningScore
from ptsemseg.utils import convert_state_dict
from ptsemseg.augmentations import get_composed_augmentations
torch.backends.cudnn.benchmark = True
import visdom

vis = visdom.Visdom()


def validate(cfg, args):

    augmentations = {'hue': args.hue, 'contrast': args.contrast, 'brightness': args.brightness,
                     'saturation': args.saturation, 'gamma': args.gamma}
    data_aug = get_composed_augmentations(augmentations)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    data_loader = get_loader(cfg['data']['dataset'])
    data_path = cfg['data']['path']

    loader = data_loader(data_path, split=cfg['data']['val_split'], is_transform=True,
                         img_size=(cfg['data']['img_rows'], cfg['data']['img_rows']),
                         augmentations=data_aug)

    n_classes = loader.n_classes
    valloader = data.DataLoader(loader, batch_size=cfg['training']['batch_size'], num_workers=8)
    running_metrics = runningScore(n_classes)

    model = get_model(cfg['model'], n_classes).to(device)
    model = torch.nn.DataParallel(model, device_ids=range(torch.cuda.device_count()))
    checkpoint = torch.load(cfg['training']['resume'], map_location=lambda storage, loc: storage)
    model.load_state_dict(checkpoint["model_state"])
    model.eval()
    model.to(device)

    for i, (images, labels) in enumerate(valloader):
        vis.images(images)
        images = images.to(device)
        outputs = model(images)
        pred = outputs.data.max(1)[1].cpu().numpy()
        gt = labels.numpy()
        decoded_crf = loader.decode_segmap(np.array(pred.squeeze(0), dtype=np.uint8))
        vis.image(decoded_crf.transpose([2, 0, 1]))
        fg = loader.decode_segmap(np.array(gt.squeeze(0), dtype=np.uint8))
        vis.image(fg.transpose([2, 0, 1]))
        running_metrics.update(gt, pred)


    score, class_iou = running_metrics.get_scores()

    for k, v in score.items():
        print(k, v)

    for i in range(n_classes):
        if loader.class_names is not None:
            print(loader.class_names[i+1], class_iou[i])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hyperparams")
    parser.add_argument(
        "--config",
        nargs="?",
        type=str,
        default="configs/enet_cityscapes.yml",
        help="Config file to be used",
    )

    parser.add_argument(
        "--hue",
        nargs="?",
        type=float,
        default=0
    )

    parser.add_argument(
        "--saturation",
        nargs="?",
        type=float,
        default=1
    )

    parser.add_argument(
        "--gamma",
        nargs="?",
        type=float,
        default=1
    )

    parser.add_argument(
        "--brightness",
        nargs="?",
        type=float,
        default=1
    )

    parser.add_argument(
        "--contrast",
        nargs="?",
        type=float,
        default=1
    )

    args = parser.parse_args()

    with open(args.config) as fp:
        cfg = yaml.load(fp)

    validate(cfg, args)
