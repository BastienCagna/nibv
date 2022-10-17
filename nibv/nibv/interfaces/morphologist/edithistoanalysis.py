from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class EditHistoAnalysisInputSpec(CommandLineInputSpec):
    histo_analysis = traits.File(
        exists=False,
        desc='Histo Analysis,  Histo Analysis',
        position=0, mandatory=False, argstr='%s')


class EditHistoAnalysisOutputSpec(TraitedSpec):
    histo_analysis = traits.File(
        desc='Histo Analysis,  Histo Analysis')


class EditHistoAnalysis(BVCommand):
    input_spec = EditHistoAnalysisInputSpec
    output_spec = EditHistoAnalysisOutputSpec
    _cmd = 'EditHistoAnalysis'

