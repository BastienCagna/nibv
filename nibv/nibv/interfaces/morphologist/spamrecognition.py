from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SpamRecognitionInputSpec(CommandLineInputSpec):
    data_graph = traits.File(
        exists=True,
        desc='Cortical folds graph,  Graph and data',
        position=0, mandatory=False, argstr='%s')
    output_graph = traits.File(
        exists=False,
        desc='Labelled Cortical folds graph, Graph and data, requiredAttributes={labelled: Yes, automatically_labelled: Yes}',
        position=1, mandatory=False, argstr='%s')
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)


class SpamRecognitionOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Labelled Cortical folds graph, Graph and data, requiredAttributes={labelled: Yes, automatically_labelled: Yes}')


class SpamRecognition(BVCommand):
    input_spec = SpamRecognitionInputSpec
    output_spec = SpamRecognitionOutputSpec
    _cmd = 'SpamRecognition'

