arg=getArgument();
dir1 = "/gpfs/data/holtlab/Andrew/"+"arg"
setBatchMode("hide");
run("Bio-Formats Macro Extensions");

list = getFileList(dir1);
  for (i=0; i<list.length; i++) {
    if (endsWith(list[i], ".nd2")) { 
    Ext.openImagePlus(dir1+list[i]);
    rename(replace(getInfo("image.filename"),".nd2",""));
		SingleParticleTracking();
}
}
function SingleParticleTracking() {
run("Particle Tracker 2D/3D", "radius=3 cutoff=0.005 per/abs=1 link=1 displacement=6 dynamics=Linear");
run("Close All");
}
