% Load the .mat file
data = load('C:\Users\burke\OneDrive\Desktop\NeuroIOT\RW1\RWNApp_Output_Jan2024\RWNApp_RW1_Walk1.mat');

% Extract the relevant Xsens data
xsens_data = data.d_xs;

% Assuming xsens_data is structured in a way where:
% Columns 1-3: x, y, z positions
% Columns 4-6: x, y, z accelerations
% Columns 7-9: x, y, z velocities

% Note: Adjust the indexing based on the actual data structure
% This is a general example assuming these columns are in the specified order

% Extract position, acceleration, and velocity
position = xsens_data(:, 1:3);    % x, y, z positions
acceleration = xsens_data(:, 4:6); % x, y, z accelerations
velocity = xsens_data(:, 7:9);     % x, y, z velocities

% Combine data into one matrix
output_data = [position, acceleration, velocity];

% Define the output file name
output_file = 'C:\Users\burke\OneDrive\Desktop\NeuroIOT\RW1\RW1Extracted\xsens_data_output.csv';

% Write to CSV
csvwrite(output_file, output_data);

disp(['Data successfully written to ', output_file]);