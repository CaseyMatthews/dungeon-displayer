from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QComboBox
import sys

class MainWindow(QMainWindow):
    
    # TODO: Idea -- write layout functions with slot functions as parameters. That way the same controls can do different
    #       things depending on the context (main screen, edit screen).
    
    def __init__(self):
        super().__init__()

        # Test Data for now.
        self.campaigns = ['Campaign 1', 'Campaign2', 'Campaign 3']
        self.maps = ['Map1', 'Map2', 'Map3']
        self.rooms = ['room1', 'room2', 'room3']
        
        # window title
        self.setWindowTitle("Dungeon Displayer")
        
        # main Layout
        self.layout = QVBoxLayout()

        # campaign selector label
        self.campaignLabel = QLabel("Campaigns:")
        self.layout.addWidget(self.campaignLabel)
        
        # campaign selector
        self.campaignComboBox = QComboBox()
        self.campaignComboBox.addItems(self.campaigns)
        self.layout.addWidget(self.campaignComboBox)
        self.campaignComboBox.currentIndexChanged.connect(self.campaignSelected)
        
        # map label
        self.mapLabel = QLabel("Maps:")
        self.layout.addWidget(self.mapLabel)
        
        # map selector
        self.mapComboBox = QComboBox()
        self.mapComboBox.addItems(self.maps)
        self.layout.addWidget(self.mapComboBox)
        self.mapComboBox.currentIndexChanged.connect(self.mapSelected)    
        
        # room label
        self.roomLabel = QLabel("Rooms:")
        self.layout.addWidget(self.roomLabel)
        
        # room selector
        self.roomComboBox = QComboBox()
        self.roomComboBox.addItems(self.rooms)
        self.layout.addWidget(self.roomComboBox)
        self.roomComboBox.currentIndexChanged.connect(self.roomSelected)
        
        # horizontal layout
        self.hControlLayout = QHBoxLayout()
        
        # edit mode toggle button
        self.editButton = QPushButton('Edit')
        self.editButton.setCheckable(True)
        self.editButton.setChecked(False)
        self.hControlLayout.addWidget(self.editButton)
        self.editButton.clicked.connect(self.toggle_edit_mode)
        
        # game toggle button
        self.gameButton = QPushButton('Game')
        self.gameButton.setCheckable(True)
        self.gameButton.setChecked(False)
        self.hControlLayout.addWidget(self.gameButton)
        self.gameButton.clicked.connect(self.toggle_game_mode)
        
        # fullscreen toggle button
        self.fullscreenButton = QPushButton('Full Screen')
        self.fullscreenButton.setCheckable(True)
        self.fullscreenButton.setChecked(False)
        self.hControlLayout.addWidget(self.fullscreenButton)
        self.fullscreenButton.clicked.connect(self.toggle_fullscreen_mode)
        
        # add horizontal control to main layout
        self.layout.addLayout(self.hControlLayout)
        
        # add layout to window.
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def campaignSelected(self, index):
        print("Campaign Selected: %s" % self.campaigns[index])
        
    def mapSelected(self, index):
        print("Map selected: %s" % self.maps[index])
        
    def roomSelected(self,index):
        print("Room selected: %s" % self.rooms[index])
        
    def toggle_edit_mode(self, checked):
        print("Edit mode: %s" % checked)
        
    def toggle_game_mode(self, checked):
        print("Game Screen: %s" % checked)
        
    def toggle_fullscreen_mode(self, checked):
        print("Full Screen: %s" % checked)

