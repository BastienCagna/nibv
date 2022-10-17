from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulciskeletonInputSpec(CommandLineInputSpec):
    hemi_cortex = traits.File(
        exists=True,
        desc='CSF+GREY Mask, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    grey_white = traits.File(
        exists=True,
        desc='Grey White Mask, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    t1mri_nobias = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    skeleton = traits.File(
        exists=False,
        desc='Cortex Skeleton, Aims writable volume formats',
        position=3, mandatory=False, argstr='%s')
    roots = traits.File(
        exists=False,
        desc='Cortex Catchment Bassins, Aims writable volume formats',
        position=4, mandatory=False, argstr='%s')
    version = traits.Enum(
        "1", "2",
        usedefault=False,
        desc='1,  2',
        position=5, mandatory=False)
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=6, mandatory=False)


class SulciskeletonOutputSpec(TraitedSpec):
    skeleton = traits.File(
        desc='Cortex Skeleton, Aims writable volume formats')
    roots = traits.File(
        desc='Cortex Catchment Bassins, Aims writable volume formats')


class Sulciskeleton(BVCommand):
    input_spec = SulciskeletonInputSpec
    output_spec = SulciskeletonOutputSpec
    _cmd = 'Sulciskeleton'

