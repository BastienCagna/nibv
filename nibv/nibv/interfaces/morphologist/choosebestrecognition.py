from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ChooseBestRecognitionInputSpec(CommandLineInputSpec):
    output_graph = traits.File(
        exists=False,
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={automatically_labelled: Yes}',
        position=2, mandatory=False, argstr='%s')
    energy_plot_file = traits.File(
        exists=False,
        desc='siRelax Fold Energy, siRelax Fold Energy',
        position=3, mandatory=False, argstr='%s')
    stats_file = traits.File(
        exists=False,
        desc='Text file,  Text file',
        position=4, mandatory=False, argstr='%s')


class ChooseBestRecognitionOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={automatically_labelled: Yes}')
    energy_plot_file = traits.File(
        desc='siRelax Fold Energy, siRelax Fold Energy')
    stats_file = traits.File(
        desc='Text file,  Text file')


class ChooseBestRecognition(BVCommand):
    input_spec = ChooseBestRecognitionInputSpec
    output_spec = ChooseBestRecognitionOutputSpec
    _cmd = 'ChooseBestRecognition'

