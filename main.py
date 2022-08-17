import math

import numpy as np
import plotly.graph_objects as go
from functools import cache


def create_integer_spiral(size: int) -> np.ndarray:
    mat = np.zeros((size, size))
    TOP_RIGHT = (0, size - 1)
    i, j = TOP_RIGHT
    n = size ** 2
    while n > 0:
        # Going left
        while j >= 0 and mat[i, j] == 0:
            mat[i, j] = n
            n -= 1
            j -= 1
        j += 1
        i += 1
        # Going down
        while i < size and mat[i, j] == 0:
            mat[i, j] = n
            n -= 1
            i += 1
        i -= 1
        j += 1
        # Going right
        while j < size and mat[i, j] == 0:
            mat[i, j] = n
            n -= 1
            j += 1
        j -= 1
        i -= 1
        # Going up
        while i >= 0 and mat[i, j] == 0:
            mat[i, j] = n
            n -= 1
            i -= 1
        i += 1
        j -= 1
    return mat


@cache
def is_prime(n):
    if n == 2:
        return n, 1

    if n % 2 == 0 or n == 1:
        return n, 0
    for i in range(3, math.ceil(n ** 0.5) + 1, 2):
        if n % i == 0:
            return n, 0
    return n, 1


# noinspection PyShadowingNames
def get_is_prime_fig(mat: np.ndarray):
    is_prime_vec = np.vectorize(is_prime)
    mat = is_prime_vec(mat)
    fig = go.Figure()
    print("Rendering figure...")
    fig.add_trace(go.Heatmap(z=mat[1], colorscale='blues', hovertext=mat[0], hoverinfo="text", showscale=False))
    fig.update_layout(title_text="Prime Spiral", title_x=0.5, yaxis_scaleanchor='x', plot_bgcolor='rgba(0,0,0,0)')
    fig.update_xaxes(showgrid=False, zeroline=False, showticklabels=False)
    fig.update_yaxes(showgrid=False, zeroline=False, showticklabels=False)

    # Adding dummy traces for a custom legend:
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode="markers",
        name="Prime",
        marker=dict(size=7, color="rgb(8,48,107)", symbol='square', line={"width": 1}),
    ))
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode="markers",
        name="Non-Prime",
        marker=dict(size=7, color="rgb(247,251,255)", symbol='square', line={"width": 1}),
    ))

    return fig


if __name__ == '__main__':
    size = int(input("Enter size: "))
    # size = 100
    print("Generating spiral...")
    fig = get_is_prime_fig(create_integer_spiral(size))
    fig.show()
