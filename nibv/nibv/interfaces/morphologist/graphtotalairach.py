from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class GraphToTalairachInputSpec(CommandLineInputSpec):
    read = traits.File(
        exists=True,
        desc='Graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    write = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=1, mandatory=False, argstr='%s')


class GraphToTalairachOutputSpec(TraitedSpec):
    write = traits.File(
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix')


class GraphToTalairach(BVCommand):
    input_spec = GraphToTalairachInputSpec
    output_spec = GraphToTalairachOutputSpec
    _cmd = 'GraphToTalairach'

