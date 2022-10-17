from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class VipSplitBrainInputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    use_template = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=1, mandatory=False)
    split_template = traits.File(
        exists=True,
        desc='Hemispheres Template, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    brain_mask = traits.File(
        exists=True,
        desc='T1 Brain Mask, Aims readable volume formats',
        position=3, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=4, mandatory=False, argstr='%s')
    split_mask = traits.File(
        exists=False,
        desc='Split Brain Mask, Aims writable volume formats',
        position=5, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=6, mandatory=False, argstr='%s')
    white_algo = traits.Enum(
        "r", "c", "b", "t",
        usedefault=False,
        desc='r, c, b,  t',
        position=7, mandatory=False)
    mult_factor = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=8, argstr='%f', mandatory=False)
    bary_factor = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=9, argstr='%f', mandatory=False)
    white_threshold = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=10, argstr='%d', mandatory=False)
    initial_erosion = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=11, argstr='%f', mandatory=False)
    cc_min_size = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=12, argstr='%d', mandatory=False)


class VipSplitBrainOutputSpec(TraitedSpec):
    split_mask = traits.File(
        desc='Split Brain Mask, Aims writable volume formats')


class VipSplitBrain(BVCommand):
    input_spec = VipSplitBrainInputSpec
    output_spec = VipSplitBrainOutputSpec
    _cmd = 'VipSplitBrain'

