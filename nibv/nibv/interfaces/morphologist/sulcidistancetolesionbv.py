from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulciDistanceToLesionBVInputSpec(CommandLineInputSpec):
    lgrey_white = traits.File(
        exists=True,
        desc='Left grey white mask, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    rgrey_white = traits.File(
        exists=True,
        desc='Right grey white mask, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    lesion_mask = traits.File(
        exists=True,
        desc='Lesion Mask,  Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    distance_map = traits.File(
        exists=False,
        desc='Lesion distance map, Aims readable volume formats',
        position=3, mandatory=False, argstr='%s')
    lgraph = traits.File(
        exists=True,
        desc='Labelled Cortical Folds Graph, Graph and data,  requiredAttributes={side: left}',
        position=4, mandatory=False, argstr='%s')
    rgraph = traits.File(
        exists=True,
        desc='Labelled Cortical Folds Graph, Graph and data,  requiredAttributes={side: right}',
        position=5, mandatory=False, argstr='%s')
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


class SulciDistanceToLesionBVOutputSpec(TraitedSpec):
    distance_map = traits.File(
        desc='Lesion distance map, Aims readable volume formats')
    output_csv = traits.File(
        desc='CSV file,  CSV file')


class SulciDistanceToLesionBV(BVCommand):
    input_spec = SulciDistanceToLesionBVInputSpec
    output_spec = SulciDistanceToLesionBVOutputSpec
    _cmd = 'SulciDistanceToLesionBV'

