from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulciCurvatureStatsInputSpec(CommandLineInputSpec):
    output_csv = traits.File(
        exists=False,
        desc='CSV file,  CSV file',
        position=1, mandatory=False, argstr='%s')
    include_nodewise = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=3, mandatory=False, argstr='%s')
    model = traits.File(
        exists=True,
        desc='Model graph,  Graph',
        position=4, mandatory=False, argstr='%s')
    label_attribute = traits.Enum(
        "auto", "label", "name",
        usedefault=False,
        desc='auto, label,  name',
        position=6, mandatory=False)
    workflow_file = traits.File(
        exists=False,
        desc='Text file,  Text file',
        position=8, mandatory=False, argstr='%s')


class SulciCurvatureStatsOutputSpec(TraitedSpec):
    output_csv = traits.File(
        desc='CSV file,  CSV file')
    workflow_file = traits.File(
        desc='Text file,  Text file')


class SulciCurvatureStats(BVCommand):
    input_spec = SulciCurvatureStatsInputSpec
    output_spec = SulciCurvatureStatsOutputSpec
    _cmd = 'SulciCurvatureStats'

