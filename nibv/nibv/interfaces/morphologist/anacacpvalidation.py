from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaCACPValidationInputSpec(CommandLineInputSpec):
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=0, mandatory=False, argstr='%s')
    t1mri = traits.File(
        exists=True,
        desc='T1 MRI,  aims readable Volume Formats',
        position=1, mandatory=False, argstr='%s')
    validation = traits.Enum(
        "Visualise", "Lock", "Unlock",
        usedefault=False,
        desc='Visualise, Lock,  Unlock',
        position=2, mandatory=False)


class AnaCACPValidationOutputSpec(TraitedSpec):
    pass


class AnaCACPValidation(BVCommand):
    input_spec = AnaCACPValidationInputSpec
    output_spec = AnaCACPValidationOutputSpec
    _cmd = 'AnaCACPValidation'

