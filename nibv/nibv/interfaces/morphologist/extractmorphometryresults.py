from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ExtractmorphometryresultsInputSpec(CommandLineInputSpec):
    output_file = traits.File(
        exists=False,
        desc='CSV File,  CSV File',
        position=2, mandatory=False, argstr='%s')
    pipeline_mode = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=3, mandatory=False)


class ExtractmorphometryresultsOutputSpec(TraitedSpec):
    output_file = traits.File(
        desc='CSV File,  CSV File')


class Extractmorphometryresults(BVCommand):
    input_spec = ExtractmorphometryresultsInputSpec
    output_spec = ExtractmorphometryresultsOutputSpec
    _cmd = 'Extractmorphometryresults'

