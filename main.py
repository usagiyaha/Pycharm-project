# to get the docstring of the function
# import inspect
#
# def split_and_stack():
#     """
#     Splits a given string and stacks it
#
#     :return:
#     """
#     return 42
#
# print(inspect.getdoc(split_and_stack))
# print(split_and_stack.__doc__)

# def load_data(path):
#     """
#     Loads and plots a given path
#     :param path:
#     :return:
#     """
#     #load the data
#     data = pd.read_csv(path)
#     y = data['labels'].values
#     x = data[col for col in data.columns if col != 'labels'].values
#     return x, y
# def plot_data(x):
#     """
#     Plots the first two principal components of a matrix.
#
#     Args:
#         X(numpy.ndarray): The data to plot.
#     """
#     pca = PCA(n_components=2).fit_transform(x)
#     plt.scatter(pca[:,0], pca[:,1])

values = [1,2,7,5,6]
values_sorted = sorted(values)
print(values_sorted)
