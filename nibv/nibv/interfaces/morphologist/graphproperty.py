from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class GraphPropertyInputSpec(CommandLineInputSpec):
    graph = traits.File(
        exists=True,
        desc='Graph, Graph, requiredAttributes={graph_version: 3.1}',
        position=0, mandatory=False, argstr='%s')
    output_directory = traits.File(
        exists=True,
        desc='Directory,  Directory',
        position=2, mandatory=False, argstr='%s')


class GraphPropertyOutputSpec(TraitedSpec):
    pass


class GraphProperty(BVCommand):
    input_spec = GraphPropertyInputSpec
    output_spec = GraphPropertyOutputSpec
    _cmd = 'GraphProperty'

