from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class Testclassifier3InputSpec(CommandLineInputSpec):
    input_data = traits.File(
        exists=True,
        desc='2D image,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    classifier = traits.File(
        exists=True,
        desc='Classifier, SVM classifier,  MLP classifier',
        position=1, mandatory=False, argstr='%s')
    output_image = traits.File(
        exists=False,
        desc='Elevation map, aims writable Volume Formats',
        position=2, mandatory=False, argstr='%s')


class Testclassifier3OutputSpec(TraitedSpec):
    output_image = traits.File(
        desc='Elevation map, aims writable Volume Formats')


class Testclassifier3(BVCommand):
    input_spec = Testclassifier3InputSpec
    output_spec = Testclassifier3OutputSpec
    _cmd = 'Testclassifier3'

