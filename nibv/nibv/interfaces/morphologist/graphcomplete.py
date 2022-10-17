from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class GraphCompleteInputSpec(CommandLineInputSpec):
    input_graph = traits.File(
        exists=True,
        desc='Cortical folds graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    output_graph = traits.File(
        exists=False,
        desc='Cortical folds graph,  Graph',
        position=1, mandatory=False, argstr='%s')


class GraphCompleteOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Cortical folds graph,  Graph')


class GraphComplete(BVCommand):
    input_spec = GraphCompleteInputSpec
    output_spec = GraphCompleteOutputSpec
    _cmd = 'GraphComplete'

