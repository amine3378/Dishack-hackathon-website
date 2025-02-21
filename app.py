from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages

# Simulated database
patients = [
    {
        "rfid_uid": "123456",
        "name": "Samir Hafeid",
        "age": 35,
        "gender": "Male",
        "password": "patient123",
        "picture": "jhon_smith.png",  # Add a picture file name
        "medical_history": [
            {"date": "2023-10-01", "document": "Blood Test Report", "file": "blood_test.pdf"},
            {"date": "2023-09-15", "document": "X-Ray Scan", "file": "xray_scan.pdf"},
            {"date": "2023-08-20", "document": "Prescription for Antibiotics", "file": "prescription.pdf"}
        ]
    },
    {
        "rfid_uid": "789012",
        "name": "Adel Hamza",
        "age": 28,
        "gender": "Female",
        "password": "patient456",
        "picture": "jane_doe.png",  # Add a picture file name
        "medical_history": [
            {"date": "2023-10-05", "document": "MRI Scan Report", "file": "mri_scan.pdf"},
            {"date": "2023-09-25", "document": "Prescription for Painkillers", "file": "prescription.pdf"}
        ]
    }
]

# Homepage (Doctor Login)
@app.route('/')
def index():
    return render_template('index.html')

# Doctor Login
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Simulated doctor login
    if email == "doctor1@example.com" and password == "password123":
        return redirect(url_for('dashboard'))
    else:
        flash('Login failed. Please check your credentials.', 'error')
        return redirect(url_for('index'))

# Dashboard (Simulate RFID Scan)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Patient Password Verification
@app.route('/verify_patient', methods=['POST'])
def verify_patient():
    rfid_uid = request.form.get('rfid')
    patient_password = request.form.get('password')
    
    # Find patient by RFID UID
    patient = next((p for p in patients if p['rfid_uid'] == rfid_uid), None)
    
    if patient:
        if patient['password'] == patient_password:
            return render_template('patient.html', patient=patient)
        else:
            flash('Incorrect patient password. Please try again.', 'error')
            return redirect(url_for('dashboard'))
    else:
        flash('Patient not found.', 'error')
        return redirect(url_for('dashboard'))

# Serve documents for download
@app.route('/documents/<filename>')
def download_file(filename):
    return send_from_directory('documents', filename)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)