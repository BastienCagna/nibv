from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class BiasCorrectionFromB1mapInputSpec(CommandLineInputSpec):
    biased_image = traits.File(
        exists=True,
        desc='3D Volume,  aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    corrected_image = traits.File(
        exists=False,
        desc='3D Volume,  aims writable volume formats',
        position=1, mandatory=False, argstr='%s')
    bafi_amplitude_map = traits.File(
        exists=True,
        desc='4D Volume,  aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    bafi_phase_map = traits.File(
        exists=True,
        desc='4D Volume,  aims readable volume formats',
        position=3, mandatory=False, argstr='%s')
    b1_map = traits.File(
        exists=True,
        desc='3D Volume,  aims readable volume formats',
        position=4, mandatory=False, argstr='%s')
    dp_gre_lowcontrast = traits.File(
        exists=True,
        desc='3D Volume,  aims readable volume formats',
        position=5, mandatory=False, argstr='%s')
    correction_field = traits.File(
        exists=False,
        desc='3D Volume,  aims writable volume formats',
        position=6, mandatory=False, argstr='%s')
    field_threshold = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=7, argstr='%f', mandatory=False)


class BiasCorrectionFromB1mapOutputSpec(TraitedSpec):
    corrected_image = traits.File(
        desc='3D Volume,  aims writable volume formats')
    correction_field = traits.File(
        desc='3D Volume,  aims writable volume formats')


class BiasCorrectionFromB1map(BVCommand):
    input_spec = BiasCorrectionFromB1mapInputSpec
    output_spec = BiasCorrectionFromB1mapOutputSpec
    _cmd = 'BiasCorrectionFromB1map'

