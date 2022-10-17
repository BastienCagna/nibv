from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CheckSpamModelsInputSpec(CommandLineInputSpec):
    auto_install = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=0, mandatory=False)


class CheckSpamModelsOutputSpec(TraitedSpec):
    pass


class CheckSpamModels(BVCommand):
    input_spec = CheckSpamModelsInputSpec
    output_spec = CheckSpamModelsOutputSpec
    _cmd = 'CheckSpamModels'

