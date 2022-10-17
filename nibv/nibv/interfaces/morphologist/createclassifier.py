from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CreateclassifierInputSpec(CommandLineInputSpec):
    classifier = traits.File(
        exists=False,
        desc='Classifier, SVM classifier,  MLP classifier',
        position=0, mandatory=False, argstr='%s')
    inputs_number = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=1, argstr='%d', mandatory=False)


class CreateclassifierOutputSpec(TraitedSpec):
    classifier = traits.File(
        desc='Classifier, SVM classifier,  MLP classifier')


class Createclassifier(BVCommand):
    input_spec = CreateclassifierInputSpec
    output_spec = CreateclassifierOutputSpec
    _cmd = 'Createclassifier'

