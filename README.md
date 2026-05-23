# Face Recognition Attendance System 👤

A desktop application that uses face recognition technology to identify users and automatically record their attendance. Built with Python, OpenCV, and Tkinter, this system provides a secure and efficient way to manage attendance tracking.

## 📋 Features

- **Real-time Face Recognition**: Identify registered users using live webcam feed
- **User Registration**: Easy registration process for new users with face capture
- **Automated Attendance Logging**: Automatically logs attendance with timestamp when user is recognized
- **GUI Interface**: User-friendly desktop application built with Tkinter
- **Local Database**: Stores registered user faces in a local directory
- **Live Webcam Feed**: Real-time video display from webcam for user feedback
- **Error Handling**: Graceful handling of unknown users and errors

## 🛠️ Technologies Used

- **Python** - Programming language
- **OpenCV** - Computer vision and face detection
- **Tkinter** - GUI framework for desktop application
- **PIL/Pillow** - Image processing and display
- **face_recognition** - Face recognition library (command-line utility)

## 📦 Prerequisites

Before installation, ensure you have:
- Python 3.7 or higher
- pip (Python package manager)
- A working webcam
- `face_recognition` command-line tool installed on your system

### Install face_recognition CLI

On Ubuntu/Debian:
```bash
sudo apt-get install -y python3-pip cmake
pip3 install face_recognition
```

On macOS (using Homebrew):
```bash
brew install cmake
pip3 install face_recognition
```

On Windows:
```bash
pip install face_recognition
```

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Dhanushka0626/Face-Recognition-Attendance-System.git
cd Face-Recognition-Attendance-System
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Running the Application

Start the application:
```bash
python main.py
```

### Main Interface

The application opens with a main window showing:
- **Live webcam feed** on the left side
- **Login button** - Click to authenticate your face
- **Register new user button** - Click to register a new user

### Login Process

1. Click the **"Login"** button
2. The system captures your face from the webcam
3. Your face is compared with registered users in the database
4. If recognized, you'll see a welcome message and your attendance is logged
5. If not recognized, you'll be prompted to register

### Registration Process

1. Click **"register new user"** button
2. A new window opens showing your captured face
3. Enter your username in the provided text field
4. Click **"Accept"** to save your face to the database
5. Your face is now registered and you can login

## 📁 Project Structure

```
Face-Recognition-Attendance-System/
├── main.py              # Main application file with GUI
├── util.py              # Utility functions for GUI components
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── LICENSE             # MIT License
├── log.txt             # Attendance log file (auto-generated)
├── db/                 # Database directory for storing face images
│   └── [username].jpg  # Individual user face images
├── example_data/       # Example data for reference
└��─ .gitignore         # Git ignore rules
```

## 💡 How It Works

### Architecture

```
┌─────────────────┐
│   Webcam Feed   │
└────────┬────────┘
         │
    ┌────▼─────┐
    │  OpenCV   │ ──► Capture Frame
    └────┬─────┘
         │
    ┌────▼──────────────┐
    │ face_recognition  │ ──► Compare with DB
    └────┬──────────────┘
         │
    ┌────▼─────────────┐
    │ Match Found?     │
    └────┬─────────┬───┘
    YES  │         │  NO
        ┌▼────┐  ┌─▼──────┐
        │Login│  │ Unknown │
        │ OK  │  │  User   │
        └─────┘  └────────┘
         │
    ┌────▼──────────────┐
    │ Log Attendance    │
    │ Timestamp         │
    └───────────────────┘
```

### Process Flow

1. **Capture**: Application captures frames from webcam in real-time
2. **Detection**: OpenCV detects faces in each frame
3. **Recognition**: Compares detected face with stored face encodings in the database
4. **Identification**: If match found, user is identified; otherwise marked as unknown
5. **Logging**: On successful identification, attendance is logged with timestamp

## 📊 Database Structure

### Face Database (`db/` directory)
- Stores individual face images for each registered user
- File naming: `[username].jpg`
- Each file contains the captured face image used for recognition

### Attendance Log (`log.txt`)
- Records attendance with format: `username,timestamp`
- Example:
```
John,2026-05-23 10:30:45.123456
Sarah,2026-05-23 10:35:12.456789
John,2026-05-23 14:20:33.789123
```

## ⚙️ Requirements

See `requirements.txt`:
```
opencv-python==4.6.0.66
Pillow
```

**System Requirements:**
- `face_recognition` library (command-line tool)
- Working webcam
- Minimum 2GB RAM

## 🔒 Security Considerations

- Face images are stored locally on your machine
- No cloud upload or external server communication
- Access control can be enhanced by adding password protection
- Consider encryption for sensitive deployments

## 🎯 Use Cases

- **Educational Institutions**: Classroom attendance tracking
- **Office Management**: Employee attendance and time-in tracking
- **Secure Access Control**: Access entry to restricted areas
- **Event Management**: Visitor check-in and tracking
- **Building Security**: Automated entry logging

## 🔧 Customization

### Modify GUI Appearance
Edit colors and dimensions in `main.py`:
```python
self.main_window.geometry("1000x500+350+100")  # Window size and position
```

### Change Recognition Confidence
Modify the recognition tolerance in face_recognition comparison

### Add Database Backup
Add functionality to backup face database regularly

## ⚠️ Troubleshooting

### "face_recognition: command not found"
- Ensure face_recognition CLI is properly installed
- Try: `pip install face-recognition`

### Webcam not detected
- Check if your webcam is connected
- Verify webcam permissions for the application
- Try: `python -c "import cv2; cv2.VideoCapture(0)"`

### Poor recognition accuracy
- Ensure proper lighting conditions
- Register multiple face angles for better accuracy
- Increase database with more user samples

### Database directory not found
- The `db/` directory is auto-created on first run
- Ensure write permissions in the application directory

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Dhanushka0626**
- GitHub: [@Dhanushka0626](https://github.com/Dhanushka0626)

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For issues or questions about the project, please open an issue on the [GitHub Issues](https://github.com/Dhanushka0626/Face-Recognition-Attendance-System/issues) page.

## 🚀 Future Enhancements

- [ ] Web-based interface for remote attendance viewing
- [ ] Database migration to SQL for better data management
- [ ] Multi-face detection and logging in one frame
- [ ] User management dashboard
- [ ] Export attendance reports (PDF, Excel)
- [ ] Camera calibration for improved accuracy
- [ ] Real-time statistics and analytics
- [ ] Mobile app integration

---

**Note**: This system requires adequate lighting conditions for optimal face recognition performance. Registration images should be clear and well-lit for better accuracy during login attempts.
