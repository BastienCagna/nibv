from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SpamRecognitionmarkovInputSpec(CommandLineInputSpec):
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
        desc='Sulci Segments Model, Text Data Table, requiredAttributes={sulci_segments_model_type:global_registered_spam}',
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
    segments_relations_model = traits.File(
        exists=True,
        desc='Sulci Segments Relations Model,  Text Data Table',
        position=6, mandatory=False, argstr='%s')
    initial_transformation = traits.File(
        exists=True,
        desc='Transformation matrix, Transformation matrix',
        position=7, mandatory=False, argstr='%s')
    global_transformation = traits.File(
        exists=True,
        desc='Sulci Talairach to Global SPAM transformation, Transformation matrix',
        position=8, mandatory=False, argstr='%s')
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=9, mandatory=False)


class SpamRecognitionmarkovOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Labelled Cortical folds graph, Graph and data, requiredAttributes={labelled: Yes, automatically_labelled: Yes}')
    posterior_probabilities = traits.File(
        desc='Sulci Labels Segmentwise Posterior Probabilities, CSV file')


class SpamRecognitionmarkov(BVCommand):
    input_spec = SpamRecognitionmarkovInputSpec
    output_spec = SpamRecognitionmarkovOutputSpec
    _cmd = 'SpamRecognitionmarkov'

