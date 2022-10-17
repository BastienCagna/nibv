from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowSymmetrizedDataInputSpec(CommandLineInputSpec):
    data_type = traits.Enum(
        "Any Type",
        usedefault=False,
        desc='Any Type',
        position=0, mandatory=False)


class AnatomistShowSymmetrizedDataOutputSpec(TraitedSpec):
    pass


class AnatomistShowSymmetrizedData(BVCommand):
    input_spec = AnatomistShowSymmetrizedDataInputSpec
    output_spec = AnatomistShowSymmetrizedDataOutputSpec
    _cmd = 'AnatomistShowSymmetrizedData'

