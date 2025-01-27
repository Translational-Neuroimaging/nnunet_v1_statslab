function Table = LoadNiftisToTable(folder)
% LoadNiftisToTable - Load multiple NIfTI files into a table from a folder.
%
% Syntax:
%   Table = LoadNiftisToTable(folder)
%
% Inputs:
%   folder - (optional) Path to the folder containing NIfTI files.
%            If not provided, a dialog box will prompt for folder selection.
%
% Outputs:
%   Table  - MATLAB table containing NIfTI image data.
%            Row names: NIfTI filenames without extensions and timepoints.
%            Column: 'ImageData' containing the image data.

    % Prompt for folder if not provided
    if nargin < 1
        folder = uigetdir('C:\', 'Select Folder Containing NIfTI Files');
        if folder == 0
            error('No folder selected.');
        end
    end

    % Get list of NIfTI files in the folder
    filePattern1 = fullfile(folder, '*.nii'); % Match .nii files
    filePattern2 = fullfile(folder, '*.nii.gz'); % Match .nii.gz files
    files1 = dir(filePattern1);
    files2 = dir(filePattern2);

    % Combine the file lists
    files = [files1; files2];

    if isempty(files)
        error('No NIfTI files (.nii or .nii.gz) found in the selected folder.');
    end

    % Initialize cell array to store data
    imageData = cell(length(files), 1);

    % Load each NIfTI file
    for i = 1:length(files)
        % Full path to the NIfTI file
        filePath = fullfile(files(i).folder, files(i).name);

        % Load NIfTI data
        nii = load_nii(filePath); % Ensure the `load_nii` function is in your path

        % Convert image data to double
        niiData = double(nii.img);

        % Store image data
        imageData{i} = niiData;
    end

    % Strip extensions from filenames for row names
    rowNames = regexprep({files.name}, '\.nii(\.gz)?$', '');

    % Prompt user for timepoints
    timepoints = input('Enter the timepoints for the dataset (e.g., 24h, 48h): ', 's');
    if isempty(timepoints)
        timepoints = 'Unknown';
    end

    % Append timepoints to row names
    rowNames = strcat(rowNames, '-', timepoints);

    % Ask user for a table name
    tableName = input('Enter a name for the output table: ', 's');
    if isempty(tableName)
        tableName = 'UnnamedTable';
    end

    % Create table with row names as filenames
    Table = table(imageData, 'RowNames', rowNames, 'VariableNames', {'ImageData'});

    % Assign table to workspace with the user-defined name
    assignin('base', tableName, Table);

    % Display completion message
    fprintf('Loaded %d NIfTI files into the table named "%s" in the workspace.\n', height(Table), tableName);
end