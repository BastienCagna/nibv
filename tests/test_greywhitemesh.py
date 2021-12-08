from nibv.interfaces.morphologist import GreyWhiteMesh

proc = GreyWhiteMesh()
proc.inputs.hemi_cortex = "/home/bastien/data/archi/t1-1mm-1/002/t1mri/default_acquisition/default_analysis/segmentation/Lcortex_002.nii.gz"
proc.inputs.white_mesh = "/home/bastien/data/test_greywhitemesh_L002.gii"

proc.run()
