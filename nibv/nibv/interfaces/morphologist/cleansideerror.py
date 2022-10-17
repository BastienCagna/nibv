from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CleanSideErrorInputSpec(CommandLineInputSpec):
    pass


class CleanSideErrorOutputSpec(TraitedSpec):
    pass


class CleanSideError(BVCommand):
    input_spec = CleanSideErrorInputSpec
    output_spec = CleanSideErrorOutputSpec
    _cmd = 'CleanSideError'

