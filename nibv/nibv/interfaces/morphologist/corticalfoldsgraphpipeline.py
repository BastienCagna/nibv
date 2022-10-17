from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CorticalFoldsGraphPipelineInputSpec(CommandLineInputSpec):
    side = traits.Enum(
        "Left", "Right",
        usedefault=False,
        desc='Left,  Right',
        position=0, mandatory=False)
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    hemi_cortex = traits.File(
        exists=True,
        desc='CSF+GREY Mask, Aims readable volume formats',
        position=3, mandatory=False, argstr='%s')
    skeleton = traits.File(
        exists=False,
        desc='Cortex Skeleton, Aims writable volume formats',
        position=4, mandatory=False, argstr='%s')
    roots = traits.File(
        exists=False,
        desc='Cortex Catchment Bassins, Aims writable volume formats',
        position=5, mandatory=False, argstr='%s')
    graph = traits.File(
        exists=False,
        desc='Cortical folds graph,  Graph',
        position=7, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=8, mandatory=False, argstr='%s')
    talairach_transform = traits.File(
        exists=True,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=9, mandatory=False, argstr='%s')


class CorticalFoldsGraphPipelineOutputSpec(TraitedSpec):
    skeleton = traits.File(
        desc='Cortex Skeleton, Aims writable volume formats')
    roots = traits.File(
        desc='Cortex Catchment Bassins, Aims writable volume formats')
    graph = traits.File(
        desc='Cortical folds graph,  Graph')


class CorticalFoldsGraphPipeline(BVCommand):
    input_spec = CorticalFoldsGraphPipelineInputSpec
    output_spec = CorticalFoldsGraphPipelineOutputSpec
    _cmd = 'CorticalFoldsGraphPipeline'

