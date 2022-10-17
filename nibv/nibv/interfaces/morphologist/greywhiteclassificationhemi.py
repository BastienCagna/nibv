from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class GreyWhiteClassificationHemiInputSpec(CommandLineInputSpec):
    side = traits.Enum(
        "left", "right",
        usedefault=False,
        desc='left,  right',
        position=0, mandatory=False)
    t1mri_nobias = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis, Histo Analysis',
        position=2, mandatory=False, argstr='%s')
    split_brain = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=3, mandatory=False, argstr='%s')
    edges = traits.File(
        exists=True,
        desc='T1 MRI Edges, Aims readable volume formats',
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
        "e", "w", "g",
        usedefault=False,
        desc='',
        position=7, mandatory=False)
    grey_white = traits.File(
        exists=False,
        desc='Morphologist Grey White Mask, Aims writable volume formats',
        position=8, mandatory=False, argstr='%s')
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=9, mandatory=False)


class GreyWhiteClassificationHemiOutputSpec(TraitedSpec):
    grey_white = traits.File(
        desc='Morphologist Grey White Mask, Aims writable volume formats')


class GreyWhiteClassificationHemi(BVCommand):
    input_spec = GreyWhiteClassificationHemiInputSpec
    output_spec = GreyWhiteClassificationHemiOutputSpec
    _cmd = 'GreyWhiteClassificationHemi'

