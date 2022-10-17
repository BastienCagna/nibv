from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class TransferSulciLabelsInputSpec(CommandLineInputSpec):
    labelled_graph = traits.File(
        exists=True,
        desc='Labelled Cortical Folds Graph,  Graph and data',
        position=0, mandatory=False, argstr='%s')
    unlabelled_graph = traits.File(
        exists=True,
        desc='Cortical Folds Graph,  Graph and data',
        position=1, mandatory=False, argstr='%s')
    output_graph = traits.File(
        exists=False,
        desc='Labelled Cortical folds graph, Graph and Data, requiredAttributes={labelled: Yes}',
        position=2, mandatory=False, argstr='%s')
    label_attribute = traits.Enum(
        "name", "label",
        usedefault=False,
        desc='name,  label',
        position=3, mandatory=False)
    output_labels_table = traits.File(
        exists=False,
        desc='Text File,  Text File',
        position=4, mandatory=False, argstr='%s')
    force_same_space = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=5, mandatory=False)


class TransferSulciLabelsOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Labelled Cortical folds graph, Graph and Data, requiredAttributes={labelled: Yes}')
    output_labels_table = traits.File(
        desc='Text File,  Text File')


class TransferSulciLabels(BVCommand):
    input_spec = TransferSulciLabelsInputSpec
    output_spec = TransferSulciLabelsOutputSpec
    _cmd = 'TransferSulciLabels'

