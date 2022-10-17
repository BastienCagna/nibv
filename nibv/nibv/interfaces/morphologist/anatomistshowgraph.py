from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowGraphInputSpec(CommandLineInputSpec):
    graph = traits.File(
        exists=True,
        desc='Data Graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=1, mandatory=False, argstr='%s')
    anatomy = traits.File(
        exists=True,
        desc='T1 MRI,  anatomist Volume Formats',
        position=2, mandatory=False, argstr='%s')
    head_mesh = traits.File(
        exists=True,
        desc='Head mesh, anatomist Mesh Formats',
        position=4, mandatory=False, argstr='%s')


class AnatomistShowGraphOutputSpec(TraitedSpec):
    pass


class AnatomistShowGraph(BVCommand):
    input_spec = AnatomistShowGraphInputSpec
    output_spec = AnatomistShowGraphOutputSpec
    _cmd = 'AnatomistShowGraph'

