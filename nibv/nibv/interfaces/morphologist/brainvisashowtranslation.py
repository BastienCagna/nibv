from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class BrainvisaShowTranslationInputSpec(CommandLineInputSpec):
    translation = traits.File(
        exists=True,
        desc='Label Translation,  Label Translation',
        position=0, mandatory=False, argstr='%s')


class BrainvisaShowTranslationOutputSpec(TraitedSpec):
    pass


class BrainvisaShowTranslation(BVCommand):
    input_spec = BrainvisaShowTranslationInputSpec
    output_spec = BrainvisaShowTranslationOutputSpec
    _cmd = 'BrainvisaShowTranslation'

