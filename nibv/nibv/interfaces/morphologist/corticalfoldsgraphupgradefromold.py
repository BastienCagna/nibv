from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CorticalFoldsGraphUpgradeFromOldInputSpec(CommandLineInputSpec):
    old_graph = traits.File(
        exists=True,
        desc='Cortical folds graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    skeleton = traits.File(
        exists=True,
        desc='Cortex Skeleton,  aims readable Volume Formats',
        position=1, mandatory=False, argstr='%s')
    graph = traits.File(
        exists=False,
        desc='Cortical folds graph,  Graph',
        position=3, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=4, mandatory=False, argstr='%s')
    talairach_transform = traits.File(
        exists=True,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=5, mandatory=False, argstr='%s')
    compute_fold_meshes = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=6, mandatory=False)
    allow_multithreading = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=7, mandatory=False)


class CorticalFoldsGraphUpgradeFromOldOutputSpec(TraitedSpec):
    graph = traits.File(
        desc='Cortical folds graph,  Graph')


class CorticalFoldsGraphUpgradeFromOld(BVCommand):
    input_spec = CorticalFoldsGraphUpgradeFromOldInputSpec
    output_spec = CorticalFoldsGraphUpgradeFromOldOutputSpec
    _cmd = 'CorticalFoldsGraphUpgradeFromOld'

