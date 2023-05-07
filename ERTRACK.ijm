dir1 = File.directory(); //directs Macro to read files in the same directory in which the macro is saved

setBatchMode("hide"); //windowless batch mode
run("Bio-Formats Macro Extensions"); //necessary to immport .nd2 files

list = getFileList(dir1); //loops through files in the directory where the macro is saved
  for (i=0; i<list.length; i++) {
    if (endsWith(list[i], ".nd2")) { 
    Ext.openImagePlus(dir1+list[i]);
title = getTitle();
      saveTitle = replace(title, ".nd2", ""); //temporarily renames the open image so the MOSAIC output doesn't contain .nd2
SingleParticleTracking(dir2);

}
}
function SingleParticleTracking() {
run("Particle Tracker 2D/3D", "radius=3 cutoff=0.005 per/abs=1 link=1 displacement=6 dynamics=Linear");
close("\\Others");
}
