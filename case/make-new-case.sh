dir_case=~/cases-argo
wmoid='5906503'
file_meteo=${dir_case}/meteo/meteo_AR${wmoid}.dat
file_tprof=${dir_case}/prof/temp_prof_AR${wmoid}.dat
file_sprof=${dir_case}/prof/salt_prof_AR${wmoid}.dat
ln -s ${file_meteo} ${wmoid}/meteo_file.dat
ln -s ${file_tprof} ${wmoid}/t_prof_file.dat
ln -s ${file_sprof} ${wmoid}/s_prof_file.dat
