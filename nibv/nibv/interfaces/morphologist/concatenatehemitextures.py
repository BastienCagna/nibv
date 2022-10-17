from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ConcatenateHemiTexturesInputSpec(CommandLineInputSpec):
    left_texture = traits.File(
        exists=True,
        desc='Texture, aims texture formats, requiredAttributes={side: left}',
        position=0, mandatory=False, argstr='%s')
    right_texture = traits.File(
        exists=True,
        desc='Texture, aims texture formats, requiredAttributes={side: right}',
        position=1, mandatory=False, argstr='%s')
    both_texture = traits.File(
        exists=False,
        desc='Texture, aims texture formats, requiredAttributes={side: both}',
        position=2, mandatory=False, argstr='%s')
    left_offset = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%f', mandatory=False)
    right_offset = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%f', mandatory=False)


class ConcatenateHemiTexturesOutputSpec(TraitedSpec):
    both_texture = traits.File(
        desc='Texture, aims texture formats, requiredAttributes={side: both}')


class ConcatenateHemiTextures(BVCommand):
    input_spec = ConcatenateHemiTexturesInputSpec
    output_spec = ConcatenateHemiTexturesOutputSpec
    _cmd = 'ConcatenateHemiTextures'

