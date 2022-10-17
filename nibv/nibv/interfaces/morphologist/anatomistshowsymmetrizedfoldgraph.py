from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowSymmetrizedFoldGraphInputSpec(CommandLineInputSpec):
    graph = traits.File(
        exists=True,
        desc='Cortical folds graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=1, mandatory=False, argstr='%s')
    white_mesh = traits.File(
        exists=True,
        desc='Hemisphere White Mesh, Anatomist mesh formats',
        position=2, mandatory=False, argstr='%s')


class AnatomistShowSymmetrizedFoldGraphOutputSpec(TraitedSpec):
    pass


class AnatomistShowSymmetrizedFoldGraph(BVCommand):
    input_spec = AnatomistShowSymmetrizedFoldGraphInputSpec
    output_spec = AnatomistShowSymmetrizedFoldGraphOutputSpec
    _cmd = 'AnatomistShowSymmetrizedFoldGraph'

