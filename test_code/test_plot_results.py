from tic_tac.toe.libs.plot_results import results_plot

agentx_x_axis = [1, 2, 3, 4, 5]
agentx_y_axis = [0, 1, 2, 2, 2]
agento_x_axis = [1, 2, 3, 4, 5]
agento_y_axis = [1, 1, 2, 2, 2]
agentd_x_axis = [1, 2, 3, 4, 5]
agentd_y_axis = [0, 0, 0, 0, 1]

result_set = [agentx_x_axis, agentx_y_axis, agento_x_axis,
              agento_y_axis, agentd_x_axis, agentd_y_axis]

plot_title = "this chart"

results_plot(plot_title, result_set)
