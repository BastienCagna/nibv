from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class MorphologistQcTableInputSpec(CommandLineInputSpec):
    acquisition = traits.String(
        None,
        usedefault=False,
        desc='',
        position=2, argstr='%s', mandatory=False)
    analysis = traits.String(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%s', mandatory=False)
    graph_version = traits.String(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%s', mandatory=False)
    output_file = traits.File(
        exists=False,
        desc='Text File,  HTML PDF',
        position=6, mandatory=False, argstr='%s')


class MorphologistQcTableOutputSpec(TraitedSpec):
    output_file = traits.File(
        desc='Text File,  HTML PDF')


class MorphologistQcTable(BVCommand):
    input_spec = MorphologistQcTableInputSpec
    output_spec = MorphologistQcTableOutputSpec
    _cmd = 'MorphologistQcTable'

