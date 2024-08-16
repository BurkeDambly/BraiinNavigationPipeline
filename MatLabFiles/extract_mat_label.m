

% INPUT FOLDER PATH-------------------------------------------
%Specify the folder path (If you are on mac try a differnt using single
%forward slashes for the file path if this doesn't work. 
folder_path = 'C:\Users\burke\OneDrive\Desktop\NeuroIOT\RW1\RWNApp_Output_Jan2024\';

% List all files in the folder
files = dir(fullfile(folder_path, '*.mat'));

% Loop through each file
for i = 1:numel(files)
    % Check if the file is a regular file (not a directory)
    if ~files(i).isdir
        % Read the content of the file
        file_path = fullfile(folder_path, files(i).name);
        data = load(file_path);
        evnts_tbl = data.evnts_tbl;

        % Define the path to save the CSV file
        [~, file_name, ~] = fileparts(files(i).name); % Extract file name without extension
        % Prepend "evnts_" to the filename
        evnts_file_name = ['evnts_' file_name];

        % SAVE FOLDER PATH ---------------------------------------
        % Define the path to save the CSV file
        save_path = fullfile('C:\Users\burke\OneDrive\Desktop\NeuroIOT\RW1\RW1Extracted', [evnts_file_name '.csv']);

        writetable(evnts_tbl, save_path);
    end
end


% data = load('C:\\Users\\burke\\OneDrive\\Desktop\\CPS\\RW3\\RWNApp_RW5\\RWNApp_RW3_Walk1.mat');
% % print(data.evnts_tbl);
%evnts_tbl = data.evnts_tbl;
% 
% % Save the table as a CSV file
% writetable(evnts_tbl, 'C:\\Users\\burke\\OneDrive\\Desktop\\CPS\\RW5\\RWNApp_RW5\\labelRWNApp_RW5_Walk1_evnts.csv');