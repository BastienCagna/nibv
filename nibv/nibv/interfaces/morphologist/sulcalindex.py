from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulcalindexInputSpec(CommandLineInputSpec):
    global_sulcal_index_file = traits.File(
        exists=False,
        desc='CSV file,  CSV file',
        position=2, mandatory=False, argstr='%s')


class SulcalindexOutputSpec(TraitedSpec):
    global_sulcal_index_file = traits.File(
        desc='CSV file,  CSV file')


class Sulcalindex(BVCommand):
    input_spec = SulcalindexInputSpec
    output_spec = SulcalindexOutputSpec
    _cmd = 'Sulcalindex'

