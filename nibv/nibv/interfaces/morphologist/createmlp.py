from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CreatemlpInputSpec(CommandLineInputSpec):
    classifier = traits.File(
        exists=False,
        desc='Classifier,  MLP classifier',
        position=0, mandatory=False, argstr='%s')
    inputs_number = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=1, argstr='%d', mandatory=False)
    outputs_number = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%d', mandatory=False)


class CreatemlpOutputSpec(TraitedSpec):
    classifier = traits.File(
        desc='Classifier,  MLP classifier')


class Createmlp(BVCommand):
    input_spec = CreatemlpInputSpec
    output_spec = CreatemlpOutputSpec
    _cmd = 'Createmlp'

