from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class BrainvisaShowHistoAnalysisInputSpec(CommandLineInputSpec):
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=0, mandatory=False, argstr='%s')
    use_hfiltered = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=1, mandatory=False)
    hfiltered = traits.File(
        exists=True,
        desc='T1 MRI Filtered For Histo, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    use_wridges = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=3, mandatory=False)
    white_ridges = traits.File(
        exists=True,
        desc='T1 MRI White Matter Ridges,    Aims readable volume formats',
        position=4, mandatory=False, argstr='%s')


class BrainvisaShowHistoAnalysisOutputSpec(TraitedSpec):
    pass


class BrainvisaShowHistoAnalysis(BVCommand):
    input_spec = BrainvisaShowHistoAnalysisInputSpec
    output_spec = BrainvisaShowHistoAnalysisOutputSpec
    _cmd = 'BrainvisaShowHistoAnalysis'

