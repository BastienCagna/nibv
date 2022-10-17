from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class RecognitionGeneralInputSpec(CommandLineInputSpec):
    data_graph = traits.File(
        exists=True,
        desc='Data graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    output_graph = traits.File(
        exists=False,
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={labelled: Yes, automatically_labelled: Yes}',
        position=1, mandatory=False, argstr='%s')
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)


class RecognitionGeneralOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={labelled: Yes, automatically_labelled: Yes}')


class RecognitionGeneral(BVCommand):
    input_spec = RecognitionGeneralInputSpec
    output_spec = RecognitionGeneralOutputSpec
    _cmd = 'RecognitionGeneral'

