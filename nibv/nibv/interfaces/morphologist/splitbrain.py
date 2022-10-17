from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SplitBrainInputSpec(CommandLineInputSpec):
    brain_mask = traits.File(
        exists=True,
        desc='T1 Brain Mask, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    t1mri_nobias = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=2, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
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
    use_template = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=6, mandatory=False)
    split_template = traits.File(
        exists=True,
        desc='Hemispheres Template, Aims readable volume formats',
        position=7, mandatory=False, argstr='%s')
    mode = traits.Enum(
        "Watershed",
        usedefault=False,
        desc='Watershed',
        position=8, mandatory=False)
    variant = traits.Enum(
        "regularized", "GW Barycentre", "WM Standard Deviation",
        usedefault=False,
        desc='regularized, GW Barycentre,  WM Standard Deviation',
        position=9, mandatory=False)
    bary_factor = traits.Enum(
        "0.9", "0.8", "0.7", "0.6", "0.5", "0.4", "0.3", "0.2", "0.1",
        usedefault=False,
        desc='0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2,  0.1',
        position=10, mandatory=False)
    mult_factor = traits.Enum(
        "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4",
        usedefault=False,
        desc='0.5, 1, 1.5, 2, 2.5, 3, 3.5,  4',
        position=11, mandatory=False)
    initial_erosion = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=12, argstr='%f', mandatory=False)
    cc_min_size = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=13, argstr='%d', mandatory=False)
    split_brain = traits.File(
        exists=False,
        desc='Split Brain Mask, Aims writable volume formats',
        position=14, mandatory=False, argstr='%s')
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=15, mandatory=False)


class SplitBrainOutputSpec(TraitedSpec):
    split_brain = traits.File(
        desc='Split Brain Mask, Aims writable volume formats')


class SplitBrain(BVCommand):
    input_spec = SplitBrainInputSpec
    output_spec = SplitBrainOutputSpec
    _cmd = 'SplitBrain'

