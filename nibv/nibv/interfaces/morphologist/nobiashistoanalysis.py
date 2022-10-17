from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class NobiasHistoAnalysisInputSpec(CommandLineInputSpec):
    t1mri_nobias = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
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
        desc='T1 MRI White Matter Ridges, Aims readable volume formats',
        position=4, mandatory=False, argstr='%s')
    undersampling = traits.Enum(
        "2", "4", "8", "16", "32", "auto", "iteration",
        usedefault=False,
        desc='2, 4, 8, 16, 32, auto,  iteration',
        position=5, mandatory=False)
    histo_analysis = traits.File(
        exists=False,
        desc='Histo Analysis,  Histo Analysis',
        position=6, mandatory=False, argstr='%s')
    histo = traits.File(
        exists=False,
        desc='Histogram,  Histogram',
        position=7, mandatory=False, argstr='%s')
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=8, mandatory=False)


class NobiasHistoAnalysisOutputSpec(TraitedSpec):
    histo_analysis = traits.File(
        desc='Histo Analysis,  Histo Analysis')
    histo = traits.File(
        desc='Histogram,  Histogram')


class NobiasHistoAnalysis(BVCommand):
    input_spec = NobiasHistoAnalysisInputSpec
    output_spec = NobiasHistoAnalysisOutputSpec
    _cmd = 'NobiasHistoAnalysis'

