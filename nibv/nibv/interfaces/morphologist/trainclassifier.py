from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class TrainclassifierInputSpec(CommandLineInputSpec):
    classifier = traits.File(
        exists=True,
        desc='Classifier, SVM classifier,  MLP classifier',
        position=0, mandatory=False, argstr='%s')
    output_classifier = traits.File(
        exists=False,
        desc='Classifier, SVM classifier, MLP classifier',
        position=1, mandatory=False, argstr='%s')
    input_data = traits.File(
        exists=True,
        desc='2D image,  aims readable Volume Formats',
        position=2, mandatory=False, argstr='%s')


class TrainclassifierOutputSpec(TraitedSpec):
    output_classifier = traits.File(
        desc='Classifier, SVM classifier, MLP classifier')


class Trainclassifier(BVCommand):
    input_spec = TrainclassifierInputSpec
    output_spec = TrainclassifierOutputSpec
    _cmd = 'Trainclassifier'

