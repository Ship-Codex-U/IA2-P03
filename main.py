import sys
import numpy as np
from sklearn.metrics import confusion_matrix
import time

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

        self.x_signal_clean = None
        self.y_signal_clean = None

        #Valor auxiliar para poder mostrar u ocultar la señal
        self.line_signal = None
        self.line_signal_noisy = None
        self.line_signal_clean = None

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
        self.ui.button_start_clean.clicked.connect(self.start_clean)
        self.ui.button_erase_signal_clean.clicked.connect(self.remove_signal_clean)

        self.press = None
        self.init_plot()
        self.show()
        
    @Slot()
    def remove_signal_clean(self):
        if self.line_signal_clean:
            self.line_signal_clean[0].remove()
            self.line_signal_clean = None
            self.ax.legend()
            self.canvas.draw_idle()

    @Slot()
    def start_clean(self):
        if self.validate_inputs() and self.validate_upload_data():
            
            if self.line_signal_clean:
                self.remove_signal_clean()

            self.x_signal_clean, self.y_signal_clean = self.generate_clean_signal(
                int(self.ui.input_number_points.toPlainText()),
                float(self.ui.input_alpha.toPlainText()),
                (self.x_signal, self.y_signal),
                (self.x_signal_noisy, self.y_signal_noisy)
            )

            self.line_signal_clean = self.ax.plot(self.x_signal_clean, self.y_signal_clean, color='green', label='Señal Limpia')

            self.ax.legend()
            self.canvas.draw_idle()

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

    def generate_clean_signal(self, step : int , alpha : float, signal_origin_points : tuple, signal_noise_points : tuple):
        x_signal_origin = signal_origin_points[0]
        y_signal_origin = signal_origin_points[1]
        x_signal_noise = signal_noise_points[0]
        y_signal_noise = signal_noise_points[1]

        x_signal_clean = []
        y_signal_clean = []

        adaline = Adaline(step)

        cont = -1

        #Inicializar los valores de la señal limpia con los valores de la señal original el numero de veces que indico el usuario
        #antes de empezar a limpiar la señal

        for i in range(step):
            x_signal_clean.append(x_signal_noise[i])
            y_signal_clean.append(y_signal_noise[i])
            cont += 1
        
        #Empezar a limpiar la señal

        while cont < len(x_signal_origin) - 1:
            inputs = []
            result = []

            for i in range(step - 1, -1, -1):
                inputs.append(y_signal_noise[cont - i])
            #Si step = 3
            #Salidas:
            #       2 - 1 - 0
            
            result = y_signal_noise[cont + 1]
            #Ejemplo
            # Señal con ruido (y) 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - 11
            # step = 3
            # cont = 2
            # result = 5

            x_signal_clean.append(x_signal_noise[cont + 1])
            predic = adaline.predict(inputs, result, alpha)

            y_signal_clean.append(predic)
            cont += 1

        return x_signal_clean, y_signal_clean

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
        alpha = self.ui.input_alpha.toPlainText()

        if not number_points or not alpha:
            QMessageBox.critical(self, "Error", "Alguno de los campos esta vacio, favor de verificar.")    
            return False

        try:
            number_points = int(number_points)
            alpha = float(alpha)
        except ValueError:
            QMessageBox.critical(self, "Error", "Los campos solo acepta valores numericos, favor de verificar.")
            return False

        return True

    def validate_upload_data(self):
        if self.x_signal is None or self.x_signal_noisy is None or self.y_signal is None or self.y_signal_noisy is None:
            QMessageBox.critical(self, "Error", "No se han cargado las señales, favor de verificar.")
            return False
        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
