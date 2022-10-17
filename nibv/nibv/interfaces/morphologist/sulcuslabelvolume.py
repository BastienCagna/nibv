from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulcuslabelvolumeInputSpec(CommandLineInputSpec):
    graph = traits.File(
        exists=True,
        desc='Cortical folds graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    mri = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, aims readable Volume Formats',
        position=1, mandatory=False, argstr='%s')
    transformation_matrix = traits.File(
        exists=True,
        desc='Transformation matrix, Transformation matrix',
        position=2, mandatory=False, argstr='%s')
    transformation_template = traits.File(
        exists=True,
        desc='3D Volume, aims readable Volume Formats',
        position=3, mandatory=False, argstr='%s')
    transformation = traits.Enum(
        "No", "Yes",
        usedefault=False,
        desc='No,  Yes',
        position=4, mandatory=False)
    binarize = traits.Enum(
        "No", "Yes",
        usedefault=False,
        desc='No,  Yes',
        position=5, mandatory=False)
    sulci = traits.File(
        exists=False,
        desc='Sulci Volume,  Aims writable volume formats',
        position=6, mandatory=False, argstr='%s')
    simple_surface = traits.File(
        exists=False,
        desc='Simple Surface Volume, Aims writable volume formats',
        position=7, mandatory=False, argstr='%s')
    bottom = traits.File(
        exists=False,
        desc='Bottom Volume,  Aims writable volume formats',
        position=8, mandatory=False, argstr='%s')
    hull_junction = traits.File(
        exists=False,
        desc='Hull Junction Volume, Aims writable volume formats',
        position=9, mandatory=False, argstr='%s')
    compress = traits.Enum(
        "Yes", "No",
        usedefault=False,
        desc='Yes,  No',
        position=10, mandatory=False)
    bucket = traits.Enum(
        "custom", "Sulci", "Simple Surfaces", "Bottoms", "Junctions with brain hull",
        usedefault=False,
        desc='custom, Sulci, Simple Surfaces, Bottoms, Junctions with brain hull',
        position=11, mandatory=False)
    custom_buckets = traits.String(
        None,
        usedefault=False,
        desc='',
        position=12, argstr='%s', mandatory=False)
    label_translation = traits.File(
        exists=True,
        desc='Label Translation,  Label Translation',
        position=13, mandatory=False, argstr='%s')
    input_int_to_label_translation = traits.File(
        exists=True,
        desc='log file,  text file',
        position=14, mandatory=False, argstr='%s')
    int_to_label_translation = traits.File(
        exists=False,
        desc='log file,  text file',
        position=15, mandatory=False, argstr='%s')
    label_attributes = traits.Enum(
        "custom", "label", "name",
        usedefault=False,
        desc='custom, , label,  name',
        position=16, mandatory=False)
    custom_label_attributes = traits.String(
        None,
        usedefault=False,
        desc='',
        position=17, argstr='%s', mandatory=False)
    node_edge_types = traits.Enum(
        "All", "custom", "Nodes", "Relations",
        usedefault=False,
        desc='All, custom, Nodes, Relations',
        position=18, mandatory=False)
    custom_node_edge_types = traits.String(
        None,
        usedefault=False,
        desc='',
        position=19, argstr='%s', mandatory=False)
    label_values = traits.String(
        None,
        usedefault=False,
        desc='',
        position=20, argstr='%s', mandatory=False)


class SulcuslabelvolumeOutputSpec(TraitedSpec):
    sulci = traits.File(
        desc='Sulci Volume,  Aims writable volume formats')
    simple_surface = traits.File(
        desc='Simple Surface Volume, Aims writable volume formats')
    bottom = traits.File(
        desc='Bottom Volume,  Aims writable volume formats')
    hull_junction = traits.File(
        desc='Hull Junction Volume, Aims writable volume formats')
    int_to_label_translation = traits.File(
        desc='log file,  text file')


class Sulcuslabelvolume(BVCommand):
    input_spec = SulcuslabelvolumeInputSpec
    output_spec = SulcuslabelvolumeOutputSpec
    _cmd = 'Sulcuslabelvolume'

