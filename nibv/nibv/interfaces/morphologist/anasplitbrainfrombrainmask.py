from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaSplitBrainFromBrainMaskInputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=1, mandatory=False, argstr='%s')
    brain_mask = traits.File(
        exists=True,
        desc='T1 Brain Mask, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    use_template = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=3, mandatory=False)
    split_template = traits.File(
        exists=True,
        desc='Hemispheres Template, Aims readable volume formats',
        position=4, mandatory=False, argstr='%s')
    split_mask = traits.File(
        exists=False,
        desc='Split Brain Mask, Aims writable volume formats',
        position=5, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=6, mandatory=False, argstr='%s')


class AnaSplitBrainFromBrainMaskOutputSpec(TraitedSpec):
    split_mask = traits.File(
        desc='Split Brain Mask, Aims writable volume formats')


class AnaSplitBrainFromBrainMask(BVCommand):
    input_spec = AnaSplitBrainFromBrainMaskInputSpec
    output_spec = AnaSplitBrainFromBrainMaskOutputSpec
    _cmd = 'AnaSplitBrainFromBrainMask'

