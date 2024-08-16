% Load the .mat file with desired RW and Walk from Directory from computer.
% Server implementation might be different.
clc;

RW = 1;
Walk = 1;
% Construct the file path using sprintf. The %d is like doing "Hello {name}"
% .mat file(s) can be found inside RealWorldNavigationCory > RWNApp_Output_Jan2024
% Replace the string text with your filePath to the .mat file.
filePath = sprintf('C:\\Users\\burke\\OneDrive\\Desktop\\NeuroIOT\\RW1\\RWNApp_Output_Jan2024\\RWNApp_RW%d_Walk%d.mat', RW, Walk);
data = load(filePath);

Mode = 'Xsens Offset'; %Xsens Offset , Neural Pace Offset

if strcmp(Mode,'Neural Pace Offset')
    % Extract 'ntp_gp' and 'ntp_np'
    ntp_gp = data.ntp_gp;
    ntp_np = data.ntp_np;   
    
    
    % Calculate the difference between when the gopro video starts and the
    % nerual pace begins to record. Example of how the offset is created
    % and can be verifed is explained below. 
    difference = ntp_np(1) - ntp_gp(1);
    

    % Display the difference
    fprintf('Difference between NeuralPace and GoPro is %0.16f seconds \n', difference);

elseif strcmp(Mode,'Xsens Offset')
    % Extract 'ntp_gp' and 'ntp_np'
    ntp_gp = data.ntp_gp;
    ntp_xs = data.ntp_xs_orig;  
    
    
    % Calculate the difference between when the gopro video starts and the
    % nerual pace begins to record. Example of how the offset is created
    % and can be verifed is explained below. 
    difference = ntp_xs(1) - ntp_gp(1);
   

    % Display the difference
    fprintf('Difference between Xsens and GoPro is %0.16f seconds \n', difference);
else
    % This is the only implemented option.
end


% If you go and look at the first time that a "Doorway" event is recorded
% you will see that it is at Neural Pace sample: 10978. Given that we know
% that the NP is recorded at 250 Hz via the RWNApp_RW%d_Walk%d.mat file. We
% can do 10978 / 250 to get 43.92 seconds. However when you go into the
% the Gopro video corresponding to the walk, you will notice the timestamp
% does not line up with the event. This is becuase the NP and the GoPro
% video are not started at the same time. The Network Time Protocol or NTP
% is used as a global time measurement to compare and find the offset. If
% we combine the 43.92 seconds with the calculated offset 50.57 seconds
% from RW1 Walk 1 you will find that 94.38 seconds or 1 minute and 34
% seconds matches with the first occurance of a doorway found in the
% original GoPro Video found inside the box (RealWorldNavigationCory > RW1 > Original > Walk1 > Gopro > GH010069.MP4). 