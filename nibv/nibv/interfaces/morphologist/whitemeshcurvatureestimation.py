from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class WhiteMeshCurvatureEstimationInputSpec(CommandLineInputSpec):
    side = traits.Enum(
        "Both", "Left", "Right",
        usedefault=False,
        desc='Both, Left,  Right',
        position=0, mandatory=False)
    method = traits.Enum(
        "fem", "barycenter", "boix",
        usedefault=False,
        desc='fem, barycenter,  boix',
        position=1, mandatory=False)
    left_white_mesh = traits.File(
        exists=True,
        desc='Left Hemisphere White Mesh,  aims Mesh Formats',
        position=2, mandatory=False, argstr='%s')
    right_white_mesh = traits.File(
        exists=True,
        desc='Right Hemisphere White Mesh,  aims Mesh Formats',
        position=3, mandatory=False, argstr='%s')
    left_white_curvature = traits.File(
        exists=False,
        desc='White Curvature Texture, Texture,  requiredAttributes={side: left}',
        position=4, mandatory=False, argstr='%s')
    right_white_curvature = traits.File(
        exists=False,
        desc='White Curvature Texture, Texture,  requiredAttributes={side: right}',
        position=5, mandatory=False, argstr='%s')
    threshold_ratio = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=6, argstr='%f', mandatory=False)


class WhiteMeshCurvatureEstimationOutputSpec(TraitedSpec):
    left_white_curvature = traits.File(
        desc='White Curvature Texture, Texture,  requiredAttributes={side: left}')
    right_white_curvature = traits.File(
        desc='White Curvature Texture, Texture,  requiredAttributes={side: right}')


class WhiteMeshCurvatureEstimation(BVCommand):
    input_spec = WhiteMeshCurvatureEstimationInputSpec
    output_spec = WhiteMeshCurvatureEstimationOutputSpec
    _cmd = 'WhiteMeshCurvatureEstimation'

