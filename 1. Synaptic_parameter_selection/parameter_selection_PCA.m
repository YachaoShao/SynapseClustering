%% Standardization
Data=zscore(ParametersS2);      %%Raw Data in excel format 
 
%% PCA
[coeff,score,latent,~,explained] = pca(Data);

%% Scree test to determine the number of principal components to be used
figure(1)
plot(latent,'k-o')
title('Scree test');
xlabel('Component number');
ylabel('Eigenvalue');

%% Percentage of variance explained by each principal component
figure(2)
pareto(explained);
title('Percentage of variance explained by each PC');
xlabel('Principal Component')
ylabel('Variance Explained (%)')

%% Scatter plot 3D
R = score(:,1:2);
figure(3);
%scatter3(R(:,1),R(:,2), (R(:,3)),'filled');    %%scatter3 for 3D, add (R(:,3)) 
scatter(R(:,1), R(:,2), 'filled');
title ('Scatter plot');%
xlabel('First Principal Component');
ylabel('Second Principal Component');
%zlabel('Third Principal Component');
neurons = num2str((1:size(R,1))','%d');       %% to get the name of data points
%text(R(:,1),R(:,2),(R(:,3)),neurons,'horizontal','left', 'vertical','bottom');
text(R(:,1),R(:,2),neurons,'horizontal','left', 'vertical','bottom');

%% Projection of original variables to new  
figure(4)
parameters = {'bvol','barea','bsc.num','bsc.area','bpsd.area','bmito.num','bmito.vol','bmito.pvol','bves.num','bves.vol','bves.pvol','bves.diam','bves.p10','bves.p20','bves.p30','bves.p40','bves.p50','bves.p60','bves.p70','bves.p80','bves.p90','bves.p100','bves.p200','bves.p300','bves.p400','bves.p500'};

biplot(coeff(:,1:2),'scores',score(:,1:2),'varlabels',parameters,'ObsLabels',neurons);
datacursormode on
% axis([-0.7 0.7 -0.7 0.7 -0.7 0.7]); 
%axis([-1 1 -1 1 -1 1]);
axis([-1 1 -1 1]);

%% Hierarchical Cluster Analysis - Dendrogram
tree=linkage(R,'ward');       
D = pdist(R);         %% pdist = Euclidean distance
leafOrder = optimalleaforder(tree,D);
figure(5),dendrogram(tree,0,'ReOrder',leafOrder,'ColorThreshold','default');

%% Determining the number of clusters (Thorndike method)
X = size(tree);
figure(6), plot(X(1):-1:1,tree(:,3),'b:o');        
title ('Determination of number of clusters');
xlabel('Number of clusters');
ylabel('Linkage distance');

%% Boxplot
figure(7)
boxplot(Data,'orientation','horizontal','labels',parameters);

%% Explanations:
%%'Coeff' - principal component coefficients in a new space in which the 
%dataset can be projected. To find the most correlated variables, choose a
%correlation value more than 0.5/0.7 from principal component coefficients.
%%To decide how many principal components to retain for cluster analysis,
%use only principal components with eigenvalues greater than one.
%%The eigenvalues are given in 'latent'. This is shown in 'screeplot'.
%%To identify the locations of each point in the plot, do a scatter plot of 
%principal component 'scores'. 

%D=linkage(pdist(R),'ward');        %% pdist = Euclidean distance
%figure(5),dendrogram(D,0,'ColorThreshold','default');