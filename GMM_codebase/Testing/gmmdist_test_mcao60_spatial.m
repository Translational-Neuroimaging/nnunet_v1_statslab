function [GMM_Test_Table, idx, NlogL, post, logpdf, mahalaD] = gmmdist_test_mcao60_spatial(GMM_Test_Table, GMM_singleNorm)
% gmmdist_test_mcao60_spatial - Test a Gaussian Mixture Model (GMM) with spatial features.
% This function applies a trained spatial GMM to a dataset, calculates probabilities, and generates labeled outputs.

% Load the template image used for masking
% Replace the file path with the appropriate location on your system.
Templ = load_nii('C:\Users\ramanna1\Documents\Backup Data\PC1\Adrian\Code\Working Code Chamba\Template-masked.nii');

% Define a binary mask for the cerebrum region by thresholding the template image
Rat_Cerebrum = Templ.img > 0;

% Extract features from the masked ADC and T2 images
[ArrayA, Combined_labelsA, ~, ~, MsizeA, NrowsA] = extractarray(GMM_Test_Table.Masked_ADC);
[ArrayT, Combined_labelsT, ~, ~, MsizeT, NrowsT] = extractarray(GMM_Test_Table.Masked_T2);

% Combine the labels for ADC and T2 to identify valid data points
ADC_T2_labels = (Combined_labelsA | Combined_labelsT);

%% Create and normalize spatial coordinate maps
% Generate spatial coordinate maps (R, X, Y, Z) for the brain volume (93x93x120)
[R, X, Y, Z] = mkcoordinatemap(93, 93, 120);

% Normalize the spatial coordinates
Coorr = normalize(R, 1);
Coorx = normalize(X, 1);
Coory = normalize(Y, 2);
Coorz = normalize(Z, 3);

% Normalize the ADC and T2 feature arrays
ArrayTn = normalize_P(ArrayT);
ArrayAn = normalize_P(ArrayA);

% Replicate the spatial coordinate maps to match the number of rows in the data
Coorx = repmat(Coorx, [1, 1, 1, NrowsA]);
Coory = repmat(Coory, [1, 1, 1, NrowsA]);
Coorz = repmat(Coorz, [1, 1, 1, NrowsA]);

% Replicate unnormalized coordinates (for optional use)
X = repmat(X, [1, 1, 1, NrowsA]);
Y = repmat(Y, [1, 1, 1, NrowsA]);
Z = repmat(Z, [1, 1, 1, NrowsA]);

%% Combine and normalize features
% Extract valid data points based on the combined labels and form feature matrices
K_data_Combined(:, 1) = ArrayAn(~ADC_T2_labels); % Normalized ADC
K_data_Combined(:, 2) = ArrayTn(~ADC_T2_labels); % Normalized T2
K_data_Combined(:, 3) = Coorx(~ADC_T2_labels);  % Normalized X-coordinate
K_data_Combined(:, 4) = Coory(~ADC_T2_labels);  % Normalized Y-coordinate
K_data_Combined(:, 5) = Coorz(~ADC_T2_labels);  % Normalized Z-coordinate

% Store unnormalized features (optional)
Unnorm(:, 1) = ArrayA(~ADC_T2_labels);
Unnorm(:, 2) = ArrayT(~ADC_T2_labels);
Unnorm(:, 3) = X(~ADC_T2_labels);
Unnorm(:, 4) = Y(~ADC_T2_labels);
Unnorm(:, 5) = Z(~ADC_T2_labels);

% Store selected features in a data structure
Data.SelectedFeatures = Unnorm;           % Unnormalized features
Data.NormSelectedFeatures = K_data_Combined; % Normalized features

%% GMM Testing
% Test the GMM on the normalized features
[idx, NlogL, post, logpdf, mahalaD] = cluster(GMM_singleNorm, Data.NormSelectedFeatures);

% Compute cluster averages for each feature
NumClus = 5; % Number of GMM clusters
for i = 1:NumClus
    ClusterAverages(i, :) = mean(Data.SelectedFeatures(idx == i, :));
end

% Calculate a cluster score and sort clusters based on the score
StrokeClusterScore = ClusterAverages(:, 2) ./ ClusterAverages(:, 1); % T2/ADC ratio
[~, ClusterScoreIDXs] = sort(StrokeClusterScore, 'descend'); % Sort clusters by descending score

% Adjust cluster indices to exclude clusters with low average ADC values
flag = 1;
count = 1;
SortedClusterAverages = ClusterAverages(ClusterScoreIDXs, :);
while flag
    if SortedClusterAverages(count, 1) < 10
        ClusterScoreIDXs = circshift(ClusterScoreIDXs, -1, 1);
        count = count + 1;
    else
        flag = 0;
    end
end

% Permute cluster probabilities based on sorted indices
post = post';
GMMClusProbsPermuted = post(ClusterScoreIDXs, :);

% Find maximum cluster probabilities and assign labels
[Probs, GMMClusIDXsPermuted] = max(GMMClusProbsPermuted);
iProbs = Probs';

% Reshape the GMM labels and probability maps
Data_GMM_Labels = GMMClusIDXsPermuted';
Data_GMM_Labels(Data_GMM_Labels ~= 1) = 2; % Set labels: Stroke (1) vs Non-Stroke (2)
Data_Stroke = (Data_GMM_Labels == 1);

% Reshape the labels and probabilities back to the original image size
idxshape = nan(size(ADC_T2_labels(:, 1)));
idxshape(~ADC_T2_labels(:, 1)) = Data_Stroke;
Idsreshaped = reshape(idxshape, [MsizeA, NrowsT]);

% Reshape the probabilities for stroke regions
Allprobs = iProbs(Data_Stroke == 1);
idxAllprobs = nan(size(ADC_T2_labels(:, 1)));
idxAllprobs(~ADC_T2_labels(:, 1)) = iProbs;
idprobs = nan(size(iProbs(:, 1)));
idprobs(Data_Stroke) = Allprobs;
idxAllprobs(~ADC_T2_labels(:, 1)) = idprobs;
Idsallprobs = reshape(idxAllprobs, [MsizeA, NrowsT]);

%% Store results in GMM_Test_Table
% Save the probability maps and binary labels into the test table
for t = 1:NrowsA
    GMM_Test_Table.RF_probmap_new(t) = {Idsallprobs(:, :, :, t)};
    GMM_Test_Table.RF_Probmaps1_new(t) = {Idsallprobs(:, :, :, t) > 0};
end

% Replace NaN values in the probability maps with zeros based on the Rat_Cerebrum mask
GMM_Test_Table.RF_Probmaps1_new = replaceNaN(GMM_Test_Table.RF_Probmaps1_new, Rat_Cerebrum);
end
