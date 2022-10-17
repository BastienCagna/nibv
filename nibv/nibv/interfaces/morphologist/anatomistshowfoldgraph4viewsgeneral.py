from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowFoldGraph4viewsGeneralInputSpec(CommandLineInputSpec):
    right_graph = traits.File(
        exists=True,
        desc='Cortical folds graph, Graph and Data, requiredAttributes={side: right}',
        position=0, mandatory=False, argstr='%s')
    left_graph = traits.File(
        exists=True,
        desc='Cortical folds graph,  Graph and Data',
        position=1, mandatory=False, argstr='%s')
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=2, mandatory=False, argstr='%s')
    right_hemi_mesh = traits.File(
        exists=True,
        desc='Right Hemisphere Mesh,  Anatomist mesh formats',
        position=3, mandatory=False, argstr='%s')
    left_hemi_mesh = traits.File(
        exists=True,
        desc='Left Hemisphere Mesh,  Anatomist mesh formats',
        position=4, mandatory=False, argstr='%s')
    view_quaternionr_v = traits.String(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%s', mandatory=False)
    view_quaternionl_v = traits.String(
        None,
        usedefault=False,
        desc='',
        position=6, argstr='%s', mandatory=False)
    view_quaternionr_h = traits.String(
        None,
        usedefault=False,
        desc='',
        position=7, argstr='%s', mandatory=False)
    view_quaternionl_h = traits.String(
        None,
        usedefault=False,
        desc='',
        position=8, argstr='%s', mandatory=False)
    snapshot_size = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=12, argstr='%d', mandatory=False)
    output_image = traits.File(
        exists=False,
        desc='2D Image,  Aims image formats',
        position=13, mandatory=False, argstr='%s')
    output_image_1 = traits.File(
        exists=False,
        desc='2D Image,  Aims image formats',
        position=14, mandatory=False, argstr='%s')
    output_image_2 = traits.File(
        exists=False,
        desc='2D Image,  Aims image formats',
        position=15, mandatory=False, argstr='%s')
    output_image_3 = traits.File(
        exists=False,
        desc='2D Image,  Aims image formats',
        position=16, mandatory=False, argstr='%s')
    output_image_4 = traits.File(
        exists=False,
        desc='2D Image,  Aims image formats',
        position=17, mandatory=False, argstr='%s')


class AnatomistShowFoldGraph4viewsGeneralOutputSpec(TraitedSpec):
    output_image = traits.File(
        desc='2D Image,  Aims image formats')
    output_image_1 = traits.File(
        desc='2D Image,  Aims image formats')
    output_image_2 = traits.File(
        desc='2D Image,  Aims image formats')
    output_image_3 = traits.File(
        desc='2D Image,  Aims image formats')
    output_image_4 = traits.File(
        desc='2D Image,  Aims image formats')


class AnatomistShowFoldGraph4viewsGeneral(BVCommand):
    input_spec = AnatomistShowFoldGraph4viewsGeneralInputSpec
    output_spec = AnatomistShowFoldGraph4viewsGeneralOutputSpec
    _cmd = 'AnatomistShowFoldGraph4viewsGeneral'

