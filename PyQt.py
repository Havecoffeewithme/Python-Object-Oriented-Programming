
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("My First GUI")

# Create widgets
label = QLabel("Welcome to Python!")
button = QPushButton("Click Me")

# Create a layout
layout = QVBoxLayout()

# Add widgets to the layout
layout.addWidget(label)
layout.addWidget(button)

# Set the layout on the window
window.setLayout(layout)

# Display the window
window.show()

# Start the event loop
sys.exit(app.exec_())
