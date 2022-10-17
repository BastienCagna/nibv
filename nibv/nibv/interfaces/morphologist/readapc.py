from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ReadAPCInputSpec(CommandLineInputSpec):
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates,  Commissure coordinates',
        position=0, mandatory=False, argstr='%s')
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable volume Formats',
        position=1, mandatory=False, argstr='%s')


class ReadAPCOutputSpec(TraitedSpec):
    pass


class ReadAPC(BVCommand):
    input_spec = ReadAPCInputSpec
    output_spec = ReadAPCOutputSpec
    _cmd = 'ReadAPC'

