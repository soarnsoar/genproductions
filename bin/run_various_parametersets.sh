#!/bin/bash






run_ajob(){
    
##variations##
    max_iter=$1
    max_event=$2
    min_event=$3
    security=$4
##############


#(0) copy Madgraph5 directory
    STARTDIR=`pwd`
    CASEDIR=MadGraph5_aMCatNLO_${max_iter}_${max_event}_${min_event}_${security}
    echo "####Copy MG5 directiry####"
    cp -r MadGraph5_aMCatNLO_template $CASEDIR
    cd $CASEDIR
    
#(1) change patch file's parameterset
    echo "###change patch file's parameterset## "
    rm -rf patches
    cp -r patches_template patches
    echo "##enter patches dir##"
    pushd patches 
    find . -name "0017-fix-event_in_iter-for-long-runtime.patch" | xargs perl -pi -e s/_MAX_ITER_/${max_iter}/g
    find . -name "0017-fix-event_in_iter-for-long-runtime.patch" | xargs perl -pi -e s/_MAX_EVENT_/${max_event}/g
    find . -name "0017-fix-event_in_iter-for-long-runtime.patch" | xargs perl -pi -e s/_MIN_EVENT_/${min_event}/g
    find . -name "0017-fix-event_in_iter-for-long-runtime.patch" | xargs perl -pi -e s/_SECURITY_/${security}/g
    
    popd
    echo "##out from patches dir"
#(2) copy run/proc cards
    echo "##copy run/proc cards##"
    mkdir -p cards/dyellell012j_5f_NLO_FXFX_validation/false_pdfwgt/perform_test
    pushd cards/dyellell012j_5f_NLO_FXFX_validation/false_pdfwgt/perform_test
    echo "##in perform_test dir##"
    jobname=${max_iter}_${max_event}_${min_event}_${security}
    echo "JOBNAME="$jobname
    rm -rf $jobname
    cp -r template/ $jobname/
    carddir=cards/dyellell012j_5f_NLO_FXFX_validation/false_pdfwgt/perform_test/$jobname
    cd $jobname

    
    mv dyellell01234j_5f_LO_MLM_mg261_false_pdfwgt_template_proc_card.dat dyellell01234j_5f_LO_MLM_mg261_false_pdfwgt_${jobname}_proc_card.dat
    mv dyellell01234j_5f_LO_MLM_mg261_false_pdfwgt_template_run_card.dat dyellell01234j_5f_LO_MLM_mg261_false_pdfwgt_${jobname}_run_card.dat
    find . -name "dyellell01234j_5f_LO_MLM_mg261_false_pdfwgt_${jobname}_proc_card.dat" | xargs perl -pi -e s/template/${jobname}/g
    
    cd -
    echo "##OUT OF carddir"
    echo "carddir="$carddir
    popd
    
    echo "##genprodcution mg dir##"
#(3) run gridpacks
    #nohup ./submit_cmsconnect_gridpack_generation.sh PROCESSNAME CARDDIR > LOGNAME.debug 2>&1 &
    echo "##Submit the job to queue##"
    echo "1st argument=dyellell01234j_5f_LO_MLM_mg261_false_pdfwgt_${jobname}"
    echo "2nd argument=$carddir"
    ##here change log
    source submit_condor_gridpack_generation.sh dyellell01234j_5f_LO_MLM_mg261_false_pdfwgt_${jobname} $carddir &> dyellell01234j_5f_LO_MLM_mg261_false_pdfwgt_${jobname}.debug &
    


    echo "@@@@SUBMITSSION FIN.@@@@"

    cd $STARTDIR
}


##Main##
#    max_iter=$1
 #   max_event=$2
  #  min_event=$3
   # security=$4

ARR_SECURITY=( 1.0 1.2 )
for sec_i in ${ARR_SECURITY[@]};do

##Olivier's example
    run_ajob 13 4000 500 $sec_i
    
##small max_iter
    run_ajob 10 4000 500 $sec_i
##large max_iter
    run_ajob 15 4000 500 $sec_i
    
##small min_event
    run_ajob 13 4000 100 $sec_i
##large min_event
    run_ajob 13 4000 2000 $sec_i
    
##small max_event
    run_ajob 13 2000 500 $sec_i
##large max_event 
    run_ajob 13 7000 500 $sec_i
    
done