from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CreatesvmInputSpec(CommandLineInputSpec):
    classifier = traits.File(
        exists=False,
        desc='Classifier,  SVM classifier',
        position=0, mandatory=False, argstr='%s')
    inputs_number = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=1, argstr='%d', mandatory=False)


class CreatesvmOutputSpec(TraitedSpec):
    classifier = traits.File(
        desc='Classifier,  SVM classifier')


class Createsvm(BVCommand):
    input_spec = CreatesvmInputSpec
    output_spec = CreatesvmOutputSpec
    _cmd = 'Createsvm'

