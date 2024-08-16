# BrainNavigationPipeline

Dual Vision Neural Analysis Pipeline

Download the .mat file related to the walk in question. Ex: RW1 Walk1 => RWNApp_RW1_Walk1. File can be found in RealWorldAnalysisCory => 
RWNApp_Output_Jan2024 => desired file. 


Download the Gopro Video related to the walk in question. Make sure that you are downloading the video from the ORIGINAL folder. Ex: RW1 Walk1 => RealWorldAnalysisCory => Original => Walk1 => GoPro => desired file. The files are not always concatenated, so look for the file where they are inside and there is a clapper. The patient is normally standing still, this is the first video. You can then use the ending of the first to the beginning of other .mp4 files to see which video is next in the event there are more than 2 .mp4 files. Do not worry about any other file type that is not .mp4. 

Download all the Matlab and python files. Make sure the matlab files listed are all in the same directory.(Change names if updated)
MatLab: CalcRWAPerm, CalcRWAPval, morseSpecGram, OffsetToOriginalCalculator, RAAnalysis_Single, RWAnalysisTest
Python: ImagesToVideo, DualVideoMaker

Open the OffsetToOrignalCalculator.mat file. Plug in the file path to the RWNApp file path here to calculate the offset. The value produced represents the time difference in seconds from the start of the Original Gopro video to the start of the Neural Pace being recorded. Data prior to this timestamp will not be available. Remember or write down this time difference to the 100th. So if the offset calculated is 50.5723495483398438 then write down 50.57. Add 10 to this. The reason for adding 10 will be explained in the next step. 

Open the RWAnalysis_Single.mat file. This file is extremely finicky so you have to be careful to make sure you are following everything correctly. Change the obj.RootDir = on line 77 to be the directory to the RWNApp_RWx_Walkx file on your device. THIS HAS TO BE THE ONLY FILE IN THE DIRECTORY. Next go to line 1955 / the only place where the word “saveas” appears in the file, and change the save directory to a new folder you created where the output of spectrograms can go. The file works by extracting all the data in the RWNApp_RWx_Walkx file and constructing a single spectrogram with a single point as reference. The Neural Pace is recorded 250 times a second or 250 Hz. The spectrogram generates data for 10 seconds before and 10 seconds after. This means that any data being attempted to generate data for sample 2500 or less will be unsuccessful (this is important for the next step). More simply put… sample 2500 is 10 seconds in. If you try to generate data at sample 2000, the spectrogram will fail because there is no data for -2 seconds. The 2000th sample happens at 8 seconds so when the code attempts to go back 10 seconds, it will break. Anyways, if you have changed the directories you can move on to step 6.

Open the RWAnalysis_Test.mat file. Ensure that whatever RW you are testing matches with the patientIDX number on line 11.rwAnalysis.loadData('PatientIdx',1);
You can also change the EndTime and FPS to your desired values. If you change the start time you are going to need to add that value minus 10 to the offset. So if you change the start time from 10 seconds to 15 then you will need to add 5 more seconds to the original offset you had + 10. That's confusing, here is the example: if the code outputs 50.57 seconds you need to add whatever value is in the startTime. So in the case of 15 seconds, the final total offset is 65.57 seconds. You cannot go below 10 seconds for the startTime. Run the file and you should see a large amount of images populate in your save folder. 

We are done with MatLab for now, open the images to a video python file. Change the input directory to where you are holding all the images and change the output to your desired folder. Make sure you match the FPS to whatever FPS you decided in the RWAnalysis File.

Open the DualVideoMaker, plug in the GoProVideo to the video1 slot and the output video from the previous file into the video2 slot. An example filepath is shown Inside the file. Change the GoProOffsetForSync to the correct value determined earlier. Run the file. The GUI should populate! 
