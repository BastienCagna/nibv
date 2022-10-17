from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class InflateCorticalSurfaceInputSpec(CommandLineInputSpec):
    input_mesh = traits.File(
        exists=True,
        desc='Hemisphere White Mesh,  Aims mesh formats',
        position=0, mandatory=False, argstr='%s')
    output_mesh = traits.File(
        exists=False,
        desc='Inflated Hemisphere White Mesh, Aims mesh formats',
        position=1, mandatory=False, argstr='%s')
    curvature_texture = traits.File(
        exists=False,
        desc='White Curvature Texture, Aims texture formats',
        position=2, mandatory=False, argstr='%s')
    iterations = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%d', mandatory=False)
    normal_force = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%f', mandatory=False)
    spring_force = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%f', mandatory=False)
    smoothing_force = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=6, argstr='%f', mandatory=False)
    save_sequence = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=7, mandatory=False)


class InflateCorticalSurfaceOutputSpec(TraitedSpec):
    output_mesh = traits.File(
        desc='Inflated Hemisphere White Mesh, Aims mesh formats')
    curvature_texture = traits.File(
        desc='White Curvature Texture, Aims texture formats')


class InflateCorticalSurface(BVCommand):
    input_spec = InflateCorticalSurfaceInputSpec
    output_spec = InflateCorticalSurfaceOutputSpec
    _cmd = 'InflateCorticalSurface'

