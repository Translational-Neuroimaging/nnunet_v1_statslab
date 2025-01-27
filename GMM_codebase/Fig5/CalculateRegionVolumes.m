function tableVolumes = CalculateRegionVolumes(matFile, niftiTable, ~)
% CalculateRegionVolumes - Calculate the volume of regions in a .mat mask file.
%
% Syntax:
%   tableVolumes = CalculateRegionVolumes(matFile, niftiTable, volumeFactor)
%
% Inputs:
%   matFile      - Path to the .mat mask file (e.g., 'Rat_Atlas.mat').
%   niftiTable   - Table containing NIfTI image data and filenames.
%                  Target values are in the 'ImageData' column.
%   volumeFactor - (optional) Volume factor to multiply with voxel counts.
%                  Default is 0.22^3 / 1000 (mm^3 to cm^3 conversion).
%
% Outputs:
%   tableVolumes - Structured table of calculated volumes for each mask and row.

    % Set default volume factor
    defaultVolumeFactor = (0.22^3) / 1000; % mm^3 to cm^3

    % Prompt user to confirm or change volume factor
    fprintf('The standard volume factor is %.5f cm^3.', defaultVolumeFactor);
    userChoice = input('Keep the standard volume factor? (Enter y for yes, or n to specify a new value): ', 's');
    if strcmpi(userChoice, 'n')
        volumeFactor = input('Enter the new volume factor: ');
        if isempty(volumeFactor)
            volumeFactor = defaultVolumeFactor;
            fprintf('No value entered. Using default volume factor: %.5f cm^3.', defaultVolumeFactor);
        end
    else
        volumeFactor = defaultVolumeFactor;
    end

    % Load the .mat mask file
    data = load(matFile, 'Rat_Striatum', 'Rat_Cerebrum', 'Rat_Cortex');

    % Masks in the .mat file
    maskFields = {'Rat_Striatum', 'Rat_Cerebrum', 'Rat_Cortex'};
    numFields = length(maskFields);
    numRows = height(niftiTable);

    % Initialize table to store volumes for each row and mask
    rowVolumes = zeros(numRows, numFields);

    for m = 1:numFields
        if isfield(data, maskFields{m})
            maskData = double(data.(maskFields{m}));
        else
            error('The .mat file does not contain a variable named ''%s''.', maskFields{m});
        end

        for r = 1:numRows
            % Get the current ImageData (3D matrix) from the table
            targetMatrix = niftiTable.ImageData{r};

            % Ensure the dimensions of maskData and targetMatrix are compatible
            if ~isequal(size(maskData), size(targetMatrix))
                error('The dimensions of maskData and targetMatrix in row %d do not match.', r);
            end

            % Find the number of voxels where the mask overlaps with the target matrix
            voxelCount = sum(maskData(:) & targetMatrix(:)); % Logical AND operation

            % Calculate the volume for this row and mask
            rowVolumes(r, m) = voxelCount * volumeFactor;
        end
    end

    % Create structured table for output
    tableVolumes = table(rowVolumes(:, 1), rowVolumes(:, 2), rowVolumes(:, 3), ...
                         'RowNames', niftiTable.Properties.RowNames, ...
                         'VariableNames', {'Volume_Striatum', 'Volume_Cerebrum', 'Volume_Cortex'});

    % Display the results
    fprintf('Calculated volumes using volume factor %.5f cm^3:', volumeFactor);
    disp(tableVolumes);
end
