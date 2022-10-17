from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaComputeHemiGreyWhiteClassifInputSpec(CommandLineInputSpec):
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
    side = traits.Enum(
        "Both", "Left", "Right",
        usedefault=False,
        desc='Both, Left,  Right',
        position=3, mandatory=False)
    left_grey_white = traits.File(
        exists=False,
        desc='Left Grey White Mask, Aims writable volume formats',
        position=4, mandatory=False, argstr='%s')
    right_grey_white = traits.File(
        exists=False,
        desc='Right Grey White Mask, Aims writable volume formats',
        position=5, mandatory=False, argstr='%s')


class AnaComputeHemiGreyWhiteClassifOutputSpec(TraitedSpec):
    left_grey_white = traits.File(
        desc='Left Grey White Mask, Aims writable volume formats')
    right_grey_white = traits.File(
        desc='Right Grey White Mask, Aims writable volume formats')


class AnaComputeHemiGreyWhiteClassif(BVCommand):
    input_spec = AnaComputeHemiGreyWhiteClassifInputSpec
    output_spec = AnaComputeHemiGreyWhiteClassifOutputSpec
    _cmd = 'AnaComputeHemiGreyWhiteClassif'

