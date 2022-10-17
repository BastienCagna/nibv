from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ResetInternalImageTransformationInputSpec(CommandLineInputSpec):
    input_image = traits.File(
        exists=True,
        desc='4D Volume, aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    output_image = traits.File(
        exists=False,
        desc='4D Volume, aims writable volume formats',
        position=1, mandatory=False, argstr='%s')
    roi_image = traits.File(
        exists=True,
        desc='4D Volume, aims readable volume formats',
        position=3, mandatory=False, argstr='%s')


class ResetInternalImageTransformationOutputSpec(TraitedSpec):
    output_image = traits.File(
        desc='4D Volume, aims writable volume formats')


class ResetInternalImageTransformation(BVCommand):
    input_spec = ResetInternalImageTransformationInputSpec
    output_spec = ResetInternalImageTransformationOutputSpec
    _cmd = 'ResetInternalImageTransformation'

