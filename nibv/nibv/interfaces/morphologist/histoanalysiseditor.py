from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class HistoAnalysisEditorInputSpec(CommandLineInputSpec):
    histo_analysis = traits.File(
        exists=True,
        desc='Histo analysis,  Histo Analysis',
        position=0, mandatory=False, argstr='%s')
    histo = traits.File(
        exists=True,
        desc='Histogram,  Histogram',
        position=1, mandatory=False, argstr='%s')
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI bias corrected, Anatomist volume formats',
        position=2, mandatory=False, argstr='%s')


class HistoAnalysisEditorOutputSpec(TraitedSpec):
    pass


class HistoAnalysisEditor(BVCommand):
    input_spec = HistoAnalysisEditorInputSpec
    output_spec = HistoAnalysisEditorOutputSpec
    _cmd = 'HistoAnalysisEditor'

