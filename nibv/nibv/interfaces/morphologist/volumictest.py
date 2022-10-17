from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class VolumicTestInputSpec(CommandLineInputSpec):
    average_group1 = traits.File(
        exists=False,
        desc='3D Volume, Aims writable volume formats',
        position=2, mandatory=False, argstr='%s')
    average_group2 = traits.File(
        exists=False,
        desc='3D Volume, Aims writable volume formats',
        position=3, mandatory=False, argstr='%s')
    mean_difference = traits.File(
        exists=False,
        desc='3D Volume, Aims writable volume formats',
        position=4, mandatory=False, argstr='%s')
    deviation = traits.File(
        exists=False,
        desc='3D Volume, Aims writable volume formats',
        position=5, mandatory=False, argstr='%s')
    t_test = traits.File(
        exists=False,
        desc='3D Volume,  Aims writable volume formats',
        position=6, mandatory=False, argstr='%s')
    data_smoothing = traits.Enum(
        "Yes", "No",
        usedefault=False,
        desc='Yes,  No',
        position=7, mandatory=False)
    smoothing_parameter = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=8, argstr='%f', mandatory=False)


class VolumicTestOutputSpec(TraitedSpec):
    average_group1 = traits.File(
        desc='3D Volume, Aims writable volume formats')
    average_group2 = traits.File(
        desc='3D Volume, Aims writable volume formats')
    mean_difference = traits.File(
        desc='3D Volume, Aims writable volume formats')
    deviation = traits.File(
        desc='3D Volume, Aims writable volume formats')
    t_test = traits.File(
        desc='3D Volume,  Aims writable volume formats')


class VolumicTest(BVCommand):
    input_spec = VolumicTestInputSpec
    output_spec = VolumicTestOutputSpec
    _cmd = 'VolumicTest'

