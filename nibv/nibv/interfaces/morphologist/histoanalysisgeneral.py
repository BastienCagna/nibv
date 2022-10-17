from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class HistoAnalysisGeneralInputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=False,
        desc='Histo Analysis,  Histo Analysis',
        position=1, mandatory=False, argstr='%s')
    hfiltered = traits.File(
        exists=True,
        desc='T1 MRI Filtered For Histo, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    white_ridges = traits.File(
        exists=True,
        desc='T1 MRI White Matter Ridges, Aims readable volume formats',
        position=3, mandatory=False, argstr='%s')


class HistoAnalysisGeneralOutputSpec(TraitedSpec):
    histo_analysis = traits.File(
        desc='Histo Analysis,  Histo Analysis')


class HistoAnalysisGeneral(BVCommand):
    input_spec = HistoAnalysisGeneralInputSpec
    output_spec = HistoAnalysisGeneralOutputSpec
    _cmd = 'HistoAnalysisGeneral'

