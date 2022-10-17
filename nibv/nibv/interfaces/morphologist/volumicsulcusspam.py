from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class VolumicSulcusSPAMInputSpec(CommandLineInputSpec):
    mri = traits.File(
        exists=True,
        desc='3D Volume,  Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    spam = traits.File(
        exists=False,
        desc='3D Volume,  Aims writable volume formats',
        position=2, mandatory=False, argstr='%s')
    smoothing = traits.Enum(
        "Yes", "No",
        usedefault=False,
        desc='Yes,  No',
        position=3, mandatory=False)
    smoothing_parameter = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%f', mandatory=False)
    bucket = traits.Enum(
        "custom", "Sulci", "Simple Surfaces", "Bottoms", "Junctions with brain hull",
        usedefault=False,
        desc='custom, Sulci, Simple Surfaces, Bottoms, Junctions with brain hull',
        position=5, mandatory=False)
    custom_buckets = traits.String(
        None,
        usedefault=False,
        desc='',
        position=6, argstr='%s', mandatory=False)
    label_translation = traits.File(
        exists=True,
        desc='Label Translation,  Label Translation',
        position=7, mandatory=False, argstr='%s')
    int_to_label_translation = traits.File(
        exists=False,
        desc='log file,  log file',
        position=8, mandatory=False, argstr='%s')
    label_attributes = traits.Enum(
        "custom", "label", "name",
        usedefault=False,
        desc='custom, , label,  name',
        position=9, mandatory=False)
    custom_label_attributes = traits.String(
        None,
        usedefault=False,
        desc='',
        position=10, argstr='%s', mandatory=False)
    node_edge_types = traits.Enum(
        "All", "custom", "Nodes", "Relations",
        usedefault=False,
        desc='All, custom, Nodes, Relations',
        position=11, mandatory=False)
    custom_node_edge_types = traits.String(
        None,
        usedefault=False,
        desc='',
        position=12, argstr='%s', mandatory=False)
    label_values = traits.String(
        None,
        usedefault=False,
        desc='',
        position=13, argstr='%s', mandatory=False)


class VolumicSulcusSPAMOutputSpec(TraitedSpec):
    spam = traits.File(
        desc='3D Volume,  Aims writable volume formats')
    int_to_label_translation = traits.File(
        desc='log file,  log file')


class VolumicSulcusSPAM(BVCommand):
    input_spec = VolumicSulcusSPAMInputSpec
    output_spec = VolumicSulcusSPAMOutputSpec
    _cmd = 'VolumicSulcusSPAM'

