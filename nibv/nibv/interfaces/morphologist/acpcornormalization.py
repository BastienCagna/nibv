from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AcpcOrNormalizationInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=False,
        desc='Commissure coordinates, Commissure coordinates',
        position=1, mandatory=False, argstr='%s')
    allow_flip_initial_mri = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)
    reoriented_t1mri = traits.File(
        exists=False,
        desc='Raw T1 MRI, aims writable volume formats',
        position=3, mandatory=False, argstr='%s')


class AcpcOrNormalizationOutputSpec(TraitedSpec):
    commissure_coordinates = traits.File(
        desc='Commissure coordinates, Commissure coordinates')
    reoriented_t1mri = traits.File(
        desc='Raw T1 MRI, aims writable volume formats')


class AcpcOrNormalization(BVCommand):
    input_spec = AcpcOrNormalizationInputSpec
    output_spec = AcpcOrNormalizationOutputSpec
    _cmd = 'AcpcOrNormalization'

