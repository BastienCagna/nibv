from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class WhitemeshcurvaturemapInputSpec(CommandLineInputSpec):
    white_mesh = traits.File(
        exists=True,
        desc='Hemisphere White Mesh,  Aims mesh formats',
        position=0, mandatory=False, argstr='%s')
    curvature_texture = traits.File(
        exists=False,
        desc='White Curvature Texture,  Aims texture formats',
        position=1, mandatory=False, argstr='%s')


class WhitemeshcurvaturemapOutputSpec(TraitedSpec):
    curvature_texture = traits.File(
        desc='White Curvature Texture,  Aims texture formats')


class Whitemeshcurvaturemap(BVCommand):
    input_spec = WhitemeshcurvaturemapInputSpec
    output_spec = WhitemeshcurvaturemapOutputSpec
    _cmd = 'Whitemeshcurvaturemap'

