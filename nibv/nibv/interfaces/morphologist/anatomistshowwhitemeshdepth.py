from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowWhiteMeshDepthInputSpec(CommandLineInputSpec):
    depth_texture = traits.File(
        exists=True,
        desc='White Depth Texture,  Texture',
        position=0, mandatory=False, argstr='%s')
    triangulation = traits.File(
        exists=True,
        desc='Hemisphere White Mesh, anatomist Mesh Formats',
        position=1, mandatory=False, argstr='%s')


class AnatomistShowWhiteMeshDepthOutputSpec(TraitedSpec):
    pass


class AnatomistShowWhiteMeshDepth(BVCommand):
    input_spec = AnatomistShowWhiteMeshDepthInputSpec
    output_spec = AnatomistShowWhiteMeshDepthOutputSpec
    _cmd = 'AnatomistShowWhiteMeshDepth'

