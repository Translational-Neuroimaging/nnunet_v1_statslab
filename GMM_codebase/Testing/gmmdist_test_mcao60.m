function [GMM_Test_Table, idx, NlogL, post, logpdf, mahalaD] = gmmdist_test_mcao60(GMM_Test_Table, GMM_singleNorm)
% gmmdist_test - Test a Gaussian Mixture Model (GMM) on selected features

% Load the template image used for masking
Templ = load_nii('C:\Users\ramanna1\Documents\Backup Data\PC1\Adrian\Code\Working Code Chamba\Template-masked.nii');

% Define a binary mask for the Rat_Cerebrum by thresholding the template image
Rat_Cerebrum = Templ.img > 0;

% Extract features from the masked ADC and T2 images
[ArrayA, Combined_labelsA, ~, ~, MsizeA, NrowsA] = extractarray(GMM_Test_Table.Masked_ADC);
[ArrayT, Combined_labelsT, ~, ~, MsizeT, NrowsT] = extractarray(GMM_Test_Table.Masked_T2);

% Combine labels for ADC and T2 images
ADC_T2_labels = (Combined_labelsA | Combined_labelsT);

% Create a combined feature matrix for ADC and T2 data
K_data_Combined(:,1) = ArrayA(~ADC_T2_labels);
K_data_Combined(:,2) = ArrayT(~ADC_T2_labels);

% Normalize the combined feature matrix
K_data_Combined_n(:,1) = normalize_P(K_data_Combined(:,1));
K_data_Combined_n(:,2) = normalize_P(K_data_Combined(:,2));

% Store the selected features and normalized features in a data structure
Data.SelectedFeatures = K_data_Combined;
Data.NormSelectedFeatures = K_data_Combined_n;

% Set the number of clusters for GMM testing
NumClus = 5;

% Cluster the data using the trained GMM model
[idx, NlogL, post, logpdf, mahalaD] = cluster(GMM_singleNorm, Data.NormSelectedFeatures);

% Calculate cluster averages and sort them by a score
for i = 1:NumClus
    ClusterAverages(i,:) = mean(Data.SelectedFeatures(idx == i,:));
end

% Calculate a cluster score and sort cluster indices accordingly
StrokeClusterScore = ClusterAverages(:,2) ./ ClusterAverages(:,1);
[~, ClusterScoreIDXs] = sort(StrokeClusterScore, 'descend');

% Permute the cluster probabilities based on the sorted indices
flag = 1;
count = 1;
SortedClusterAverages = ClusterAverages(ClusterScoreIDXs,:);
while flag
    if SortedClusterAverages(count,1) < 10
        ClusterScoreIDXs = circshift(ClusterScoreIDXs, -1, 1);
        count = count + 1;
    else
        flag = 0;
    end
end

% Transpose and permute the cluster probabilities
post = post';
GMMClusProbsPermuted = post(ClusterScoreIDXs,:);

% Find the maximum probability for each cluster
[Probs, GMMClusIDXsPermuted] = max(GMMClusProbsPermuted);
iProbs = Probs';

% Reshape the GMM labels and select the primary cluster
Data_GMM_Labels = GMMClusIDXsPermuted';
Data_GMM_Labels(Data_GMM_Labels ~= 1) = 2;
Data_Stroke = (Data_GMM_Labels == 1);

% Reshape the labels and probability maps
idxshape = nan(size(ADC_T2_labels(:,1)));
idxshape(~ADC_T2_labels(:,1)) = Data_Stroke;
Idsreshaped = reshape(idxshape, [MsizeA, NrowsT]);

Allprobs = iProbs(Data_Stroke == 1);
idxAllprobs = nan(size(ADC_T2_labels(:,1)));
idxAllprobs(~ADC_T2_labels(:,1)) = iProbs;
idprobs = nan(size(iProbs(:,1)));
idprobs(Data_Stroke) = Allprobs;
idxAllprobs(~ADC_T2_labels(:,1)) = idprobs;
Idsallprobs = reshape(idxAllprobs, [MsizeA, NrowsT]);

% Store probability maps in GMM_Trained_Table
for t = 1:NrowsA
    GMM_Test_Table.RF_probmap_new(t) = {Idsallprobs(:,:,:,t)};
    GMM_Test_Table.RF_Probmaps1_new(t) = {Idsallprobs(:,:,:,t) > 0};
end

% Replace NaN values in probability maps based on the Rat_Cerebrum mask
GMM_Test_Table.RF_Probmaps1_new = replaceNaN(GMM_Test_Table.RF_Probmaps1_new, Rat_Cerebrum);
end
