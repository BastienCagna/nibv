from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class MorphologistCapsulInputSpec(CommandLineInputSpec):
    transfer_inputs = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=4, mandatory=False)
    transfer_outputs = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=5, mandatory=False)
    use_translated_shared_directory = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=6, mandatory=False)
    workflow = traits.File(
        exists=False,
        desc='Text File,  Soma-Workflow workflow',
        position=7, mandatory=False, argstr='%s')
    edit_one_pipeline = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=8, mandatory=False)


class MorphologistCapsulOutputSpec(TraitedSpec):
    workflow = traits.File(
        desc='Text File,  Soma-Workflow workflow')


class MorphologistCapsul(BVCommand):
    input_spec = MorphologistCapsulInputSpec
    output_spec = MorphologistCapsulOutputSpec
    _cmd = 'MorphologistCapsul'

