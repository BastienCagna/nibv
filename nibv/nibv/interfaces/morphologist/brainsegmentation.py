from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class BrainSegmentationInputSpec(CommandLineInputSpec):
    t1mri_nobias = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis, Histo Analysis',
        position=1, mandatory=False, argstr='%s')
    variance = traits.File(
        exists=True,
        desc='T1 MRI Variance, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    edges = traits.File(
        exists=True,
        desc='T1 MRI Edges, Aims readable volume formats',
        position=3, mandatory=False, argstr='%s')
    white_ridges = traits.File(
        exists=True,
        desc='T1 MRI White Matter Ridges, Aims readable volume formats',
        position=4, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=5, mandatory=False, argstr='%s')
    lesion_mask = traits.File(
        exists=True,
        desc='Lesion Mask, Aims readable volume formats',
        position=6, mandatory=False, argstr='%s')
    lesion_mask_mode = traits.Enum(
        "e", "i",
        usedefault=False,
        desc='',
        position=7, mandatory=False)
    variant = traits.Enum(
        "2010", "2005 based on white ridge", "Standard +", "Standard +", "Standard +", "ithout regularisation", "Robust +", "Robust +", "Robust +", "ithout regularisation", "Fast",
        usedefault=False,
        desc='2010, 2005 based on white ridge, Standard +, Standard +, Standard +, ithout regularisation, Robust +, Robust +, Robust +, ithout regularisation, Fast',
        position=8, mandatory=False)
    visu = traits.Enum(
        "No", "Yes",
        usedefault=False,
        desc='No,  Yes',
        position=10, mandatory=False)
    layer = traits.Enum(
        "0", "1", "2", "3", "4", "5",
        usedefault=False,
        desc='0, 1, 2, 3, 4,  5',
        position=11, mandatory=False)
    first_slice = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=12, argstr='%d', mandatory=False)
    last_slice = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=13, argstr='%d', mandatory=False)
    brain_mask = traits.File(
        exists=False,
        desc='T1 Brain Mask, Aims writable volume formats',
        position=14, mandatory=False, argstr='%s')
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=15, mandatory=False)


class BrainSegmentationOutputSpec(TraitedSpec):
    brain_mask = traits.File(
        desc='T1 Brain Mask, Aims writable volume formats')


class BrainSegmentation(BVCommand):
    input_spec = BrainSegmentationInputSpec
    output_spec = BrainSegmentationOutputSpec
    _cmd = 'BrainSegmentation'

