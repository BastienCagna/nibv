from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SpamRecognitionglobalInputSpec(CommandLineInputSpec):
    data_graph = traits.File(
        exists=True,
        desc='Cortical folds graph,  Graph and data',
        position=0, mandatory=False, argstr='%s')
    output_graph = traits.File(
        exists=False,
        desc='Labelled Cortical folds graph, Graph and data, requiredAttributes={labelled: Yes, automatically_labelled: Yes}',
        position=1, mandatory=False, argstr='%s')
    model_type = traits.Enum(
        "Talairach", "Global registration",
        usedefault=False,
        desc='Talairach,  Global registration',
        position=2, mandatory=False)
    model = traits.File(
        exists=True,
        desc='Sulci Segments Model,  Text Data Table',
        position=3, mandatory=False, argstr='%s')
    posterior_probabilities = traits.File(
        exists=False,
        desc='Sulci Labels Segmentwise Posterior Probabilities, CSV file',
        position=4, mandatory=False, argstr='%s')
    labels_translation_map = traits.File(
        exists=True,
        desc='Label Translation, Label Translation,  DEF Label translation',
        position=5, mandatory=False, argstr='%s')
    labels_priors = traits.File(
        exists=True,
        desc='Sulci Labels Priors,  Text Data Table',
        position=6, mandatory=False, argstr='%s')
    output_transformation = traits.File(
        exists=False,
        desc='Sulci Talairach to Global SPAM transformation, Transformation matrix',
        position=7, mandatory=False, argstr='%s')
    initial_transformation = traits.File(
        exists=True,
        desc='Transformation matrix, Transformation matrix',
        position=8, mandatory=False, argstr='%s')
    output_t1_to_global_transformation = traits.File(
        exists=False,
        desc='Raw T1 to Global SPAM transformation, Transformation matrix',
        position=9, mandatory=False, argstr='%s')


class SpamRecognitionglobalOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Labelled Cortical folds graph, Graph and data, requiredAttributes={labelled: Yes, automatically_labelled: Yes}')
    posterior_probabilities = traits.File(
        desc='Sulci Labels Segmentwise Posterior Probabilities, CSV file')
    output_transformation = traits.File(
        desc='Sulci Talairach to Global SPAM transformation, Transformation matrix')
    output_t1_to_global_transformation = traits.File(
        desc='Raw T1 to Global SPAM transformation, Transformation matrix')


class SpamRecognitionglobal(BVCommand):
    input_spec = SpamRecognitionglobalInputSpec
    output_spec = SpamRecognitionglobalOutputSpec
    _cmd = 'SpamRecognitionglobal'

