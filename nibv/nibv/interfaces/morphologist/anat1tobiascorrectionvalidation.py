from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaT1toBiasCorrectionValidationInputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable Volume Formats',
        position=1, mandatory=False, argstr='%s')
    validation = traits.Enum(
        "Visualise", "Lock", "Unlock",
        usedefault=False,
        desc='Visualise, Lock,  Unlock',
        position=2, mandatory=False)


class AnaT1toBiasCorrectionValidationOutputSpec(TraitedSpec):
    pass


class AnaT1toBiasCorrectionValidation(BVCommand):
    input_spec = AnaT1toBiasCorrectionValidationInputSpec
    output_spec = AnaT1toBiasCorrectionValidationOutputSpec
    _cmd = 'AnaT1toBiasCorrectionValidation'

