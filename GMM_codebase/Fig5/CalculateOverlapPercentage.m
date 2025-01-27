function overlap = CalculateOverlapPercentage(table1, table2)
% CalculateOverlapPercentage - Calculate the overlap percentage between two NIfTI datasets.
%
% Syntax:
%   overlap = CalculateOverlapPercentage(table1, table2)
%
% Inputs:
%   table1 - First table containing NIfTI image data.
%   table2 - Second table containing NIfTI image data.
%
% Outputs:
%   overlap - Table containing overlap percentages for each row.

    % Check that both tables have the same row names
    if ~isequal(sort(table1.Properties.RowNames), sort(table2.Properties.RowNames))
        error('The two tables must have the same row names.');
    end

    % Ensure row order matches between tables
    table2 = table2(table1.Properties.RowNames, :);

    % Initialize overlap percentages and changes
    overlapPercentages = zeros(height(table1), 1);
    percentageChanges = zeros(height(table1), 1);

    % Calculate overlap and changes for each row
    for r = 1:height(table1)
        % Get the image data from both tables
        img1 = table1.ImageData{r};
        img2 = table2.ImageData{r};

        % Replace NaNs with zeros
        img1(isnan(img1)) = 0;
        img2(isnan(img2)) = 0;

        % Ensure the dimensions of the two images are compatible
        if ~isequal(size(img1), size(img2))
            error('The dimensions of the images in row %s do not match.', table1.Properties.RowNames{r});
        end

        % Calculate the overlap
        overlapVoxelCount = sum(img1(:) & img2(:)); % Logical AND operation
        totalVoxelCount = sum(img1(:) | img2(:)); % Logical OR operation

        % Calculate the percentage of overlap
        if totalVoxelCount == 0
            overlapPercentages(r) = 0; % Avoid division by zero
        else
            overlapPercentages(r) = (overlapVoxelCount / totalVoxelCount) * 100;
        end

        % Calculate the difference and percentage change
        difference = img1(:) - img2(:);
        changeMagnitude = sum(abs(difference));
        referenceMagnitude = sum(abs(img1(:)));
        if referenceMagnitude == 0
            percentageChanges(r) = 0; % Avoid division by zero
        else
            percentageChanges(r) = (changeMagnitude / referenceMagnitude) * 100;
        end
    end

    % Get table names for dynamic naming
    table1Name = inputname(1);
    table2Name = inputname(2);
    if isempty(table1Name)
        table1Name = 'Table1';
    end
    if isempty(table2Name)
        table2Name = 'Table2';
    end

    % Name the output table dynamically
    overlapName = sprintf('overlap_%s_%s', table1Name, table2Name);

    % Create output table
    overlap = table(overlapPercentages, percentageChanges, ...
                         'RowNames', table1.Properties.RowNames, ...
                         'VariableNames', {'OverlapPercentage', 'PercentageChange'});

    % Assign table to workspace with the dynamic name
    assignin('base', overlapName, overlap);

    % Display the results
    fprintf('Overlap table created and assigned to workspace as "%s".\n', overlapName);
    disp('Overlap percentages and percentage changes for each row:');
    disp(overlap);
end

