from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ParallelRecognitionInputSpec(CommandLineInputSpec):
    data_graph = traits.File(
        exists=True,
        desc='Data graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    model = traits.File(
        exists=True,
        desc='Model graph,  Graph',
        position=1, mandatory=False, argstr='%s')
    output_graph = traits.File(
        exists=False,
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={labelled: Yes, automatically_labelled: Yes}',
        position=2, mandatory=False, argstr='%s')
    number_of_trials = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%d', mandatory=False)
    keep_all_results = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=5, mandatory=False)
    energy_plot_file = traits.File(
        exists=False,
        desc='siRelax Fold Energy,  siRelax Fold Energy',
        position=6, mandatory=False, argstr='%s')
    stats_file = traits.File(
        exists=False,
        desc='Text file,  Text file',
        position=7, mandatory=False, argstr='%s')
    rate = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=8, argstr='%f', mandatory=False)
    stoprate = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=9, argstr='%f', mandatory=False)
    niterbelowstopprop = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=10, argstr='%d', mandatory=False)
    forbid_unknown_label = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=11, mandatory=False)


class ParallelRecognitionOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={labelled: Yes, automatically_labelled: Yes}')
    energy_plot_file = traits.File(
        desc='siRelax Fold Energy,  siRelax Fold Energy')
    stats_file = traits.File(
        desc='Text file,  Text file')


class ParallelRecognition(BVCommand):
    input_spec = ParallelRecognitionInputSpec
    output_spec = ParallelRecognitionOutputSpec
    _cmd = 'ParallelRecognition'

