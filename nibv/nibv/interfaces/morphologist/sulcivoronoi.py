from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulcivoronoiInputSpec(CommandLineInputSpec):
    graph = traits.File(
        exists=True,
        desc='Cortical folds graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    hemi_cortex = traits.File(
        exists=True,
        desc='CSF+GREY Mask, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    sulci_voronoi = traits.File(
        exists=False,
        desc='Sulci Voronoi, Aims writable volume formats',
        position=2, mandatory=False, argstr='%s')


class SulcivoronoiOutputSpec(TraitedSpec):
    sulci_voronoi = traits.File(
        desc='Sulci Voronoi, Aims writable volume formats')


class Sulcivoronoi(BVCommand):
    input_spec = SulcivoronoiInputSpec
    output_spec = SulcivoronoiOutputSpec
    _cmd = 'Sulcivoronoi'

