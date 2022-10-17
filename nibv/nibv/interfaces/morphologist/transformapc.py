from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class TransformAPCInputSpec(CommandLineInputSpec):
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates,  Commissure coordinates',
        position=0, mandatory=False, argstr='%s')
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  AIMS readable volume formats',
        position=1, mandatory=False, argstr='%s')
    output_coordinates = traits.File(
        exists=False,
        desc='Commissure coordinates, Commissure coordinates',
        position=2, mandatory=False, argstr='%s')
    transformation = traits.File(
        exists=True,
        desc='Transformation Matrix, Transformation matrix',
        position=3, mandatory=False, argstr='%s')
    destination_volume = traits.File(
        exists=True,
        desc='Raw T1 MRI, AIMS readable volume formats',
        position=4, mandatory=False, argstr='%s')


class TransformAPCOutputSpec(TraitedSpec):
    output_coordinates = traits.File(
        desc='Commissure coordinates, Commissure coordinates')


class TransformAPC(BVCommand):
    input_spec = TransformAPCInputSpec
    output_spec = TransformAPCOutputSpec
    _cmd = 'TransformAPC'

