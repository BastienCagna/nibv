from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class HistoAnalysisCreationInputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI bias corrected, Anatomist volume formats',
        position=0, mandatory=False, argstr='%s')
    histo = traits.File(
        exists=False,
        desc='Histogram,  Histogram',
        position=1, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=False,
        desc='Histo analysis,  Histo Analysis',
        position=2, mandatory=False, argstr='%s')


class HistoAnalysisCreationOutputSpec(TraitedSpec):
    histo = traits.File(
        desc='Histogram,  Histogram')
    histo_analysis = traits.File(
        desc='Histo analysis,  Histo Analysis')


class HistoAnalysisCreation(BVCommand):
    input_spec = HistoAnalysisCreationInputSpec
    output_spec = HistoAnalysisCreationOutputSpec
    _cmd = 'HistoAnalysisCreation'

