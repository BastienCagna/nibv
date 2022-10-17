from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class LocalizeCoordTalairachInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    talairach_transform = traits.File(
        exists=True,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=1, mandatory=False, argstr='%s')
    localised = traits.File(
        exists=False,
        desc='3D Volume,  aims Writable Volume Formats',
        position=2, mandatory=False, argstr='%s')


class LocalizeCoordTalairachOutputSpec(TraitedSpec):
    localised = traits.File(
        desc='3D Volume,  aims Writable Volume Formats')


class LocalizeCoordTalairach(BVCommand):
    input_spec = LocalizeCoordTalairachInputSpec
    output_spec = LocalizeCoordTalairachOutputSpec
    _cmd = 'LocalizeCoordTalairach'

