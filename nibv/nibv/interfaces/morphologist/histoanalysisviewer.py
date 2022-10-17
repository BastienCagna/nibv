from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class HistoAnalysisViewerInputSpec(CommandLineInputSpec):
    histo_analysis = traits.File(
        exists=True,
        desc='Histo analysis,  Histo Analysis',
        position=0, mandatory=False, argstr='%s')
    histo = traits.File(
        exists=True,
        desc='Histogram,  Histogram',
        position=1, mandatory=False, argstr='%s')


class HistoAnalysisViewerOutputSpec(TraitedSpec):
    pass


class HistoAnalysisViewer(BVCommand):
    input_spec = HistoAnalysisViewerInputSpec
    output_spec = HistoAnalysisViewerOutputSpec
    _cmd = 'HistoAnalysisViewer'

