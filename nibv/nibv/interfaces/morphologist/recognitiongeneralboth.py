from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class RecognitionGeneralBothInputSpec(CommandLineInputSpec):
    side = traits.Enum(
        "left", "right", "both", "none",
        usedefault=False,
        desc='left, right, both,  none',
        position=0, mandatory=False)
    model = traits.Enum(
        "ann_model", "ann_model_2001", "spam_model", "desync_msg",
        usedefault=False,
        desc='ann_model, ann_model_2001, spam_model,  desync_msg',
        position=1, mandatory=False)
    left_data_graph = traits.File(
        exists=True,
        desc='Cortical Folds Graph, Graph and Data,  requiredAttributes={side: left}',
        position=2, mandatory=False, argstr='%s')
    left_output_graph = traits.File(
        exists=False,
        desc='Labelled Cortical Folds Graph, Graph and Data,  requiredAttributes={side: left}',
        position=3, mandatory=False, argstr='%s')
    right_data_graph = traits.File(
        exists=True,
        desc='Cortical Folds Graph, Graph and Data,  requiredAttributes={side: right}',
        position=4, mandatory=False, argstr='%s')
    right_output_graph = traits.File(
        exists=False,
        desc='Labelled Cortical Folds Graph, Graph and Data,  requiredAttributes={side: right}',
        position=5, mandatory=False, argstr='%s')


class RecognitionGeneralBothOutputSpec(TraitedSpec):
    left_output_graph = traits.File(
        desc='Labelled Cortical Folds Graph, Graph and Data,  requiredAttributes={side: left}')
    right_output_graph = traits.File(
        desc='Labelled Cortical Folds Graph, Graph and Data,  requiredAttributes={side: right}')


class RecognitionGeneralBoth(BVCommand):
    input_spec = RecognitionGeneralBothInputSpec
    output_spec = RecognitionGeneralBothOutputSpec
    _cmd = 'RecognitionGeneralBoth'

