from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class WhitemeshdepthmapInputSpec(CommandLineInputSpec):
    white_mesh = traits.File(
        exists=True,
        desc='Hemisphere White Mesh,  Aims mesh formats',
        position=0, mandatory=False, argstr='%s')
    hemi_cortex = traits.File(
        exists=True,
        desc='CSF+GREY Mask, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    depth_texture = traits.File(
        exists=False,
        desc='White Depth Texture, aims Texture formats',
        position=2, mandatory=False, argstr='%s')
    closing_size = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%f', mandatory=False)


class WhitemeshdepthmapOutputSpec(TraitedSpec):
    depth_texture = traits.File(
        desc='White Depth Texture, aims Texture formats')


class Whitemeshdepthmap(BVCommand):
    input_spec = WhitemeshdepthmapInputSpec
    output_spec = WhitemeshdepthmapOutputSpec
    _cmd = 'Whitemeshdepthmap'

