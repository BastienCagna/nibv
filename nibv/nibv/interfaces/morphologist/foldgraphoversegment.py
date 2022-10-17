from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class FoldgraphoversegmentInputSpec(CommandLineInputSpec):
    input_graph = traits.File(
        exists=True,
        desc='Cortical Folds Graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    output_graph = traits.File(
        exists=False,
        desc='Cortical Folds Graph,  Graph',
        position=2, mandatory=False, argstr='%s')
    skeleton = traits.File(
        exists=True,
        desc='Cortex Skeleton,  aims readable Volume Formats',
        position=3, mandatory=False, argstr='%s')
    pieces_length = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%f', mandatory=False)
    minimum_size = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%d', mandatory=False)


class FoldgraphoversegmentOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Cortical Folds Graph,  Graph')


class Foldgraphoversegment(BVCommand):
    input_spec = FoldgraphoversegmentInputSpec
    output_spec = FoldgraphoversegmentOutputSpec
    _cmd = 'Foldgraphoversegment'

