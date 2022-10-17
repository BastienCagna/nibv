from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaGetSphericalCorticalSurfaceInputSpec(CommandLineInputSpec):
    pass


class AnaGetSphericalCorticalSurfaceOutputSpec(TraitedSpec):
    pass


class AnaGetSphericalCorticalSurface(BVCommand):
    input_spec = AnaGetSphericalCorticalSurfaceInputSpec
    output_spec = AnaGetSphericalCorticalSurfaceOutputSpec
    _cmd = 'AnaGetSphericalCorticalSurface'

