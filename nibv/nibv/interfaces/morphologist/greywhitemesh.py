from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class GreyWhiteMeshInputSpec(CommandLineInputSpec):
    hemi_cortex = traits.File(
        exists=True,
        desc='CSF+GREY Mask, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    white_mesh = traits.File(
        exists=False,
        desc='Hemisphere White Mesh,  Aims mesh formats',
        position=1, mandatory=False, argstr='%s')


class GreyWhiteMeshOutputSpec(TraitedSpec):
    white_mesh = traits.File(
        desc='Hemisphere White Mesh,  Aims mesh formats')


class GreyWhiteMesh(BVCommand):
    input_spec = GreyWhiteMeshInputSpec
    output_spec = GreyWhiteMeshOutputSpec
    _cmd = 'GreyWhiteMesh'

