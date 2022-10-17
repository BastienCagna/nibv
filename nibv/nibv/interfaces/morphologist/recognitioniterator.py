from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class RecognitionIteratorInputSpec(CommandLineInputSpec):
    model = traits.File(
        exists=True,
        desc='Model graph,  Graph',
        position=1, mandatory=False, argstr='%s')
    session = traits.String(
        None,
        usedefault=False,
        desc='',
        position=2, argstr='%s', mandatory=False)
    output = traits.File(
        exists=False,
        desc='CSV file,  CSV file',
        position=3, mandatory=False, argstr='%s')
    parallelism_mode = traits.Enum(
        "local", "grid", "duch", "LSF",
        usedefault=False,
        desc='local, grid, duch,  LSF',
        position=4, mandatory=False)


class RecognitionIteratorOutputSpec(TraitedSpec):
    output = traits.File(
        desc='CSV file,  CSV file')


class RecognitionIterator(BVCommand):
    input_spec = RecognitionIteratorInputSpec
    output_spec = RecognitionIteratorOutputSpec
    _cmd = 'RecognitionIterator'

