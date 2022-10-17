from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaComputeLCRClassifInputSpec(CommandLineInputSpec):
    left_grey_white = traits.File(
        exists=True,
        desc='Left Grey White Mask, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    right_grey_white = traits.File(
        exists=True,
        desc='Right Grey White Mask, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    left_csf = traits.File(
        exists=False,
        desc='Left CSF Mask,  Aims writable volume formats',
        position=2, mandatory=False, argstr='%s')
    right_csf = traits.File(
        exists=False,
        desc='Right CSF Mask, Aims writable volume formats',
        position=3, mandatory=False, argstr='%s')
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=4, mandatory=False, argstr='%s')


class AnaComputeLCRClassifOutputSpec(TraitedSpec):
    left_csf = traits.File(
        desc='Left CSF Mask,  Aims writable volume formats')
    right_csf = traits.File(
        desc='Right CSF Mask, Aims writable volume formats')


class AnaComputeLCRClassif(BVCommand):
    input_spec = AnaComputeLCRClassifInputSpec
    output_spec = AnaComputeLCRClassifOutputSpec
    _cmd = 'AnaComputeLCRClassif'

