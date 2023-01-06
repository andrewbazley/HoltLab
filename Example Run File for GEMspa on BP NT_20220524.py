import trajectory_analysis as tja

run_my_data=True

main_dir='/gpfs/data/holtlab/Andrew/20220524'
result_folder = main_dir+"/results_NT"
data_file=main_dir+'/NT_20220524.txt'

traj_an = tja.trajectory_analysis(data_file,
                                  result_folder,
                                  use_movie_metadata=False,
                                  uneven_time_steps=False,
                                  make_rainbow_tracks=False,
                                  limit_to_ROIs=False,
                                  measure_track_intensities=False,
                                  img_file_prefix='DNA_')

traj_an.time_step = 0.1033
traj_an.micron_per_px = 0.11
traj_an.ts_resolution=0.005
traj_an.intensity_radius=2

traj_an.output_filtered_tracks=False

traj_an.min_track_len_linfit = 11
traj_an.min_track_len_ensemble = 11

traj_an.tlag_cutoff_linfit = 10
traj_an.tlag_cutoff_ensemble = 10

traj_an.min_track_len_step_size = 3
traj_an.max_tlag_step_size = 3

traj_an.min_D_cutoff = 0
traj_an.max_D_cutoff = 2
traj_an.max_ss_rainbow_tracks = 1
traj_an.max_D_rainbow_tracks = 2

traj_an.line_width_rainbow_tracks=0.1
traj_an.time_coded_rainbow_tracks_by_frame=False

traj_an.write_params_to_log_file()

if(run_my_data):
    traj_an.calculate_msd_and_diffusion()
    traj_an.calculate_step_sizes_and_angles()

traj_an.make_plot() #label_order=['100_10pc',''])
traj_an.make_plot_combined_data() #label_order=conditions_order) # like matlab


traj_an.plot_alpha_D_heatmap()
traj_an.plot_msd_ensemble_by_group()
traj_an.plot_cos_theta_by_group()

#traj_an.plot_distribution_step_sizes(tlags=[1,])
#traj_an.plot_distribution_angles(tlags=[1,])
traj_an.plot_distribution_Deff(bin_size=0.01)
traj_an.plot_distribution_alpha(bin_size=0.01)
traj_an.plot_distribution_Deff(plot_type='', bin_size=0.1)
traj_an.plot_distribution_alpha(plot_type='', bin_size=0.1)

#if(limit_with_rois):
#    traj_an.make_plot_roi_area()
#if(measure_gem_intensities):
#    traj_an.make_plot_intensity()

print("Finished!")
