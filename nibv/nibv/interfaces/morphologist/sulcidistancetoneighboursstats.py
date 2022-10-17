from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulciDistanceToNeighboursStatsInputSpec(CommandLineInputSpec):
    output_csv = traits.File(
        exists=False,
        desc='CSV file,  CSV file',
        position=1, mandatory=False, argstr='%s')
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=2, mandatory=False, argstr='%s')
    model = traits.File(
        exists=True,
        desc='Model graph,  Graph',
        position=3, mandatory=False, argstr='%s')
    label_attribute = traits.Enum(
        "auto", "label", "name",
        usedefault=False,
        desc='auto, label,  name',
        position=5, mandatory=False)


class SulciDistanceToNeighboursStatsOutputSpec(TraitedSpec):
    output_csv = traits.File(
        desc='CSV file,  CSV file')


class SulciDistanceToNeighboursStats(BVCommand):
    input_spec = SulciDistanceToNeighboursStatsInputSpec
    output_spec = SulciDistanceToNeighboursStatsOutputSpec
    _cmd = 'SulciDistanceToNeighboursStats'

