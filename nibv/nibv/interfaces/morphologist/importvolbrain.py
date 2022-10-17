from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ImportVolbrainInputSpec(CommandLineInputSpec):
    volbrain_mni_zip = traits.File(
        exists=True,
        desc='Any Type, ZIP file, section=inputs',
        position=0, mandatory=False, argstr='%s')
    volbrain_native_zip = traits.File(
        exists=True,
        desc='Any Type, ZIP file, section=inputs',
        position=1, mandatory=False, argstr='%s')
    subject = traits.File(
        exists=True,
        desc='Subject, Directory, section=inputs',
        position=2, mandatory=False, argstr='%s')
    acquisition = traits.String(
        None,
        usedefault=False,
        desc='section=inputs',
        position=3, argstr='%s', mandatory=False)
    check_subject_name_in_zipfile = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='section=inputs',
        position=4, mandatory=False)
    report_csv = traits.File(
        exists=False,
        desc='Analysis Report, CSV file, requiredAttributes={modality: volBrain}, section=report',
        position=5, mandatory=False, argstr='%s')
    report_pdf = traits.File(
        exists=False,
        desc='Analysis Report, PDF file, requiredAttributes={modality: volBrain}, section=report',
        position=6, mandatory=False, argstr='%s')
    mni_lab = traits.File(
        exists=False,
        desc='Subcortical labels, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni',
        position=7, mandatory=False, argstr='%s')
    mni_hemi = traits.File(
        exists=False,
        desc='Split Brain Mask, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni',
        position=8, mandatory=False, argstr='%s')
    mni_crisp = traits.File(
        exists=False,
        desc='Intracranial labels, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni',
        position=9, mandatory=False, argstr='%s')
    mni_mask = traits.File(
        exists=False,
        desc='Intracranial mask, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni',
        position=10, mandatory=False, argstr='%s')
    mni_wm = traits.File(
        exists=False,
        desc='tissue probability map, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni, tissue_class: white}, section=outputs_mni',
        position=11, mandatory=False, argstr='%s')
    mni_gm = traits.File(
        exists=False,
        desc='tissue probability map, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni, tissue_class: grey}, section=outputs_mni',
        position=12, mandatory=False, argstr='%s')
    mni_csf = traits.File(
        exists=False,
        desc='tissue probability map, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni, tissue_class: csf}, section=outputs_mni',
        position=13, mandatory=False, argstr='%s')
    mni_normalised = traits.File(
        exists=False,
        desc='T1 MRI Denoised and Bias Corrected, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni',
        position=14, mandatory=False, argstr='%s')
    mni_readme = traits.File(
        exists=False,
        desc='Text file, PDF file, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni',
        position=15, mandatory=False, argstr='%s')
    affine_transformation = traits.File(
        exists=False,
        desc='Transformation, Text file, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni',
        position=16, mandatory=False, argstr='%s')
    native_lab = traits.File(
        exists=False,
        desc='Subcortical labels, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native',
        position=17, mandatory=False, argstr='%s')
    native_hemi = traits.File(
        exists=False,
        desc='Split Brain Mask, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native',
        position=18, mandatory=False, argstr='%s')
    native_crisp = traits.File(
        exists=False,
        desc='Intracranial labels, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native',
        position=19, mandatory=False, argstr='%s')
    native_mask = traits.File(
        exists=False,
        desc='Intracranial mask, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native',
        position=20, mandatory=False, argstr='%s')
    native_filtered = traits.File(
        exists=False,
        desc='T1 MRI Denoised, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native',
        position=21, mandatory=False, argstr='%s')
    native_normalised = traits.File(
        exists=False,
        desc='T1 MRI Denoised and Bias Corrected, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native',
        position=22, mandatory=False, argstr='%s')
    native_readme = traits.File(
        exists=False,
        desc='Text file, PDF file, requiredAttributes={modality: volBrain, space: native}, section=outputs_native',
        position=23, mandatory=False, argstr='%s')


class ImportVolbrainOutputSpec(TraitedSpec):
    report_csv = traits.File(
        desc='Analysis Report, CSV file, requiredAttributes={modality: volBrain}, section=report')
    report_pdf = traits.File(
        desc='Analysis Report, PDF file, requiredAttributes={modality: volBrain}, section=report')
    mni_lab = traits.File(
        desc='Subcortical labels, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni')
    mni_hemi = traits.File(
        desc='Split Brain Mask, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni')
    mni_crisp = traits.File(
        desc='Intracranial labels, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni')
    mni_mask = traits.File(
        desc='Intracranial mask, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni')
    mni_wm = traits.File(
        desc='tissue probability map, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni, tissue_class: white}, section=outputs_mni')
    mni_gm = traits.File(
        desc='tissue probability map, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni, tissue_class: grey}, section=outputs_mni')
    mni_csf = traits.File(
        desc='tissue probability map, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni, tissue_class: csf}, section=outputs_mni')
    mni_normalised = traits.File(
        desc='T1 MRI Denoised and Bias Corrected, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni')
    mni_readme = traits.File(
        desc='Text file, PDF file, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni')
    affine_transformation = traits.File(
        desc='Transformation, Text file, requiredAttributes={modality: volBrain, space: mni}, section=outputs_mni')
    native_lab = traits.File(
        desc='Subcortical labels, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native')
    native_hemi = traits.File(
        desc='Split Brain Mask, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native')
    native_crisp = traits.File(
        desc='Intracranial labels, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native')
    native_mask = traits.File(
        desc='Intracranial mask, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native')
    native_filtered = traits.File(
        desc='T1 MRI Denoised, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native')
    native_normalised = traits.File(
        desc='T1 MRI Denoised and Bias Corrected, gz compressed NIFTI-1 image, requiredAttributes={modality: volBrain, space: native}, section=outputs_native')
    native_readme = traits.File(
        desc='Text file, PDF file, requiredAttributes={modality: volBrain, space: native}, section=outputs_native')


class ImportVolbrain(BVCommand):
    input_spec = ImportVolbrainInputSpec
    output_spec = ImportVolbrainOutputSpec
    _cmd = 'ImportVolbrain'

