from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CortexInputSpec(CommandLineInputSpec):
    side = traits.Enum(
        "Both", "Left", "Right",
        usedefault=False,
        desc='Both, Left,  Right',
        position=0, mandatory=False)
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=2, mandatory=False, argstr='%s')
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=3, mandatory=False, argstr='%s')
    use_ridges = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=4, mandatory=False)
    white_ridges = traits.File(
        exists=True,
        desc='T1 MRI White Matter Ridges, Aims readable volume formats',
        position=5, mandatory=False, argstr='%s')
    left_hemi_cortex = traits.File(
        exists=False,
        desc='Left CSF+GREY Mask, Aims writable volume formats',
        position=6, mandatory=False, argstr='%s')
    right_hemi_cortex = traits.File(
        exists=False,
        desc='Right CSF+GREY Mask, Aims writable volume formats',
        position=7, mandatory=False, argstr='%s')
    pressure = traits.Enum(
        "0", "25", "50", "75", "100", "125", "150",
        usedefault=False,
        desc='0, 25, 50, 75, 100, 125,  150',
        position=8, mandatory=False)


class CortexOutputSpec(TraitedSpec):
    left_hemi_cortex = traits.File(
        desc='Left CSF+GREY Mask, Aims writable volume formats')
    right_hemi_cortex = traits.File(
        desc='Right CSF+GREY Mask, Aims writable volume formats')


class Cortex(BVCommand):
    input_spec = CortexInputSpec
    output_spec = CortexOutputSpec
    _cmd = 'Cortex'

