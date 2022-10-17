from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulcigraphmorphometryintersubjectInputSpec(CommandLineInputSpec):
    output_directory = traits.File(
        exists=False,
        desc='Directory,  Directory',
        position=4, mandatory=False, argstr='%s')


class SulcigraphmorphometryintersubjectOutputSpec(TraitedSpec):
    output_directory = traits.File(
        desc='Directory,  Directory')


class Sulcigraphmorphometryintersubject(BVCommand):
    input_spec = SulcigraphmorphometryintersubjectInputSpec
    output_spec = SulcigraphmorphometryintersubjectOutputSpec
    _cmd = 'Sulcigraphmorphometryintersubject'

