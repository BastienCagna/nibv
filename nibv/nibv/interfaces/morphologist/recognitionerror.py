from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class RecognitionErrorInputSpec(CommandLineInputSpec):
    model = traits.File(
        exists=True,
        desc='Model graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    labels_translation = traits.File(
        exists=True,
        desc='Label translation, Label translation,  DEF Label translation',
        position=1, mandatory=False, argstr='%s')
    base_graph = traits.File(
        exists=True,
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={labelled: Yes}',
        position=2, mandatory=False, argstr='%s')
    labeled_graph = traits.File(
        exists=True,
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={labelled: Yes, automatically_labelled: Yes}',
        position=3, mandatory=False, argstr='%s')
    base_graph_labeling = traits.Enum(
        "Automatic", "Manual",
        usedefault=False,
        desc='Automatic,  Manual',
        position=4, mandatory=False)
    labeled_graph_labeling = traits.Enum(
        "Automatic", "Manual",
        usedefault=False,
        desc='Automatic,  Manual',
        position=5, mandatory=False)
    error_file = traits.File(
        exists=False,
        desc='Text File,  Text File',
        position=6, mandatory=False, argstr='%s')


class RecognitionErrorOutputSpec(TraitedSpec):
    error_file = traits.File(
        desc='Text File,  Text File')


class RecognitionError(BVCommand):
    input_spec = RecognitionErrorInputSpec
    output_spec = RecognitionErrorOutputSpec
    _cmd = 'RecognitionError'

