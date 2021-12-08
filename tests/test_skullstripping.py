from nibv.interfaces.morphologist import Skullstripping

proc = Skullstripping()
proc.inputs.t1mri = "/home/bastien/data/archi/t1-1mm-1/002/t1mri/default_acquisition/default_analysis/nobias_002.nii.gz"
proc.inputs.brain_mask = "/home/bastien/data/archi/t1-1mm-1/002/t1mri/default_acquisition/default_analysis/segmentation/"
proc.inputs.skul_stripped = ""
