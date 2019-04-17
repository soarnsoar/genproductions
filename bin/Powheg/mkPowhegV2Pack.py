
import os

UseCondor = True


# Definition of the input parameters:
# (1) -p grid production stage [f]  (one go)
# (2) -i intput card name [powheg.input]
# (3) -m process name (process defined in POWHEG)
# (4) -f working folder [my_ggH]
# (5) -q batch queue name (run locally if not specified)
# (6) -n the number of events to run



########### All

massGrid = {
            'VBfHWWlnuqq': [],
            #'VBFhWWlnuqq': [125, 200, 250, 300, 350, 400, 450, 500, 550,600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000, 4000, 5000],
	    'VBfHWW2L2Nu': [],
	    #'VBfHWW2L2Nu': [115, 120, 124, 125, 126, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 190,200,210,230,270, 300,350,450,500,550,600,650,700,800,900,1000,1500,2000,2500,3000],
	    'ggHToWW2L2Nu': [400,750],
	    #'ggHToWW2L2Nu': [115, 120, 124, 125, 126, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 190, 300, 650],
	    'ggHToWWlnuqq': [],#[115, 120,124,126,130,135,140,145,150,155,160,165,170,175,180,190,200],
	    #'ggHToWWlnuqq': [4000, 5000],
            'ggZHWW': [],
	    'HZJ': [],
            }


##################
#  400 <batch> Exited
##################
#massGrid = {'VBFhWWlnuqq': [125, 200, 250, 300, 350, 450, 500, 550,600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000]
#            }

#massGrid = {'VBFhWWlnuqq': [400]
#            }

if UseCondor == True :
  print "Using Condor"
  # HWminusJ_HToWW_M125_13TeV_powheg_pythia8_TuneCP5
  #cmd = 'python ./run_pwg_condor.py -p f -i  production/2017/13TeV/Higgs/WminusHJ_HanythingJ_NNPDF31_13TeV/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vinclusive.input -g ../JHUGen/cards/decay/WWany.input -m HWJ -f HWminusJ_HWWany_NNPDF31_13TeV_M125_Vinc_JHU724 '+' -q workday -n 10'
  #print cmd
  #os.system(cmd)
  #cmd = 'python ./run_pwg_condor.py -p f -i  production/2017/13TeV/Higgs/WplusHJ_HanythingJ_NNPDF31_13TeV/HWplusJ_HanythingJ_NNPDF31_13TeV_M125_Vinclusive.input -g ../JHUGen/cards/decay/WWany.input -m HWJ -f HWplusJ_HWWany_NNPDF31_13TeV_M125_Vinc_JHU724 '+' -q tomorrow -n 10'
  #print cmd
  #os.system(cmd)

#########################
# one go
#########################

  for mass in massGrid['VBfHWW2L2Nu']:
      print mass
      if mass < 200 :
          cmd = 'python ./run_pwg_condor.py -p f -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m VBF_H -f VBfHWW2L2Nu_jhu'+str(mass)+' -q tomorrow -n 30'
      else :
          cmd = 'python ./run_pwg_condor.py -p f -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m VBF_H -f VBfHWW2L2Nu_jhu'+str(mass)+' -q tomorrow -n 30'
  
      print cmd
      os.system(cmd)
#
  for mass in massGrid['VBfHWWlnuqq']:
      print mass
      if mass < 200 :
          cmd = 'python ./run_pwg_condor.py -p f -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m VBF_H -f VBfHWWlnuqq_jhu'+str(mass)+' -q tomorrow -n 30'
      else :
          cmd = 'python ./run_pwg_condor.py -p f -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m VBF_H -f VBfHWWlnuqq_jhu'+str(mass)+' -q tomorrow -n 30'
  
      print cmd
      os.system(cmd)

  for mass in massGrid['ggHToWW2L2Nu']:
      print mass
      if mass < 200 :
          cmd = 'python ./run_pwg_condor.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m gg_H_quark-mass-effects -f gghWW2l2nu_jhu'+str(mass)+' -q tomorrow -n 30'
      else :
          cmd = 'python ./run_pwg_condor.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m gg_H_quark-mass-effects -f gghWW2l2nu_jhu'+str(mass)+' -q tomorrow -n 30'
  
      print cmd
      os.system(cmd)

  for mass in massGrid['ggHToWWlnuqq']:
      print mass
      if mass < 200 :
          cmd = 'python ./run_pwg_condor.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m gg_H_quark-mass-effects -f gghWWlnuqq_jhu'+str(mass)+' -q tomorrow -n 30'
      else :
          cmd = 'python ./run_pwg_condor.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m gg_H_quark-mass-effects -f gghWWlnuqq_jhu'+str(mass)+' -q tomorrow -n 30'
  
      print cmd
      os.system(cmd)

  for mass in massGrid['HZJ']:
    
    print mass
     #HToWW
    cmd = 'python ./run_pwg_condor.py -p f -i production/2017/13TeV/Higgs/HZJ_HanythingJ_NNPDF31_13TeV/HZJ_HanythingJ_NNPDF31_13TeV_M'+str(mass)+'_Vleptonic.input -g ../JHUGen/cards/decay/WWany.input  -m HZJ -f HZJ_HWWany_NNPDF31_13TeV_'+str(mass)+'_Vleptonic_JHU726 '+' -q tomorrow -n 10'
    print cmd
    os.system(cmd)

  for mass in massGrid['HZJ']:
  
    # HToWW
    cmd = 'python ./run_pwg_condor.py -p f -i production/2017/13TeV/Higgs/ggHZ_HanythingJ_NNPDF31_13TeV/ggHZ_HanythingJ_NNPDF31_13TeV_M'+str(mass)+'_Vleptonic.input -g ../JHUGen/cards/decay/WWany.input  -m ggHZ -f ggHZ_HWWany_NNPDF31_13TeV_'+str(mass)+'_Vleptonic_JHU726 '+' -q tomorrow -n 10'
    print cmd
    os.system(cmd)

else:
  print "Not using Condor"



#####################################################
# Gridpack production with multiple processors
#####################################################

######################################
# Step1: Compiling the POWHEG source
######################################
#for mass in massGrid['VBFhWWlnuqq']:
#    print mass
#    if mass < 300 :
#        cmd = 'python ./run_pwg.py -p 0 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m VBF_H -f vbfhWWlnuqq'+str(mass)
#    else :
#        cmd = 'python ./run_pwg.py -p 0 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m VBF_H -f vbfhWWlnuqq'+str(mass)
#
#    print cmd
#    os.system(cmd)
#
###############################################################
# Step2: Producting grids with 3 separate internal stages
################################################################
###########
# step 1-1  p1 x1,2,3,4,5 8nh
###########
#for mass in massGrid['VBFhWWlnuqq']:
#    print mass
#    if mass < 300 :
#        cmd = 'python ./run_pwg.py -p 1 -x 5 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m VBF_H -f vbfhWWlnuqq'+str(mass) +' -q 8nh -j 10'
#    else :
#        cmd = 'python ./run_pwg.py -p 1 -x 5 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m VBF_H -f vbfhWWlnuqq'+str(mass) + ' -q 8nh -j 10'
#
#    print cmd
#    os.system(cmd)
#
###########
# step 2 (2nd), 3 (8nh)
###########
#for mass in massGrid['VBFhWWlnuqq']:
#    print mass
#    if mass < 300 :
#        cmd = 'python ./run_pwg.py -p 3 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m VBF_H -f vbfhWWlnuqq'+str(mass) +' -q 2nd -j 10'
#    else :
#        cmd = 'python ./run_pwg.py -p 3 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m VBF_H -f vbfhWWlnuqq'+str(mass) + ' -q 2nd -j 10'
#
#    print cmd
#    os.system(cmd)
#
####################################################
# Step 3: Create the POWHEG gridpack tarball
####################################################
#for mass in massGrid['VBFhWWlnuqq']:
#    print mass
#    if mass < 300 :
#        cmd = 'python ./run_pwg.py -p 9 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m VBF_H -f vbfhWWlnuqq'+str(mass) +' -k 1'
#    else :
#        cmd = 'python ./run_pwg.py -p 9 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m VBF_H -f vbfhWWlnuqq'+str(mass) + ' -k 1'
#
#    print cmd
#    os.system(cmd)



#########################
# one go
#########################
#
#for mass in massGrid['VBfHWW2L2Nu']:
#    print mass
#    if mass < 300 :
#        cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m VBF_H -f VBfHWW2L2Nu'+str(mass)+' -q 1nd -n 100'
#    else :
#        cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m VBF_H -f VBfHWW2L2Nu'+str(mass)+' -q 1nd -n 100'
#
#    print cmd
#    os.system(cmd)
#
#
#for mass in massGrid['VBFhWWlnuqq']:
#    print mass
#    if mass < 300 :
#        cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m VBF_H -f vbfhWWlnuqq'+str(mass)+' -q 1nd -n 1000'
#    else :
#        cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m VBF_H -f vbfhWWlnuqq'+str(mass)+' -q 1nd -n 1000'
#
#    print cmd
#    os.system(cmd)
#
# option -d 1: no pdf check
#cmd = 'python ./run_pwg.py  -d 1 -p f -i production/pre2017/14TeV/VBF_H_WW_NNPDF30_14TeV/VBF_H_WW_NNPDF30_14TeV_M125.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m VBF_H -f vbfhWW2l2nu_NNPDF30_14TeV_125 -q 1nd -n 1000'
#
#print cmd
#os.system(cmd)

#for mass in massGrid['ggHToWW2L2Nu']:
#  #print mass
#  if mass < 300 :
#      cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m gg_H_quark-mass-effects -f gghWW2l2nu'+str(mass)+' -q 1nd -n 100'
#  else :
#      cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m gg_H_quark-mass-effects -f gghWW2l2nu'+str(mass)+' -q 1nd -n 100'
#
#  print cmd
#  os.system(cmd)
#


#for mass in massGrid['ggZHWW']:
#  print mass
#  cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/ggHZ_HanythingJ_NNPDF31_13TeV/ggHZ_HanythingJ_NNPDF31_13TeV_M'+str(mass)+'_Vinclusive.input  -m ggHZ -f ggHZ_Hanything_NNPDF31_13TeV_'+str(mass)+' -q 1nw -n 1000'
#
#  print cmd
#  os.system(cmd)

#for mass in massGrid['HZJ']:
#  #if mass != 120: continue
#  print mass
#  # HToWW
#  cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/HZJ_HanythingJ_NNPDF31_13TeV/HZJ_HanythingJ_NNPDF31_13TeV_M'+str(mass)+'_Vinc.input -g ../JHUGen/cards/decay/WWany.input  -m HZJ -f HZJ_HWWany_NNPDF31_13TeV_'+str(mass)+'_Vinc_JHU714 '+' -q 1nw -n 10'
#  print cmd
#  os.system(cmd)
#
#  # HToWWTo2L2Nu
#  cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/HZJ_HanythingJ_NNPDF31_13TeV/HZJ_HanythingJ_NNPDF31_13TeV_M'+str(mass)+'_Vinc.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input  -m HZJ -f HZJ_HWWTo2L2Nu_NNPDF31_13TeV_'+str(mass)+'_Vinc_JHU714'+' -q 1nw -n 10'
#  print cmd
#  os.system(cmd)
#
#  # HToWWTo2L2Nu_ZTo2L
#  #cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/HZJ_HanythingJ_NNPDF31_13TeV/HZJ_HanythingJ_NNPDF31_13TeV_M'+str(mass)+'_Vleptonic.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input  -m HZJ -f HZJ_HWWTo2L2Nu_NNPDF31_13TeV_'+str(mass)+'_Vleptonic_JHU714 '+' -q 1nw -n 10'
#  #print cmd
#  #os.system(cmd)

####################################
# Anomalous coupling
####################################

#cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m gg_H_quark-mass-effects -f ggh_0PM_WW2l2n_M125_jhu710 -q 1nd -n 1000'
#print cmd
#os.system(cmd)
#
#cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_a3.input -m gg_H_quark-mass-effects -f ggh_0M_WW2l2n_M125_jhu710 -q 1nd -n 1000'
#print cmd
#os.system(cmd)
#
#cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_a3mix.input -m gg_H_quark-mass-effects -f ggh_0Mf05ph0_WW2l2n_M125_jhu710 -q 1nd -n 1000'
#print cmd
#os.system(cmd)
#
#
#cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_a2.input -m gg_H_quark-mass-effects -f ggh_0PH_WW2l2n_M125_jhu710 -q 1nd -n 1000'
#print cmd
#os.system(cmd)
#
#
#cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_a2mix.input -m gg_H_quark-mass-effects -f ggh_0PHf05ph0_WW2l2n_M125_jhu710 -q 1nd -n 1000'
#print cmd
#os.system(cmd)
#
#
#cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_L1.input -m gg_H_quark-mass-effects -f ggh_0L1_WW2l2n_M125_jhu710 -q 1nd -n 1000'
#print cmd
#os.system(cmd)
#
#
#cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_L1mix.input -m gg_H_quark-mass-effects -f ggh_0L1f05ph0_WW2l2n_M125_jhu710 -q 1nd -n 1000'
#print cmd
#os.system(cmd)


#cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/WZTo3lNu_NNPDF31nnlo_13TeV/WZ_lllnu_mllmin01_NNPDF31nnlo_13TeV.input -m WZ -f WZTo3LNu_mllmin01_NNPDF31_TuneCP5_13TeV_powheg_pythia8 -q 1nd -n 1000'
#print cmd
#os.system(cmd)


#cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/WZTo3lNu_NNPDF31nnlo_13TeV/WZ_lllnu_mllmin0001max1_NNPDF31nnlo_13TeV.input -m WZ -f WZTo3LNu_mllmin0001max1_NNPDF31_TuneCP5_13TeV_powheg_pythia8 -q 1nd -n 100'
#print cmd
#os.system(cmd)

#cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/ggHZ_HanythingJ_NNPDF31_13TeV/ggHZ_HanythingJ_NNPDF31_13TeV_M125_Vleptonic.input -m ggHZ -f ggHZ_HanythingJ_NNPDF31_13TeV_M125_Vleptonic -q 1nw -n 1000'
#print cmd
#os.system(cmd)


