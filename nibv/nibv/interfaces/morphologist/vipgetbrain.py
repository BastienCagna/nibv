from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class VipGetBrainInputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=1, mandatory=False, argstr='%s')
    mode = traits.Enum(
        "standard+iterative", "standard", "robust+iterative", "robust", "fast",
        usedefault=False,
        desc='standard+iterative, standard, robust+iterative, robust,  fast',
        position=2, mandatory=False)
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=3, mandatory=False, argstr='%s')
    brain_mask = traits.File(
        exists=False,
        desc='T1 Brain Mask, aims Writable Volume Formats',
        position=4, mandatory=False, argstr='%s')
    regularization = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=5, mandatory=False)
    erosion_size = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=6, argstr='%f', mandatory=False)
    layer = traits.Enum(
        "0", "1", "2", "3", "4", "5",
        usedefault=False,
        desc='0, 1, 2, 3, 4,  5',
        position=7, mandatory=False)
    first_slice = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=8, argstr='%d', mandatory=False)
    last_slice = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=9, argstr='%d', mandatory=False)
    lesion_mask = traits.File(
        exists=True,
        desc='Lesion Mask,  aims readable volume Formats',
        position=10, mandatory=False, argstr='%s')


class VipGetBrainOutputSpec(TraitedSpec):
    brain_mask = traits.File(
        desc='T1 Brain Mask, aims Writable Volume Formats')


class VipGetBrain(BVCommand):
    input_spec = VipGetBrainInputSpec
    output_spec = VipGetBrainOutputSpec
    _cmd = 'VipGetBrain'

