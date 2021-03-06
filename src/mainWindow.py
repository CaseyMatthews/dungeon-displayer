from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QComboBox
from PySide2.QtCore import Qt
from gameWindow import GameWindow

class MainWindow(QMainWindow):
    
    # TODO: Idea -- write layout functions with slot functions as parameters. That way the same controls can do different
    #       things depending on the context (main screen, edit screen).
    
    def __init__(self):
        super().__init__()

        # Test Data for now.
        self.campaigns = ['Campaign 1', 'Campaign 2', 'Campaign 3']
        self.maps = ['assets\Redbrand_Hideout_Map_numbered.jpg', 'assets\Redbrand_Hideout_Map_not_numbered.webp']
        self.rooms = ['room1', 'room2', 'room3']
        
        # create a game window
        self.gameWindow = GameWindow(self.maps[0])
        
        # window title
        self.setWindowTitle("Dungeon Displayer")
        
        # main Layout
        self.layout = QVBoxLayout()
        
        # campaign name label
        self.titleLabel = QLabel(self.campaigns[0])
        font = self.titleLabel.font()
        font.setPointSize(25)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignHCenter)
        self.layout.addWidget(self.titleLabel)

        # campaign selector label
        self.campaignLabel = QLabel("Campaigns:")
        self.layout.addWidget(self.campaignLabel)
        
        # campaign selector
        self.campaignComboBox = QComboBox()
        self.campaignComboBox.addItems(self.campaigns)
        self.layout.addWidget(self.campaignComboBox)
        self.campaignComboBox.currentIndexChanged.connect(self.campaign_selected)
        
        # map label
        self.mapLabel = QLabel("Maps:")
        self.layout.addWidget(self.mapLabel)
        
        # map selector
        self.mapComboBox = QComboBox()
        self.mapComboBox.addItems(self.maps)
        self.layout.addWidget(self.mapComboBox)
        self.mapComboBox.currentIndexChanged.connect(self.map_selected)    
        
        # room label
        self.roomLabel = QLabel("Rooms:")
        self.layout.addWidget(self.roomLabel)
        
        # room selector
        self.roomComboBox = QComboBox()
        self.roomComboBox.addItems(self.rooms)
        self.layout.addWidget(self.roomComboBox)
        self.roomComboBox.currentIndexChanged.connect(self.room_selected)
        
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
        self.fullscreenButton.setChecked(self.gameButton.isChecked())
        self.fullscreenButton.setEnabled(self.gameButton.isChecked())
        self.hControlLayout.addWidget(self.fullscreenButton)
        self.fullscreenButton.clicked.connect(self.toggle_fullscreen_mode)
        
        # add horizontal control to main layout
        self.layout.addLayout(self.hControlLayout)
        
        # add layout to window.
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        
    ### LAYOUT FUNCTIONS
        
    ### ACTION FUNCTIONS

    def campaign_selected(self, index):
        print("Campaign Selected: %s" % self.campaigns[index])
        self.set_title_label(self.campaigns[index])
        
    def map_selected(self, index):
        print("Map selected: %s" % self.maps[index])
        self.gameWindow.set_scaled_map_image(self.maps[index])
        
    def room_selected(self,index):
        print("Room selected: %s" % self.rooms[index])
        
    def toggle_edit_mode(self, checked):
        print("Edit mode: %s" % checked)
        
    def toggle_game_mode(self, checked):
        print("Game Screen: %s" % checked)
        self.gameWindow.reset_window_state()
        self.gameWindow.setVisibility(checked)
        self.fullscreenButton.setEnabled(checked)
        self.fullscreenButton.setChecked(False)
        
    def toggle_fullscreen_mode(self, checked):
        print("Full Screen: %s" % checked)
        self.gameWindow.setMaximized(checked)
        
    def set_title_label(self, newTitle):
        self.titleLabel.setText(newTitle)
        
    def closeEvent(self, event):
        self.gameWindow.close()
        event.accept()
        