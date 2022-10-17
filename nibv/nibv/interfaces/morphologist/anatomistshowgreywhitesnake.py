from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowGreyWhiteSnakeInputSpec(CommandLineInputSpec):
    snake = traits.File(
        exists=True,
        desc='CSF+GREY Mask,  Anatomist volume formats',
        position=0, mandatory=False, argstr='%s')
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Anatomist volume formats',
        position=1, mandatory=False, argstr='%s')


class AnatomistShowGreyWhiteSnakeOutputSpec(TraitedSpec):
    pass


class AnatomistShowGreyWhiteSnake(BVCommand):
    input_spec = AnatomistShowGreyWhiteSnakeInputSpec
    output_spec = AnatomistShowGreyWhiteSnakeOutputSpec
    _cmd = 'AnatomistShowGreyWhiteSnake'

