from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class GreyWhiteTopologyInputSpec(CommandLineInputSpec):
    grey_white = traits.File(
        exists=True,
        desc='Grey White Mask, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    t1mri_nobias = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=2, mandatory=False, argstr='%s')
    hemi_cortex = traits.File(
        exists=False,
        desc='CSF+GREY Mask, Aims writable volume formats',
        position=3, mandatory=False, argstr='%s')
    version = traits.Enum(
        "1", "2",
        usedefault=False,
        desc='1,  2',
        position=4, mandatory=False)
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=5, mandatory=False)


class GreyWhiteTopologyOutputSpec(TraitedSpec):
    hemi_cortex = traits.File(
        desc='CSF+GREY Mask, Aims writable volume formats')


class GreyWhiteTopology(BVCommand):
    input_spec = GreyWhiteTopologyInputSpec
    output_spec = GreyWhiteTopologyOutputSpec
    _cmd = 'GreyWhiteTopology'

