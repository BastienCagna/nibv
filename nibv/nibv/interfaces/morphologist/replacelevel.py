from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ReplaceLevelInputSpec(CommandLineInputSpec):
    image = traits.File(
        exists=True,
        desc='3D Volume,  Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    method = traits.Enum(
        "gt", "le", "lt", "ge", "eq", "di", "be", "ou",
        usedefault=False,
        desc='gt, le, lt, ge, eq, di, be,  ou',
        position=1, mandatory=False)
    normalize = traits.Enum(
        "yes", "no",
        usedefault=False,
        desc='yes,  no',
        position=2, mandatory=False)
    threshold = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%f', mandatory=False)


class ReplaceLevelOutputSpec(TraitedSpec):
    pass


class ReplaceLevel(BVCommand):
    input_spec = ReplaceLevelInputSpec
    output_spec = ReplaceLevelOutputSpec
    _cmd = 'ReplaceLevel'

