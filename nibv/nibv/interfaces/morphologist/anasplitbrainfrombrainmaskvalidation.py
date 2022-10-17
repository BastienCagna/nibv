from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaSplitBrainfromBrainMaskValidationInputSpec(CommandLineInputSpec):
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    validation = traits.Enum(
        "Visualise", "Lock", "Unlock",
        usedefault=False,
        desc='Visualise, Lock,  Unlock',
        position=2, mandatory=False)


class AnaSplitBrainfromBrainMaskValidationOutputSpec(TraitedSpec):
    pass


class AnaSplitBrainfromBrainMaskValidation(BVCommand):
    input_spec = AnaSplitBrainfromBrainMaskValidationInputSpec
    output_spec = AnaSplitBrainfromBrainMaskValidationOutputSpec
    _cmd = 'AnaSplitBrainfromBrainMaskValidation'

