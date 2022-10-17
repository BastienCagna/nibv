from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowFoldGraphInputSpec(CommandLineInputSpec):
    graph = traits.File(
        exists=True,
        desc='Cortical folds graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=1, mandatory=False, argstr='%s')
    white_mesh = traits.File(
        exists=True,
        desc='Hemisphere White Mesh, Anatomist mesh formats,  requiredAttributes={modality: t1mri}',
        position=2, mandatory=False, argstr='%s')
    hemi_mesh = traits.File(
        exists=True,
        desc='Hemisphere Mesh,  Anatomist mesh formats',
        position=3, mandatory=False, argstr='%s')
    load_mri = traits.Enum(
        "Yes", "No",
        usedefault=False,
        desc='Yes,  No',
        position=4, mandatory=False)
    two_windows = traits.Enum(
        "Yes", "No",
        usedefault=False,
        desc='Yes,  No',
        position=5, mandatory=False)
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Anatomist volume formats',
        position=6, mandatory=False, argstr='%s')


class AnatomistShowFoldGraphOutputSpec(TraitedSpec):
    pass


class AnatomistShowFoldGraph(BVCommand):
    input_spec = AnatomistShowFoldGraphInputSpec
    output_spec = AnatomistShowFoldGraphOutputSpec
    _cmd = 'AnatomistShowFoldGraph'

