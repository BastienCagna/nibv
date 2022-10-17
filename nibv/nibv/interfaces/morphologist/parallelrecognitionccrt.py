from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ParallelRecognitionCCRTInputSpec(CommandLineInputSpec):
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
        position=3, argstr='%d', mandatory=False)
    energy_plot_file = traits.File(
        exists=False,
        desc='siRelax Fold Energy,  siRelax Fold Energy',
        position=4, mandatory=False, argstr='%s')
    rate = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%f', mandatory=False)
    stoprate = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=6, argstr='%f', mandatory=False)
    niterbelowstopprop = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=7, argstr='%d', mandatory=False)
    model_repl_path = traits.String(
        None,
        usedefault=False,
        desc='',
        position=8, argstr='%s', mandatory=False)
    data_repl_path = traits.String(
        None,
        usedefault=False,
        desc='',
        position=9, argstr='%s', mandatory=False)


class ParallelRecognitionCCRTOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={labelled: Yes, automatically_labelled: Yes}')
    energy_plot_file = traits.File(
        desc='siRelax Fold Energy,  siRelax Fold Energy')


class ParallelRecognitionCCRT(BVCommand):
    input_spec = ParallelRecognitionCCRTInputSpec
    output_spec = ParallelRecognitionCCRTOutputSpec
    _cmd = 'ParallelRecognitionCCRT'

