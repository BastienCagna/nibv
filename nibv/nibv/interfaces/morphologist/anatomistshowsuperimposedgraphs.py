from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowSuperimposedGraphsInputSpec(CommandLineInputSpec):
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=1, mandatory=False, argstr='%s')
    hemi_mesh = traits.File(
        exists=True,
        desc='Hemisphere Mesh,  Anatomist mesh formats',
        position=2, mandatory=False, argstr='%s')


class AnatomistShowSuperimposedGraphsOutputSpec(TraitedSpec):
    pass


class AnatomistShowSuperimposedGraphs(BVCommand):
    input_spec = AnatomistShowSuperimposedGraphsInputSpec
    output_spec = AnatomistShowSuperimposedGraphsOutputSpec
    _cmd = 'AnatomistShowSuperimposedGraphs'

