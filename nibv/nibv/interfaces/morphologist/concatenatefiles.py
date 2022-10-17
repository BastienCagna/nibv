from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ConcatenatefilesInputSpec(CommandLineInputSpec):
    measures_files_without_header = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)
    group_measures = traits.File(
        exists=False,
        desc='Text file, Text file, CSV file,  Text Data Table',
        position=3, mandatory=False, argstr='%s')


class ConcatenatefilesOutputSpec(TraitedSpec):
    group_measures = traits.File(
        desc='Text file, Text file, CSV file,  Text Data Table')


class Concatenatefiles(BVCommand):
    input_spec = ConcatenatefilesInputSpec
    output_spec = ConcatenatefilesOutputSpec
    _cmd = 'Concatenatefiles'

