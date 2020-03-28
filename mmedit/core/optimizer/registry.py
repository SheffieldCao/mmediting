import inspect

import torch
from mmcv.utils import Registry

__all__ = ['OPTIMIZERS']

OPTIMIZERS = Registry('optimizer')


def register_torch_optimizers():
    torch_optimizers = []
    for module_name in dir(torch.optim):
        if module_name.startswith('__') or module_name == 'Optimizer':
            continue
        _optim = getattr(torch.optim, module_name)
        if inspect.isclass(_optim) and issubclass(_optim,
                                                  torch.optim.Optimizer):
            OPTIMIZERS.register_module(_optim)
            torch_optimizers.append(module_name)
    return torch_optimizers


TORCH_OPTIMIZERS = register_torch_optimizers()