from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SpamRecognitionlocalInputSpec(CommandLineInputSpec):
    data_graph = traits.File(
        exists=True,
        desc='Cortical folds graph,  Graph and data',
        position=0, mandatory=False, argstr='%s')
    output_graph = traits.File(
        exists=False,
        desc='Labelled Cortical folds graph, Graph and data, requiredAttributes={labelled: Yes, automatically_labelled: Yes}',
        position=1, mandatory=False, argstr='%s')
    model = traits.File(
        exists=True,
        desc='Sulci Segments Model,  Text Data Table',
        position=2, mandatory=False, argstr='%s')
    posterior_probabilities = traits.File(
        exists=False,
        desc='Sulci Labels Segmentwise Posterior Probabilities, CSV file',
        position=3, mandatory=False, argstr='%s')
    labels_translation_map = traits.File(
        exists=True,
        desc='Label Translation, Label Translation,  DEF Label translation',
        position=4, mandatory=False, argstr='%s')
    labels_priors = traits.File(
        exists=True,
        desc='Sulci Labels Priors,  Text Data Table',
        position=5, mandatory=False, argstr='%s')
    local_referentials = traits.File(
        exists=True,
        desc='Sulci Local referentials, Text Data Table',
        position=6, mandatory=False, argstr='%s')
    direction_priors = traits.File(
        exists=True,
        desc='Sulci Direction Transformation Priors, Text Data Table',
        position=7, mandatory=False, argstr='%s')
    angle_priors = traits.File(
        exists=True,
        desc='Sulci Angle Transformation Priors, Text Data Table',
        position=8, mandatory=False, argstr='%s')
    translation_priors = traits.File(
        exists=True,
        desc='Sulci Translation Transformation Priors, Text Data Table',
        position=9, mandatory=False, argstr='%s')
    output_local_transformations = traits.File(
        exists=False,
        desc='Sulci Local SPAM transformations Directory, Directory',
        position=10, mandatory=False, argstr='%s')
    initial_transformation = traits.File(
        exists=True,
        desc='Transformation matrix, Transformation matrix',
        position=11, mandatory=False, argstr='%s')
    global_transformation = traits.File(
        exists=True,
        desc='Sulci Talairach to Global SPAM transformation, Transformation matrix',
        position=12, mandatory=False, argstr='%s')


class SpamRecognitionlocalOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Labelled Cortical folds graph, Graph and data, requiredAttributes={labelled: Yes, automatically_labelled: Yes}')
    posterior_probabilities = traits.File(
        desc='Sulci Labels Segmentwise Posterior Probabilities, CSV file')
    output_local_transformations = traits.File(
        desc='Sulci Local SPAM transformations Directory, Directory')


class SpamRecognitionlocal(BVCommand):
    input_spec = SpamRecognitionlocalInputSpec
    output_spec = SpamRecognitionlocalOutputSpec
    _cmd = 'SpamRecognitionlocal'

