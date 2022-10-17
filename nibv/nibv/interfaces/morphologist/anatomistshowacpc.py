from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowACPCInputSpec(CommandLineInputSpec):
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=0, mandatory=False, argstr='%s')
    show_t1mri = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=1, mandatory=False)
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI, Anatomist volume formats, exactType=True',
        position=2, mandatory=False, argstr='%s')


class AnatomistShowACPCOutputSpec(TraitedSpec):
    pass


class AnatomistShowACPC(BVCommand):
    input_spec = AnatomistShowACPCInputSpec
    output_spec = AnatomistShowACPCOutputSpec
    _cmd = 'AnatomistShowACPC'

