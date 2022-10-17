from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class VolumicDeviationInputSpec(CommandLineInputSpec):
    reference = traits.File(
        exists=True,
        desc='3D Volume,  Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    deviation = traits.File(
        exists=False,
        desc='3D Volume,  Aims writable volume formats',
        position=2, mandatory=False, argstr='%s')
    data_smoothing = traits.Enum(
        "Yes", "No",
        usedefault=False,
        desc='Yes,  No',
        position=3, mandatory=False)
    smoothing_parameter = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%f', mandatory=False)


class VolumicDeviationOutputSpec(TraitedSpec):
    deviation = traits.File(
        desc='3D Volume,  Aims writable volume formats')


class VolumicDeviation(BVCommand):
    input_spec = VolumicDeviationInputSpec
    output_spec = VolumicDeviationOutputSpec
    _cmd = 'VolumicDeviation'

