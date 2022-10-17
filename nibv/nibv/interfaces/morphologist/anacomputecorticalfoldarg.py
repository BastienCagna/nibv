from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaComputeCorticalFoldArgInputSpec(CommandLineInputSpec):
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
    left_hemi_cortex = traits.File(
        exists=False,
        desc='Left CSF+GREY Mask, Aims writable volume formats',
        position=4, mandatory=False, argstr='%s')
    right_hemi_cortex = traits.File(
        exists=False,
        desc='Right CSF+GREY Mask, Aims writable volume formats',
        position=5, mandatory=False, argstr='%s')
    lskeleton = traits.File(
        exists=False,
        desc='Left Cortex Skeleton, Aims writable volume formats',
        position=6, mandatory=False, argstr='%s')
    rskeleton = traits.File(
        exists=False,
        desc='Right Cortex Skeleton, Aims writable volume formats',
        position=7, mandatory=False, argstr='%s')
    lroots = traits.File(
        exists=False,
        desc='Left Cortex Catchment Bassins, Aims writable volume formats',
        position=8, mandatory=False, argstr='%s')
    rroots = traits.File(
        exists=False,
        desc='Right Cortex Catchment Bassins, Aims writable volume formats',
        position=9, mandatory=False, argstr='%s')
    lgraph = traits.File(
        exists=False,
        desc='Cortical folds graph, Graph, requiredAttributes={side: left, labelled: No,  graph_version: 3.0}',
        position=10, mandatory=False, argstr='%s')
    rgraph = traits.File(
        exists=False,
        desc='Cortical folds graph, Graph, requiredAttributes={side: right, labelled: No,   graph_version: 3.0}',
        position=11, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=12, mandatory=False, argstr='%s')
    compute_fold_meshes = traits.Enum(
        "Yes", "No",
        usedefault=False,
        desc='Yes,  No',
        position=13, mandatory=False)


class AnaComputeCorticalFoldArgOutputSpec(TraitedSpec):
    left_hemi_cortex = traits.File(
        desc='Left CSF+GREY Mask, Aims writable volume formats')
    right_hemi_cortex = traits.File(
        desc='Right CSF+GREY Mask, Aims writable volume formats')
    lskeleton = traits.File(
        desc='Left Cortex Skeleton, Aims writable volume formats')
    rskeleton = traits.File(
        desc='Right Cortex Skeleton, Aims writable volume formats')
    lroots = traits.File(
        desc='Left Cortex Catchment Bassins, Aims writable volume formats')
    rroots = traits.File(
        desc='Right Cortex Catchment Bassins, Aims writable volume formats')
    lgraph = traits.File(
        desc='Cortical folds graph, Graph, requiredAttributes={side: left, labelled: No,  graph_version: 3.0}')
    rgraph = traits.File(
        desc='Cortical folds graph, Graph, requiredAttributes={side: right, labelled: No,   graph_version: 3.0}')


class AnaComputeCorticalFoldArg(BVCommand):
    input_spec = AnaComputeCorticalFoldArgInputSpec
    output_spec = AnaComputeCorticalFoldArgOutputSpec
    _cmd = 'AnaComputeCorticalFoldArg'

