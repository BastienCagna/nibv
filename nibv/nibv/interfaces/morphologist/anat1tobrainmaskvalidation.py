from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaT1toBrainMaskValidationInputSpec(CommandLineInputSpec):
    brain_mask = traits.File(
        exists=True,
        desc='T1 Brain Mask,  Aims readable volume formats',
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


class AnaT1toBrainMaskValidationOutputSpec(TraitedSpec):
    pass


class AnaT1toBrainMaskValidation(BVCommand):
    input_spec = AnaT1toBrainMaskValidationInputSpec
    output_spec = AnaT1toBrainMaskValidationOutputSpec
    _cmd = 'AnaT1toBrainMaskValidation'

