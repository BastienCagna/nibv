from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ConcatenateHemiMeshesInputSpec(CommandLineInputSpec):
    left_mesh = traits.File(
        exists=True,
        desc='Mesh, aims mesh formats, requiredAttributes={side: left}',
        position=0, mandatory=False, argstr='%s')
    right_mesh = traits.File(
        exists=True,
        desc='Mesh, aims mesh formats, requiredAttributes={side: right}',
        position=1, mandatory=False, argstr='%s')
    both_mesh = traits.File(
        exists=False,
        desc='Mesh, aims mesh formats, requiredAttributes={side: both}',
        position=2, mandatory=False, argstr='%s')


class ConcatenateHemiMeshesOutputSpec(TraitedSpec):
    both_mesh = traits.File(
        desc='Mesh, aims mesh formats, requiredAttributes={side: both}')


class ConcatenateHemiMeshes(BVCommand):
    input_spec = ConcatenateHemiMeshesInputSpec
    output_spec = ConcatenateHemiMeshesOutputSpec
    _cmd = 'ConcatenateHemiMeshes'

