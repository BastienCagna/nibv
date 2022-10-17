from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ThresholdSimorphoOutputOnNNoutputInputSpec(CommandLineInputSpec):
    input_directory = traits.File(
        exists=True,
        desc='Directory,  Directory',
        position=0, mandatory=False, argstr='%s')
    good_regonition_percentage = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=1, argstr='%d', mandatory=False)
    remove_non_valid = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)
    select_all_descriptors = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=3, mandatory=False)
    output_directory = traits.File(
        exists=False,
        desc='Directory,  Directory',
        position=6, mandatory=False, argstr='%s')


class ThresholdSimorphoOutputOnNNoutputOutputSpec(TraitedSpec):
    output_directory = traits.File(
        desc='Directory,  Directory')


class ThresholdSimorphoOutputOnNNoutput(BVCommand):
    input_spec = ThresholdSimorphoOutputOnNNoutputInputSpec
    output_spec = ThresholdSimorphoOutputOnNNoutputOutputSpec
    _cmd = 'ThresholdSimorphoOutputOnNNoutput'

