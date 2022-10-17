from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowInflatedWhiteMeshInputSpec(CommandLineInputSpec):
    inflated_mesh = traits.File(
        exists=True,
        desc='Inflated Hemisphere White Mesh, Anatomist mesh formats',
        position=0, mandatory=False, argstr='%s')
    curvature_texture = traits.File(
        exists=True,
        desc='White Curvature Texture, Anatomist texture formats',
        position=1, mandatory=False, argstr='%s')


class AnatomistShowInflatedWhiteMeshOutputSpec(TraitedSpec):
    pass


class AnatomistShowInflatedWhiteMesh(BVCommand):
    input_spec = AnatomistShowInflatedWhiteMeshInputSpec
    output_spec = AnatomistShowInflatedWhiteMeshOutputSpec
    _cmd = 'AnatomistShowInflatedWhiteMesh'

