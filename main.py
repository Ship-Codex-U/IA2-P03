import sys
import numpy as np
from sklearn.metrics import confusion_matrix

from module import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Establecer el rango de los ejes coordenados
        self.rangeMinGraphic = -10
        self.rangeMaxGraphic = 10

        self.zoom_factor = 1.2

        self.points = Points()
        self.perceptron = Perceptron()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.figure = Figure()
        self.figure.subplots_adjust(left=0.07, right=0.95, bottom=0.07, top=0.95)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        self.ui.layout_graphic.addWidget(self.canvas)
        self.ui.button_start.clicked.connect(self.click_start_analysis)
        self.ui.button_generate_data_new.clicked.connect(self.generate_new_data)
        self.ui.button_clean.clicked.connect(self.click_clean)
        self.canvas.mpl_connect("button_press_event", self.click_insert_point_mouse)

        self.canvas.mpl_connect("scroll_event", self.on_scroll)
        self.generate_new_data()

        self.init_plot()
        self.show()

    @Slot()
    def click_start_analysis(self):
        input_values = self.points.get_inputs()
        true_values = self.points.get_results()

        if not self.validate_inputs():
            return
        
        alpha = float(self.ui.input_alpha.toPlainText())
        iterations = 1000

        if not self.perceptron.train(input_values, true_values, alpha, iterations):
            QMessageBox.critical(self, "Error", "No se pudo entrenar el perceptrón.")

        weight_01, weight_02 = self.perceptron.weights
        bias = self.perceptron.bias

        self.ui.output_weight_01.setText(str(round(weight_01, 5)))
        self.ui.output_weight_02.setText(str(round(weight_02, 5)))
        self.ui.output_bias.setText(str(round(bias, 2)))

        m, b = self.perceptron.get_MB_equation_line()

        if m is not None:
            self.draw_equation_line(self.rangeMinGraphic, self.rangeMaxGraphic, m, b)
        
        predicted_values = self.perceptron.predict(self.points.get_inputs())

        if len(true_values) != len(predicted_values):
            QMessageBox.critical(self, "Error", "El número de valores verdaderos y predichos no coincide.")
        else:
            tn, fp, fn, tp = confusion_matrix(true_values, predicted_values).ravel()
        
            self.ui.output_true_negatives.setText(str(tn))
            self.ui.output_false_positives.setText(str(fp))
            self.ui.output_false_negatives.setText(str(fn))
            self.ui.output_true_positives.setText(str(tp))
        
            precision = tp / (tp + fp) #¿Que proporcion de identificaciones positivas fue realmente correcta?
            recall = tp / (tp + fn) #¿Que proporcion de positivos reales se identificaron correctamente?
            f1_score = 2 * (precision * recall) / (precision + recall) #Media armónica de precision y recall

            self.ui.output_precision.setText(str(round(precision, 2)))
            self.ui.output_f1_score.setText(str(round(f1_score, 2)))

    
    @Slot()
    def generate_new_data(self):
        self.perceptron.randomize_weights_and_bias()

        weight_01, weight_02 = self.perceptron.weights
        bias = self.perceptron.bias

        self.ui.output_weight_01.setText(str(round(weight_01, 5)))
        self.ui.output_weight_02.setText(str(round(weight_02, 5)))
        self.ui.output_bias.setText(str(round(bias, 5)))

    def click_insert_point_mouse(self, event):
        if event.xdata is not None and event.ydata is not None:
            coord = (event.xdata, event.ydata)
            color = 'black'
            value = 0

            if event.button == 1:
                color = 'blue'
                value = 1
            elif event.button == 3:
                color = 'red'
                value = 0
            else:
                color = 'black'
                value = -1

            self.ax.plot(coord[0], coord[1], 'o', color=color, markersize=4)
            self.ax.annotate(f'({value})', (coord[0], coord[1]), textcoords="offset points", xytext=(0,5), ha='center')

            self.points.insert_point(coord[0], coord[1], value, color)

            self.canvas.draw_idle()

            #self.update_plot()
    
    def draw_equation_line(self, x_min, x_max, m, b):
        x = np.linspace(x_min, x_max + 1, 1000)
        y = m * x + b

        self.ax.plot(x, y, color='red', label=f'y = {m:.2f}x + {b:.2f} ')
        self.ax.legend()
        self.canvas.draw_idle()

    @Slot()
    def click_clean(self):
        self.points.clear()
        self.init_inputs()
        self.init_plot()
        self.init_maetrics()
        self.canvas.draw_idle()
    
    def init_maetrics(self):
        self.ui.output_true_negatives.setText("TN")
        self.ui.output_false_positives.setText("FP")
        self.ui.output_false_negatives.setText("FN")
        self.ui.output_true_positives.setText("TP")
        self.ui.output_precision.setText("")
        self.ui.output_f1_score.setText("")

    def init_plot(self):
        self.ax.clear()
        self.ax.set_xlim(self.rangeMinGraphic, self.rangeMaxGraphic)
        self.ax.set_ylim(self.rangeMinGraphic, self.rangeMaxGraphic)
        self.ax.set_aspect('equal')

        self.ax.spines["left"].set_position("zero")
        self.ax.spines["bottom"].set_position("zero")
        self.ax.spines["right"].set_color("none")
        self.ax.spines["top"].set_color("none")

        self.ax.grid(True, linestyle="--", linewidth=0.5)

        self.ax.set_xticks(np.arange(self.rangeMinGraphic, self.rangeMaxGraphic + 1, 1))
        self.ax.set_yticks(np.arange(self.rangeMinGraphic, self.rangeMaxGraphic + 1, 1))
        
    def init_inputs(self):
        self.ui.input_alpha.setText("")
        self.ui.input_iterations.setText("")
    
    def on_scroll(self, event):
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        x_center = (xlim[0] + xlim[1]) / 2
        y_center = (ylim[0] + ylim[1]) / 2

        if event.step > 0:  # Zoom in
            scale_factor = 1 / self.zoom_factor
        else:  # Zoom out
            scale_factor = self.zoom_factor

        new_xlim = [(x - x_center) * scale_factor + x_center for x in xlim]
        new_ylim = [(y - y_center) * scale_factor + y_center for y in ylim]

        self.ax.set_xlim(new_xlim)
        self.ax.set_ylim(new_ylim)
        self.canvas.draw()
    
    def validate_inputs(self):
        alpha = self.ui.input_alpha.toPlainText()
        iterations = self.ui.input_iterations.toPlainText()

        if not alpha or not iterations:
            QMessageBox.critical(self, "Error", "Alguno de los campos están vacíos, favor de verificar.")    
            return False

        try:
            alpha = float(alpha)
            iterations = int(iterations)
        except ValueError:
            QMessageBox.critical(self, "Error", "Los campos deben ser numéricos, favor de verificar.")
            return False

        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
