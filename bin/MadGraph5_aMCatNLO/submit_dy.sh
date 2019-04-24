#nohup ./submit_cmsconnect_gridpack_generation.sh PROCESSNAME CARDDIR > LOGNAME.debug 2>&1 &

##DY NLO cards
#cards/production/2017/13TeV/dyellell012j_5f_NLO_FXFX/dyellell012j_5f_NLO_FXFX_proc_card.dat
#cards/production/2017/13TeV/dyellell012j_5f_NLO_FXFX/dyellell012j_5f_NLO_FXFX_run_card.dat


nohup ./submit_cmsconnect_gridpack_generation.sh dyellell012j_5f_NLO_FXFX cards/production/2017/13TeV/dyellell012j_5f_NLO_FXFX > dyellell012j_5f_NLO_FXFX.debug 2>&1 &

##DY NLO 01j cards
#cards/examples/dyellell01j_5f_NLO_FXFX/dyellell01j_5f_NLO_FXFX_proc_card.dat
#cards/examples/dyellell01j_5f_NLO_FXFX/dyellell01j_5f_NLO_FXFX_run_card.dat
nohup ./submit_cmsconnect_gridpack_generation.sh dyellell01j_5f_NLO_FXFX cards/production/2017/13TeV/dyellell01j_5f_NLO_FXFX > dyellell01j_5f_NLO_FXFX.debug 2>&1 &



#DY LO cards
#cards/examples/dyellell01234j_5f_LO_MLM/dyellell01234j_5f_LO_MLM_proc_card.dat
#cards/examples/dyellell01234j_5f_LO_MLM/dyellell01234j_5f_LO_MLM_run_card.dat
nohup ./submit_cmsconnect_gridpack_generation.sh dyellell01234j_5f_LO_MLM cards/examples/dyellell01234j_5f_LO_MLM > dyellell01234j_5f_LO_MLM.debug 2>&1 &

#DY LO card pdfwgt ==T
#cards/examples/dyellell01234j_5f_LO_MLM_pdfwgt_T/dyellell01234j_5f_LO_MLM_pdfwgt_T_proc_card.dat
#cards/examples/dyellell01234j_5f_LO_MLM_pdfwgt_T/dyellell01234j_5f_LO_MLM_pdfwgt_T_run_card.dat
nohup ./submit_cmsconnect_gridpack_generation.sh dyellell01234j_5f_LO_MLM_pdfwgt_T cards/examples/dyellell01234j_5f_LO_MLM_pdfwgt_T > dyellell01234j_5f_LO_MLM_pdfwgt_T.debug 2>&1 &

#DY LO 012j cards
#cards/examples/dyellell012j_5f_LO_MLM/dyellell012j_5f_LO_MLM_proc_card.dat
#cards/examples/dyellell012j_5f_LO_MLM/dyellell012j_5f_LO_MLM_run_card.dat

nohup ./submit_cmsconnect_gridpack_generation.sh dyellell012j_5f_LO_MLM cards/examples/dyellell012j_5f_LO_MLM > dyellell012j_5f_LO_MLM.debug 2>&1 &

#DY LO 012j cards pdfwgt ==T
#cards/examples/dyellell012j_5f_LO_MLM_pdfwgt_T/dyellell012j_5f_LO_MLM_pdfwgt_T_proc_card.dat
#cards/examples/dyellell012j_5f_LO_MLM_pdfwgt_T/dyellell012j_5f_LO_MLM_pdfwgt_T_run_card.dat
nohup ./submit_cmsconnect_gridpack_generation.sh dyellell012j_5f_LO_MLM_pdfwgt_T cards/examples/dyellell012j_5f_LO_MLM_pdfwgt_T/ > dyellell012j_5f_LO_MLM_pdfwgt_T.debug 2>&1 &