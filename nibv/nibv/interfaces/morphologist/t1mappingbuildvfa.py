from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class T1mappingBuildVFAInputSpec(CommandLineInputSpec):
    t1weighted_low_angle = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    t1weighted_high_angle = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    bafi_amplitude_map = traits.File(
        exists=True,
        desc='4D Volume,  aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    bafi_phase_map = traits.File(
        exists=True,
        desc='4D Volume,  aims readable volume formats',
        position=3, mandatory=False, argstr='%s')
    output_t1_map = traits.File(
        exists=False,
        desc='Raw T1 MRI,  aims writable volume formats',
        position=4, mandatory=False, argstr='%s')
    invert = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=5, mandatory=False)
    bafi_smoothing = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=6, argstr='%f', mandatory=False)


class T1mappingBuildVFAOutputSpec(TraitedSpec):
    output_t1_map = traits.File(
        desc='Raw T1 MRI,  aims writable volume formats')


class T1mappingBuildVFA(BVCommand):
    input_spec = T1mappingBuildVFAInputSpec
    output_spec = T1mappingBuildVFAOutputSpec
    _cmd = 'T1mappingBuildVFA'

