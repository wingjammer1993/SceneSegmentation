import copy
import torchvision.models as models


from .segnet import *
from .enet import *
from .deeplab import *


def get_model(model_dict, n_classes, version=None):
    name = model_dict['arch']
    model = _get_model_instance(name)
    param_dict = copy.deepcopy(model_dict)
    param_dict.pop('arch')

    if name == "segnet":
        model = model(n_classes=n_classes, **param_dict)
        vgg16 = models.vgg16(pretrained=True)
        model.init_vgg16_params(vgg16)

    elif name == "enet":
        model = model(num_classes=n_classes, **param_dict)

    elif name == "deeplab":
        model = Res_Deeplab(num_classes=n_classes, **param_dict)

    else:
        pass
    return model


def _get_model_instance(name):
    try:
        return {
            "segnet": segnet,
            "enet": ENet,
            "deeplab": None,
        }[name]
    except:
        raise("Model {} not available".format(name))
