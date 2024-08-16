% RWAnalysis_Test
% Assuming RWAnalysis class is defined and available in the path
clear;
clc;

% Create an instance of the RWAnalysis class
rwAnalysis = RWAnalysis_Single();


% Load data for the specified patient
rwAnalysis.loadData('PatientIdx',1);

% Generate multi-patient transition data for specgram analysis
rwAnalysis.getMultTransData();

% Plot the multi-transition spectrogram
% Adjust the parameters as needed for your specific use case

% Parameters in seconds. (This is where you want to alter the values.)
startTime = 60; % seconds
EndTime = 120; % seconds
Fps = 2; % Frames per second. The higher you go the smoother the end video will be.


% Sample conversion.
startSample = startTime * 250;
EndSample = EndTime * 250;
FpsSample = 250 / Fps;

  
for sampleRange = startSample : FpsSample : EndSample
    
    fH = rwAnalysis.plotSingleTransSpecGramPerm(sampleRange, 'transtype', 'Doorway', 'regiontype', 'AntHipp', 'walktype', 'All Walks', 'permtype', 'standard', 'correctiontype', 'cluster', 'patienttype', 'All Patients');
end


