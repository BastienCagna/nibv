from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulciDistanceToLesionStatsInputSpec(CommandLineInputSpec):
    output_csv = traits.File(
        exists=False,
        desc='CSV file,  CSV file',
        position=6, mandatory=False, argstr='%s')
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=7, mandatory=False, argstr='%s')
    model = traits.File(
        exists=True,
        desc='Model graph,  Graph',
        position=8, mandatory=False, argstr='%s')
    label_attribute = traits.Enum(
        "auto", "label", "name",
        usedefault=False,
        desc='auto, label,  name',
        position=10, mandatory=False)
    reuse_existing_distancemap = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=11, mandatory=False)
    lesions_sizes = traits.File(
        exists=False,
        desc='CSV file,  CSV file',
        position=12, mandatory=False, argstr='%s')


class SulciDistanceToLesionStatsOutputSpec(TraitedSpec):
    output_csv = traits.File(
        desc='CSV file,  CSV file')
    lesions_sizes = traits.File(
        desc='CSV file,  CSV file')


class SulciDistanceToLesionStats(BVCommand):
    input_spec = SulciDistanceToLesionStatsInputSpec
    output_spec = SulciDistanceToLesionStatsOutputSpec
    _cmd = 'SulciDistanceToLesionStats'

