from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ModelgraphinfoInputSpec(CommandLineInputSpec):
    model_graph = traits.File(
        exists=True,
        desc='Model graph,  Graph and data',
        position=0, mandatory=False, argstr='%s')
    model_graph_description = traits.File(
        exists=True,
        desc='Data description,  HTML',
        position=1, mandatory=False, argstr='%s')


class ModelgraphinfoOutputSpec(TraitedSpec):
    pass


class Modelgraphinfo(BVCommand):
    input_spec = ModelgraphinfoInputSpec
    output_spec = ModelgraphinfoOutputSpec
    _cmd = 'Modelgraphinfo'

