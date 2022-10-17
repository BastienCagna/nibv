from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulcilabelconsistencycheckInputSpec(CommandLineInputSpec):
    sulci_graph = traits.File(
        exists=True,
        desc='Labelled Cortical folds graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    side = traits.Enum(
        "left", "right", "None",
        usedefault=False,
        desc='left, right,  None',
        position=1, mandatory=False)


class SulcilabelconsistencycheckOutputSpec(TraitedSpec):
    pass


class Sulcilabelconsistencycheck(BVCommand):
    input_spec = SulcilabelconsistencycheckInputSpec
    output_spec = SulcilabelconsistencycheckOutputSpec
    _cmd = 'Sulcilabelconsistencycheck'

