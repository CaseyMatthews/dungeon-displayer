from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt

class GameWindow(QWidget):
    
    def __init__(self, defaultImagePath, displayed=False):
        super().__init__()        
        self.label = QLabel("Game Window")
        self.ogMapImage = QPixmap(defaultImagePath)
        self.label.setPixmap(self.ogMapImage)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.setVisibility(displayed)
        self.setMinimumSize(500, 500)
        self.defaultWindowFlags = self.windowFlags()
        
    def setVisibility(self, visible):
        if(visible):
            self.show()
        else:
            self.hide()
            
    def setMaximized(self, maximized):
        if(maximized):
            self.maximize_window_state()
            
        else:
            self.reset_window_state()     
    
    def maximize_window_state(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.showMaximized()
    
    def reset_window_state(self):
        self.setWindowFlags(self.defaultWindowFlags)
        self.setVisibility(True)
        self.showNormal()
        self.resize(500,500)
        
    def set_map_image(self, imagePath):
        self.ogMapImage = QPixmap(imagePath)
    
    def scale_map_image(self):
        image = self.ogMapImage.scaled(self.width(), self.height())
        self.label.setPixmap(image)
        
    def set_scaled_map_image(self, imagePath):
        self.set_map_image(imagePath)
        self.scale_map_image()
        
    def resizeEvent(self, event):
        # self.label.resize(self.width(), self.height())
        # image = self.ogMapImage.scaled(self.width(), self.height())
        # self.label.setPixmap(image)
        self.scale_map_image()
        event.accept()