from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SurfaceareaInputSpec(CommandLineInputSpec):
    output_csv = traits.File(
        exists=False,
        desc='CSV file,  CSV file',
        position=1, mandatory=False, argstr='%s')


class SurfaceareaOutputSpec(TraitedSpec):
    output_csv = traits.File(
        desc='CSV file,  CSV file')


class Surfacearea(BVCommand):
    input_spec = SurfaceareaInputSpec
    output_spec = SurfaceareaOutputSpec
    _cmd = 'Surfacearea'

