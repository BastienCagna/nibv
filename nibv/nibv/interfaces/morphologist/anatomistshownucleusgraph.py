from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowNucleusGraphInputSpec(CommandLineInputSpec):
    nucleus_graph = traits.File(
        exists=True,
        desc='Nucleus graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    nucleus_nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=1, mandatory=False, argstr='%s')
    load_mri = traits.Enum(
        "Yes", "No",
        usedefault=False,
        desc='Yes,  No',
        position=2, mandatory=False)
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Anatomist volume formats',
        position=3, mandatory=False, argstr='%s')
    load_sulcus = traits.Enum(
        "Both", "Left", "Right", "No",
        usedefault=False,
        desc='Both, Left, Right,  No',
        position=4, mandatory=False)
    load_hemis = traits.Enum(
        "Yes", "No",
        usedefault=False,
        desc='Yes,  No',
        position=5, mandatory=False)
    lfold_graph = traits.File(
        exists=True,
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={side: left, labelled: Yes, manually_labelled: Yes}',
        position=6, mandatory=False, argstr='%s')
    rfold_graph = traits.File(
        exists=True,
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={side: right, labelled: Yes, manually_labelled: Yes}',
        position=7, mandatory=False, argstr='%s')
    fold_nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=8, mandatory=False, argstr='%s')
    lhemi_mesh = traits.File(
        exists=True,
        desc='Left Hemisphere Mesh, Anatomist mesh formats',
        position=9, mandatory=False, argstr='%s')
    rhemi_mesh = traits.File(
        exists=True,
        desc='Right Hemisphere Mesh, Anatomist mesh formats',
        position=10, mandatory=False, argstr='%s')


class AnatomistShowNucleusGraphOutputSpec(TraitedSpec):
    pass


class AnatomistShowNucleusGraph(BVCommand):
    input_spec = AnatomistShowNucleusGraphInputSpec
    output_spec = AnatomistShowNucleusGraphOutputSpec
    _cmd = 'AnatomistShowNucleusGraph'

