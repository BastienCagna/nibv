from nibv.interfaces.morphologist import AnatomistShowGraph

proc = AnatomistShowGraph()
proc.inputs.graph = "/home/bastien/data/archi/t1-1mm-1/002/t1mri/default_acquisition/default_analysis/folds/3.3/session1_manual/L002_session1_manual.arg"
proc.inputs.nomenclature = "/home/bastien/soft/brainvisa/brainvisa/src/brainvisa-share/master/nomenclature/hierarchy/sulcal_root_colors.hie"
proc.inputs.anatomy = "/home/bastien/data/archi/t1-1mm-1/002/t1mri/default_acquisition/default_analysis/nobias_002.nii.gz"
proc.inputs.head_mesh = "/home/bastien/data/archi/t1-1mm-1/002/t1mri/default_acquisition/default_analysis/segmentation/mesh/002_Lwhite.gii"

print(proc.cmdline)
proc.run()
