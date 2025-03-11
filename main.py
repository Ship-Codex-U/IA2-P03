import sys
import numpy as np
from sklearn.metrics import confusion_matrix

from module import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Establecemos el rango de los ejes coordenados
        self.rangeXMinGraphic = 0
        self.rangeXMaxGraphic = 60
        self.rangeYMinGraphic = -3
        self.rangeYMaxGraphic = 3

        self.zoom_factor = 1.5

        #Valores de las señales
        self.x_signal = None
        self.y_signal = None

        self.x_signal_noisy = None
        self.y_signal_noisy = None

        #Valor auxiliar para poder mostrar u ocultar la señal
        self.line_signal = None
        self.line_signal_noisy = None

        self.points = Points()
        self.perceptron = Perceptron()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Configuramos el plano cartesiano
        self.figure = Figure()
        self.figure.subplots_adjust(left=0.07, right=0.95, bottom=0.07, top=0.95)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        self.ui.layout_graphic.addWidget(self.canvas)

        #Conectamos eventos para el zoom y el arrastre del plano
        self.canvas.mpl_connect("scroll_event", self.on_scroll)
        self.canvas.mpl_connect("button_press_event", self.on_press)
        self.canvas.mpl_connect("motion_notify_event", self.on_motion)
        self.canvas.mpl_connect("button_release_event", self.on_release)


        #Conectamos los eventos de los botones
        self.ui.button_open_signal.clicked.connect(self.open_signal)
        self.ui.button_open_signal_noisy.clicked.connect(self.open_signal_noisy)
        self.ui.button_show_signal.clicked.connect(self.show_signal)
        self.ui.button_show_signa_noisy.clicked.connect(self.show_signal_noisy)
        self.ui.button_hide_signal.clicked.connect(self.hide_signal)
        self.ui.button_hide_signal_noisy.clicked.connect(self.hide_signal_noisy)

        self.press = None
        self.init_plot()
        self.show()
    
    @Slot()
    def show_signal(self):
        if self.line_signal:
            self.line_signal[0].set_visible(True)
            self.canvas.draw_idle()
    
    @Slot()
    def show_signal_noisy(self):
        if self.line_signal_noisy:
            self.line_signal_noisy[0].set_visible(True)
            self.canvas.draw_idle()
    
    @Slot()
    def hide_signal(self):
        if self.line_signal:
            self.line_signal[0].set_visible(False)
            self.canvas.draw_idle()
    
    @Slot()
    def hide_signal_noisy(self):
        if self.line_signal_noisy:
            self.line_signal_noisy[0].set_visible(False)
            self.canvas.draw_idle()

    @Slot( )
    def open_signal(self):
        self.x_signal, self.y_signal, self.line_signal = self.open_and_draw_data('blue', 'Señal Original')

    @Slot( )
    def open_signal_noisy(self):
        self.x_signal_noisy, self.y_signal_noisy, self.line_signal_noisy = self.open_and_draw_data('red', 'Señal con Ruido')
    
    # @Slot()
    # def click_start_analysis(self):
    #     input_values = self.points.get_inputs()
    #     true_values = self.points.get_results()

    #     if not self.validate_inputs():
    #         return
        
    #     alpha = float(self.ui.input_alpha.toPlainText())
    #     iterations = 1000

    #     if not self.perceptron.train(input_values, true_values, alpha, iterations):
    #         QMessageBox.critical(self, "Error", "No se pudo entrenar el perceptrón.")

    #     weight_01, weight_02 = self.perceptron.weights
    #     bias = self.perceptron.bias

    #     self.ui.output_weight_01.setText(str(round(weight_01, 5)))
    #     self.ui.output_weight_02.setText(str(round(weight_02, 5)))
    #     self.ui.output_bias.setText(str(round(bias, 2)))

    #     m, b = self.perceptron.get_MB_equation_line()

    #     if m is not None:
    #         self.draw_equation_line(self.rangeMinGraphic, self.rangeMaxGraphic, m, b)
        
    #     predicted_values = self.perceptron.predict(self.points.get_inputs())

    #     if len(true_values) != len(predicted_values):
    #         QMessageBox.critical(self, "Error", "El número de valores verdaderos y predichos no coincide.")
    #     else:
    #         tn, fp, fn, tp = confusion_matrix(true_values, predicted_values).ravel()
        
    #         self.ui.output_true_negatives.setText(str(tn))
    #         self.ui.output_false_positives.setText(str(fp))
    #         self.ui.output_false_negatives.setText(str(fn))
    #         self.ui.output_true_positives.setText(str(tp))
        
    #         precision = tp / (tp + fp) #¿Que proporcion de identificaciones positivas fue realmente correcta?
    #         recall = tp / (tp + fn) #¿Que proporcion de positivos reales se identificaron correctamente?
    #         f1_score = 2 * (precision * recall) / (precision + recall) #Media armónica de precision y recall

    #         self.ui.output_precision.setText(str(round(precision, 2)))
    #         self.ui.output_f1_score.setText(str(round(f1_score, 2)))

    
    # @Slot()
    # def generate_new_data(self):
    #     self.perceptron.randomize_weights_and_bias()

    #     weight_01, weight_02 = self.perceptron.weights
    #     bias = self.perceptron.bias

    #     self.ui.output_weight_01.setText(str(round(weight_01, 5)))
    #     self.ui.output_weight_02.setText(str(round(weight_02, 5)))
    #     self.ui.output_bias.setText(str(round(bias, 5)))

    # def click_insert_point_mouse(self, event):
    #     if event.xdata is not None and event.ydata is not None:
    #         coord = (event.xdata, event.ydata)
    #         color = 'black'
    #         value = 0

    #         if event.button == 1:
    #             color = 'blue'
    #             value = 1
    #         elif event.button == 3:
    #             color = 'red'
    #             value = 0
    #         else:
    #             color = 'black'
    #             value = -1

    #         self.ax.plot(coord[0], coord[1], 'o', color=color, markersize=4)
    #         self.ax.annotate(f'({value})', (coord[0], coord[1]), textcoords="offset points", xytext=(0,5), ha='center')

    #         self.points.insert_point(coord[0], coord[1], value, color)

    #         self.canvas.draw_idle()

    #         #self.update_plot()
    
    # def draw_equation_line(self, x_min, x_max, m, b):
    #     x = np.linspace(x_min, x_max + 1, 1000)
    #     y = m * x + b

    #     self.ax.plot(x, y, color='red', label=f'y = {m:.2f}x + {b:.2f} ')
    #     self.ax.legend()
    #     self.canvas.draw_idle()

    # @Slot()
    # def click_clean(self):
    #     self.points.clear()
    #     self.init_inputs()
    #     self.init_plot()
    #     self.init_maetrics()
    #     self.canvas.draw_idle()
    
    # def init_maetrics(self):
    #     self.ui.output_true_negatives.setText("TN")
    #     self.ui.output_false_positives.setText("FP")
    #     self.ui.output_false_negatives.setText("FN")
    #     self.ui.output_true_positives.setText("TP")
    #     self.ui.output_precision.setText("")
    #     self.ui.output_f1_score.setText("")

    def open_and_draw_data(self, colorLine : str, labelGraphic : str):
        x = None
        y = None
        line = None

        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'TXT (*.txt)'
        )[0]
        
        if ubicacion:
            x, y = self.load_data(ubicacion)

            if x is not None and y is not None:                
                line = self.ax.plot(x, y, color=colorLine, label=labelGraphic)
                self.ax.legend()
                self.canvas.draw_idle()

            else: 
                QMessageBox.critical(self, "Alerta", "El archivo no se pudo abrir correctamente.", QMessageBox.Ok)    
        else: 
            QMessageBox.critical(self, "Alerta", "El archivo no se pudo abrir correctamente.", QMessageBox.Ok)

        return x, y, line

    def load_data(self, filepath):
        try:
            data = np.loadtxt(filepath)
            x = data[:, 0]
            y = data[:, 1]
            return x, y
        except Exception as e:
            return None, None

    def init_plot(self):
        self.ax.clear()
        self.ax.set_xlim(self.rangeXMinGraphic, self.rangeXMaxGraphic)
        self.ax.set_ylim(self.rangeYMinGraphic, self.rangeYMaxGraphic)
        self.ax.set_aspect('auto')

        self.ax.spines["left"].set_position("zero")
        self.ax.spines["bottom"].set_position("zero")
        self.ax.spines["right"].set_color("none")
        self.ax.spines["top"].set_color("none")

        self.ax.grid(True, linestyle="--", linewidth=0.5)

        self.ax.set_xticks(np.arange(self.rangeXMinGraphic, self.rangeXMaxGraphic + 1, 1))
        self.ax.set_yticks(np.arange(self.rangeYMinGraphic, self.rangeYMaxGraphic + 1, 1))
        
    def init_inputs(self):
        self.ui.input_number_points.setText("")
    
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

        # Bloqueo para evitar zoom out fuera del tamaño original del plano
        if new_xlim[0] < self.rangeXMinGraphic:
            new_xlim[0] = self.rangeXMinGraphic
        if new_xlim[1] > self.rangeXMaxGraphic:
            new_xlim[1] = self.rangeXMaxGraphic
        if new_ylim[0] < self.rangeYMinGraphic:
            new_ylim[0] = self.rangeYMinGraphic
        if new_ylim[1] > self.rangeYMaxGraphic:
            new_ylim[1] = self.rangeYMaxGraphic

        self.ax.set_xlim(new_xlim)
        self.ax.set_ylim(new_ylim)
        self.canvas.draw()

    def on_press(self, event):
        if event.inaxes != self.ax:
            return
        self.press = event.xdata, event.ydata

    def on_motion(self, event):
        if self.press is None or event.inaxes != self.ax:
            return
        x_prev, y_prev = self.press
        dx = event.xdata - x_prev
        dy = event.ydata - y_prev

        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        new_xlim = [x - dx for x in xlim]
        new_ylim = [y - dy for y in ylim]

        # Bloqueo para evitar arrastrar fuera del tamaño original del plano
        if new_xlim[0] < self.rangeXMinGraphic:
            new_xlim[0] = self.rangeXMinGraphic
        if new_xlim[1] > self.rangeXMaxGraphic:
            new_xlim[1] = self.rangeXMaxGraphic
        if new_ylim[0] < self.rangeYMinGraphic:
            new_ylim[0] = self.rangeYMinGraphic
        if new_ylim[1] > self.rangeYMaxGraphic:
            new_ylim[1] = self.rangeYMaxGraphic

        self.ax.set_xlim(new_xlim)
        self.ax.set_ylim(new_ylim)
        self.canvas.draw()

    def on_release(self, event):
        self.press = None
        self.canvas.draw()
    
    def validate_inputs(self):
        number_points = self.ui.input_number_points.toPlainText()

        if not number_points:
            QMessageBox.critical(self, "Error", "El campo esta vacio, favor de verificar.")    
            return False

        try:
            number_points = int(number_points)
        except ValueError:
            QMessageBox.critical(self, "Error", "El campo solo acepta valores numericos, favor de verificar.")
            return False

        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
