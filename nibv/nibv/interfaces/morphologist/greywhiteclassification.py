from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class GreyWhiteClassificationInputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=1, mandatory=False, argstr='%s')
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    edges = traits.File(
        exists=True,
        desc='T1 MRI Edges, Aims readable volume formats',
        position=3, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=4, mandatory=False, argstr='%s')
    side = traits.Enum(
        "Both", "Left", "Right",
        usedefault=False,
        desc='Both, Left,  Right',
        position=5, mandatory=False)
    left_grey_white = traits.File(
        exists=False,
        desc='Left Grey White Mask, Aims writable volume formats',
        position=6, mandatory=False, argstr='%s')
    right_grey_white = traits.File(
        exists=False,
        desc='Right Grey White Mask, Aims writable volume formats',
        position=7, mandatory=False, argstr='%s')
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=8, mandatory=False)


class GreyWhiteClassificationOutputSpec(TraitedSpec):
    left_grey_white = traits.File(
        desc='Left Grey White Mask, Aims writable volume formats')
    right_grey_white = traits.File(
        desc='Right Grey White Mask, Aims writable volume formats')


class GreyWhiteClassification(BVCommand):
    input_spec = GreyWhiteClassificationInputSpec
    output_spec = GreyWhiteClassificationOutputSpec
    _cmd = 'GreyWhiteClassification'

