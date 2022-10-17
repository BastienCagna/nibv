from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulciswitchmanuallabelsInputSpec(CommandLineInputSpec):
    input_graph = traits.File(
        exists=True,
        desc='Data graph, Graph, requiredAttributes={labelled: Yes}',
        position=0, mandatory=False, argstr='%s')
    output_graph = traits.File(
        exists=False,
        desc='Data graph, Graph, requiredAttributes={labelled: Yes}',
        position=1, mandatory=False, argstr='%s')


class SulciswitchmanuallabelsOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Data graph, Graph, requiredAttributes={labelled: Yes}')


class Sulciswitchmanuallabels(BVCommand):
    input_spec = SulciswitchmanuallabelsInputSpec
    output_spec = SulciswitchmanuallabelsOutputSpec
    _cmd = 'Sulciswitchmanuallabels'

