# Face Recognition Based Smart Attendance System Using Python & Machine Learning, Face Recognition Based Smart Attendance System Using Python & Machine Learning,
The Face Recognition-Based Smart Attendance System is an innovative application of Python and Machine Learning that streamlines the traditional attendance tracking process. By leveraging facial recognition technology, this system offers a seamless and efficient way to record attendance.
The system operates in real-time, enabling instant updates to attendance records as individuals are recognized.
The K-Nearest Neighbors (KNN) Algorithm is used for Face Detection.
# Steps:
Before applying KNN, facial features are extracted from the images.
Techniques like Histogram of Oriented Gradients (HOG), Local Binary Patterns (LBP), or deep learning-based methods (like Convolutional Neural Networks - CNNs) are used for feature extraction.
Images are typically preprocessed to ensure uniformity and reduce noise.
Preprocessing includes resizing, normalization, and grayscale conversion.
Each face is represented by its extracted features (HOG, LBP, etc.) and associated with a label (person's name or ID).
Once the dataset is prepared, the KNN model is trained on the extracted features and labels.
The KNN algorithm stores the feature vectors and their corresponding labels.
When a new face is encountered (either from live video or images), its features are extracted using the same method used during training.
The KNN model is then used to predict the label (person's name or ID) of the new face based on its nearest neighbors in the training data.
