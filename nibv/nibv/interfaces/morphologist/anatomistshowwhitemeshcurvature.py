from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowWhiteMeshCurvatureInputSpec(CommandLineInputSpec):
    curvature_texture = traits.File(
        exists=True,
        desc='White Curvature Texture, Anatomist texture formats',
        position=0, mandatory=False, argstr='%s')
    triangulation = traits.File(
        exists=True,
        desc='Hemisphere White Mesh, anatomist mesh formats',
        position=1, mandatory=False, argstr='%s')


class AnatomistShowWhiteMeshCurvatureOutputSpec(TraitedSpec):
    pass


class AnatomistShowWhiteMeshCurvature(BVCommand):
    input_spec = AnatomistShowWhiteMeshCurvatureInputSpec
    output_spec = AnatomistShowWhiteMeshCurvatureOutputSpec
    _cmd = 'AnatomistShowWhiteMeshCurvature'

