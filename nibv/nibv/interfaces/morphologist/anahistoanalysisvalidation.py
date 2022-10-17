from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaHistoAnalysisValidationInputSpec(CommandLineInputSpec):
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
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


class AnaHistoAnalysisValidationOutputSpec(TraitedSpec):
    pass


class AnaHistoAnalysisValidation(BVCommand):
    input_spec = AnaHistoAnalysisValidationInputSpec
    output_spec = AnaHistoAnalysisValidationOutputSpec
    _cmd = 'AnaHistoAnalysisValidation'

