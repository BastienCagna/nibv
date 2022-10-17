from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class TrainmlpInputSpec(CommandLineInputSpec):
    classifier = traits.File(
        exists=True,
        desc='Classifier,  MLP classifier',
        position=0, mandatory=False, argstr='%s')
    output_classifier = traits.File(
        exists=False,
        desc='Classifier,  MLP classifier',
        position=1, mandatory=False, argstr='%s')
    input_data = traits.File(
        exists=True,
        desc='2D image,  aims readable Volume Formats',
        position=2, mandatory=False, argstr='%s')
    cycles = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%d', mandatory=False)
    learn_factor = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%f', mandatory=False)


class TrainmlpOutputSpec(TraitedSpec):
    output_classifier = traits.File(
        desc='Classifier,  MLP classifier')


class Trainmlp(BVCommand):
    input_spec = TrainmlpInputSpec
    output_spec = TrainmlpOutputSpec
    _cmd = 'Trainmlp'

