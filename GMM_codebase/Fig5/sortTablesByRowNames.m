function [sortedTable1, sortedTable2] = sortTablesByRowNames(table1, table2)
    % Ensure both tables have row names
    if isempty(table1.Properties.RowNames) || isempty(table2.Properties.RowNames)
        error('Both input tables must have row names.');
    end

    % Find the common row names between the two tables
    commonRowNames = intersect(table1.Properties.RowNames, table2.Properties.RowNames);

    % If there are no common row names, return empty tables
    if isempty(commonRowNames)
        warning('No common row names found. Returning empty tables.');
        sortedTable1 = table();
        sortedTable2 = table();
        return;
    end

    % Sort and retain only the rows with common row names
    sortedTable1 = table1(commonRowNames, :);
    sortedTable2 = table2(commonRowNames, :);

    % Ensure the row names are in the same order for both tables
    sortedTable2 = sortedTable2(commonRowNames, :);
end
