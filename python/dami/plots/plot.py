import numpy as np
import matplotlib.pyplot as plt

from python.dami import riona
from python.dami.sources import data as ff

labels = ['women', 'men']


def scatter_clazz(data):
    for index, clazz in enumerate(data):
        vectors_in_class = np.asarray(clazz)
        x = vectors_in_class[:, 0]
        y = vectors_in_class[:, 1]
        plt.scatter(x, y, label=labels[index])


def draw_classified_2d_data(data):
    scatter_clazz(data)

    plt.title("Assigned sex in the function of height and weight")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend()
    plt.grid()
    plt.show()


def draw_classified_2d_data_with_test(data, point, r=5):
    scatter_clazz(data)

    x, y = point
    plt.scatter(x, y, color='grey')
    circle = plt.Circle((x, y), r, color='grey', fill=False)
    plt.gca().add_patch(circle)

    plt.title("Assigned sex in the function of height and weight\n Adding new point with k = ...")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend()
    plt.grid()
    plt.show()


def draw_classified_2d_data_with_metric(grouped_data, point, minimum_values, maximum_values, types=None, r=None,
                                        k=None):
    if r is not None:

        for index, clazz in enumerate(grouped_data):
            x = np.array(clazz)[:, 0]
            y = np.array(clazz)[:, 1]
            plt.scatter(x, y, color='#D8D8D8')

            grouped_data[index] = list(
                filter(lambda v: riona.distance(point, v, types, minimum_values, maximum_values) <= r, clazz))

    scatter_clazz(grouped_data)

    x_c, y_c = point
    plt.scatter(x_c, y_c, color='grey')

    for index, clazz in enumerate(grouped_data):
        for vector in clazz:
            if r is None or riona.distance(point, vector, types, minimum_values, maximum_values) <= r:
                x, y, group = vector
                plt.text(x + .5, y + .5,
                         "{:.2f}".format(riona.distance(point, vector[:-1], types, minimum_values, maximum_values)))

    if k is not None:
        plt.title("Assigned sex in the function of height and weight\n Adding new point with k = {}".format(k))
    else:
        plt.title("Assigned sex in the function of height and weight".format(k))

    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend()
    plt.grid()
    plt.show()


def flatten(t):
    return [item for sublist in t for item in sublist]


def draw(data, class_name):
    for clazz, elements in data.groupby(by=[class_name]):
        x = np.array(elements)[:, 0]
        y = np.array(elements)[:, 1]

        plt.scatter(x, y, label=labels[clazz - 1])

    plt.title("Assigned sex in the function of height and weight")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend()
    plt.grid()
    plt.show()


def draw_with_distance(data, class_name, point, minimum_values, maximum_values):
    for clazz, elements in data.groupby(by=[class_name]):
        x = np.array(elements)[:, 0]
        y = np.array(elements)[:, 1]

        plt.scatter(x, y, label=labels[int(clazz - 1)])

        for index, vector in elements.iterrows():
            x_l, y_l, label = vector
            plt.text(x_l + .5, y_l + .5,
                     "{:.2f}".format(riona.distance(point[:-1], vector[:-1], data.dtypes, class_name, minimum_values,
                                                    maximum_values)))

    plt.title("Assigned sex in the function of height and weight\n Adding new point with k = ...")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend()
    plt.grid()
    plt.show()


def draw_closest_point(data, closest_objects, class_name, point, minimum_values, maximum_values, k=1):
    for clazz, elements in data.groupby(by=[class_name]):
        x = np.array(elements)[:, 0]
        y = np.array(elements)[:, 1]

        plt.scatter(x, y, color='#D8D8D8')

        for index, vector in elements.iterrows():
            x_l, y_l, label = vector
            plt.text(x_l + .5, y_l + .5,
                     "{:.2f}".format(
                         riona.distance(point, vector, closest_objects.dtypes, class_name, minimum_values,
                                        maximum_values)))

    for clazz, elements in closest_objects.groupby(by=[class_name]):
        x = np.array(elements)[:, 0]
        y = np.array(elements)[:, 1]

        plt.scatter(x, y, label=labels[int(clazz - 1)])

        for index, vector in elements.iterrows():
            x_l, y_l, label = vector
            plt.text(x_l + .5, y_l + .5,
                     "{:.2f}".format(
                         riona.distance(point, vector, closest_objects.dtypes, class_name, minimum_values,
                                        maximum_values)))

    x_c, y_c, label = point
    plt.scatter(x_c, y_c, color='red')

    plt.title("Assigned sex in the function of height and weight\n Adding new point with k = {}".format(k))
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend()
    plt.grid()
    plt.show()
