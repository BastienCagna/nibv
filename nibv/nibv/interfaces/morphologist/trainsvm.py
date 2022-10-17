from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class TrainsvmInputSpec(CommandLineInputSpec):
    classifier = traits.File(
        exists=True,
        desc='Classifier,  SVM classifier',
        position=0, mandatory=False, argstr='%s')
    output_classifier = traits.File(
        exists=False,
        desc='Classifier,  SVM classifier',
        position=1, mandatory=False, argstr='%s')
    input_data = traits.File(
        exists=True,
        desc='2D image,  aims readable Volume Formats',
        position=2, mandatory=False, argstr='%s')
    svm_mode = traits.Enum(
        "classifier", "probability", "regression", "quality", "decision", "one_class",
        usedefault=False,
        desc='classifier, probability, regression, quality, decision,  one_class',
        position=3, mandatory=False)
    sigma = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%f', mandatory=False)
    c = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%f', mandatory=False)


class TrainsvmOutputSpec(TraitedSpec):
    output_classifier = traits.File(
        desc='Classifier,  SVM classifier')


class Trainsvm(BVCommand):
    input_spec = TrainsvmInputSpec
    output_spec = TrainsvmOutputSpec
    _cmd = 'Trainsvm'

