from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'tutorial_debug_MC_generation'
config.General.workArea = '/net/scratch_cms3b/crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.User.voGroup = 'dcms'

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'LHE.py'
#config.JobType.allowUndistributedCMSSW = True
config.JobType.scriptExe = 'crabtest.sh'
config.JobType.outputFiles = ['LHETuple.root']

config.Data.outputPrimaryDataset = 'MinBias'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10
NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_tutorial_May2015_MC_analysis'

config.Site.storageSite = "T2_DE_DESY"
