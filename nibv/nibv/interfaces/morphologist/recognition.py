from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class RecognitionInputSpec(CommandLineInputSpec):
    data_graph = traits.File(
        exists=True,
        desc='Data graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    model = traits.File(
        exists=True,
        desc='Model graph, Graph, requiredAttributes={trained: Yes}',
        position=1, mandatory=False, argstr='%s')
    output_graph = traits.File(
        exists=False,
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={labelled: Yes, automatically_labelled: Yes}',
        position=2, mandatory=False, argstr='%s')
    energy_plot_file = traits.File(
        exists=False,
        desc='siRelax Fold Energy, siRelax Fold Energy',
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
    forbid_unknown_label = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=8, mandatory=False)
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=9, mandatory=False)


class RecognitionOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={labelled: Yes, automatically_labelled: Yes}')
    energy_plot_file = traits.File(
        desc='siRelax Fold Energy, siRelax Fold Energy')


class Recognition(BVCommand):
    input_spec = RecognitionInputSpec
    output_spec = RecognitionOutputSpec
    _cmd = 'Recognition'

