from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaValidateAllInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    validation_total = traits.Enum(
        "Visualise", "Lock", "Unlock", "Itemwise",
        usedefault=False,
        desc='Visualise, Lock, Unlock,  Itemwise',
        position=1, mandatory=False)
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    validation_mri_corrected = traits.Enum(
        "Nothing", "Visualise", "Lock", "Unlock",
        usedefault=False,
        desc='Nothing, Visualise, Lock,  Unlock',
        position=3, mandatory=False)
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=4, mandatory=False, argstr='%s')
    validation_histo_analysis = traits.Enum(
        "Nothing", "Visualise", "Lock", "Unlock",
        usedefault=False,
        desc='Nothing, Visualise, Lock,  Unlock',
        position=5, mandatory=False)
    brain_mask = traits.File(
        exists=True,
        desc='T1 Brain Mask, Aims readable volume formats',
        position=6, mandatory=False, argstr='%s')
    validation_brain_mask = traits.Enum(
        "Nothing", "Visualise", "Lock", "Unlock",
        usedefault=False,
        desc='Nothing, Visualise, Lock,  Unlock',
        position=7, mandatory=False)
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=8, mandatory=False, argstr='%s')
    validation_split_mask = traits.Enum(
        "Nothing", "Visualise", "Lock", "Unlock",
        usedefault=False,
        desc='Nothing, Visualise, Lock,  Unlock',
        position=9, mandatory=False)
    left_hemi_mesh = traits.File(
        exists=True,
        desc='Left Hemisphere Mesh, Aims mesh formats',
        position=10, mandatory=False, argstr='%s')
    validation_left_hemi_mesh = traits.Enum(
        "Nothing", "Visualise", "Lock", "Unlock",
        usedefault=False,
        desc='Nothing, Visualise, Lock,  Unlock',
        position=11, mandatory=False)
    right_hemi_mesh = traits.File(
        exists=True,
        desc='Right Hemisphere Mesh, Aims mesh formats',
        position=12, mandatory=False, argstr='%s')
    validation_right_hemi_mesh = traits.Enum(
        "Nothing", "Visualise", "Lock", "Unlock",
        usedefault=False,
        desc='Nothing, Visualise, Lock,  Unlock',
        position=13, mandatory=False)
    left_white_mesh = traits.File(
        exists=True,
        desc='Left Hemisphere White Mesh, Aims mesh formats',
        position=14, mandatory=False, argstr='%s')
    validation_left_white_mesh = traits.Enum(
        "Nothing", "Visualise", "Lock", "Unlock",
        usedefault=False,
        desc='Nothing, Visualise, Lock,  Unlock',
        position=15, mandatory=False)
    right_white_mesh = traits.File(
        exists=True,
        desc='Right Hemisphere White Mesh, Aims mesh formats',
        position=16, mandatory=False, argstr='%s')
    validation_right_white_mesh = traits.Enum(
        "Nothing", "Visualise", "Lock", "Unlock",
        usedefault=False,
        desc='Nothing, Visualise, Lock,  Unlock',
        position=17, mandatory=False)


class AnaValidateAllOutputSpec(TraitedSpec):
    pass


class AnaValidateAll(BVCommand):
    input_spec = AnaValidateAllInputSpec
    output_spec = AnaValidateAllOutputSpec
    _cmd = 'AnaValidateAll'

