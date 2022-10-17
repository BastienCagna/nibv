from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ClassifiersvmInputSpec(CommandLineInputSpec):
    input_data = traits.File(
        exists=True,
        desc='2D image,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    classifier = traits.File(
        exists=False,
        desc='Classifier,  SVM classifier',
        position=1, mandatory=False, argstr='%s')
    output_image = traits.File(
        exists=False,
        desc='Elevation map, aims writable Volume Formats',
        position=2, mandatory=False, argstr='%s')


class ClassifiersvmOutputSpec(TraitedSpec):
    classifier = traits.File(
        desc='Classifier,  SVM classifier')
    output_image = traits.File(
        desc='Elevation map, aims writable Volume Formats')


class Classifiersvm(BVCommand):
    input_spec = ClassifiersvmInputSpec
    output_spec = ClassifiersvmOutputSpec
    _cmd = 'Classifiersvm'

