from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CorticalfoldsgraphInputSpec(CommandLineInputSpec):
    skeleton = traits.File(
        exists=True,
        desc='Cortex Skeleton, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    roots = traits.File(
        exists=True,
        desc='Cortex Catchment Bassins, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    grey_white = traits.File(
        exists=True,
        desc='Grey White Mask, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    hemi_cortex = traits.File(
        exists=True,
        desc='CSF+GREY Mask, Aims readable volume formats',
        position=3, mandatory=False, argstr='%s')
    split_brain = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=4, mandatory=False, argstr='%s')
    white_mesh = traits.File(
        exists=True,
        desc='Hemisphere White Mesh,  Aims mesh formats',
        position=5, mandatory=False, argstr='%s')
    pial_mesh = traits.File(
        exists=True,
        desc='Hemisphere Mesh,  Aims mesh formats',
        position=6, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=7, mandatory=False, argstr='%s')
    talairach_transform = traits.File(
        exists=True,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=8, mandatory=False, argstr='%s')
    compute_fold_meshes = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=9, mandatory=False)
    allow_multithreading = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=10, mandatory=False)
    graph_version = traits.Enum(
        "3.0", "3.1", "3.2",
        usedefault=False,
        desc='3.0, 3.1,  3.2',
        position=11, mandatory=False)
    graph = traits.File(
        exists=False,
        desc='Cortical folds graph,  Graph',
        position=12, mandatory=False, argstr='%s')
    sulci_voronoi = traits.File(
        exists=False,
        desc='Sulci Voronoi, Aims writable volume formats',
        position=13, mandatory=False, argstr='%s')
    write_cortex_mid_interface = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=14, mandatory=False)
    cortex_mid_interface = traits.File(
        exists=False,
        desc='Grey White Mid-Interface Volume, Aims writable volume formats',
        position=15, mandatory=False, argstr='%s')


class CorticalfoldsgraphOutputSpec(TraitedSpec):
    graph = traits.File(
        desc='Cortical folds graph,  Graph')
    sulci_voronoi = traits.File(
        desc='Sulci Voronoi, Aims writable volume formats')
    cortex_mid_interface = traits.File(
        desc='Grey White Mid-Interface Volume, Aims writable volume formats')


class Corticalfoldsgraph(BVCommand):
    input_spec = CorticalfoldsgraphInputSpec
    output_spec = CorticalfoldsgraphOutputSpec
    _cmd = 'Corticalfoldsgraph'

