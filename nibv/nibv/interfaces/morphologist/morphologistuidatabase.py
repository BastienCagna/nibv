from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class MorphologistUiDatabaseInputSpec(CommandLineInputSpec):
    pass


class MorphologistUiDatabaseOutputSpec(TraitedSpec):
    pass


class MorphologistUiDatabase(BVCommand):
    input_spec = MorphologistUiDatabaseInputSpec
    output_spec = MorphologistUiDatabaseOutputSpec
    _cmd = 'MorphologistUiDatabase'

