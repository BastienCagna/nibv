from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CorticalFoldsGraphThicknessInputSpec(CommandLineInputSpec):
    graph = traits.File(
        exists=True,
        desc='Cortical folds graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    hemi_cortex = traits.File(
        exists=True,
        desc='CSF+GREY Mask, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    gw_interface = traits.File(
        exists=True,
        desc='Grey White Mask, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    white_mesh = traits.File(
        exists=True,
        desc='Hemisphere White Mesh,  Aims mesh formats',
        position=3, mandatory=False, argstr='%s')
    hemi_mesh = traits.File(
        exists=True,
        desc='Hemisphere Mesh,  Aims mesh formats',
        position=4, mandatory=False, argstr='%s')
    output_graph = traits.File(
        exists=False,
        desc='Cortical folds graph,  Graph',
        position=5, mandatory=False, argstr='%s')
    write_mid_interface = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=6, mandatory=False)
    output_mid_interface = traits.File(
        exists=False,
        desc='Grey White Mid-Interface Volume, Aims writable volume formats',
        position=7, mandatory=False, argstr='%s')
    sulci_voronoi = traits.File(
        exists=True,
        desc='Sulci Voronoi, Aims writable volume formats',
        position=8, mandatory=False, argstr='%s')


class CorticalFoldsGraphThicknessOutputSpec(TraitedSpec):
    output_graph = traits.File(
        desc='Cortical folds graph,  Graph')
    output_mid_interface = traits.File(
        desc='Grey White Mid-Interface Volume, Aims writable volume formats')


class CorticalFoldsGraphThickness(BVCommand):
    input_spec = CorticalFoldsGraphThicknessInputSpec
    output_spec = CorticalFoldsGraphThicknessOutputSpec
    _cmd = 'CorticalFoldsGraphThickness'

